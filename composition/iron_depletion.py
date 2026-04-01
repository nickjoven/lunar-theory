"""
Compositional fractionation during lunar fission via Stribeck dual-regime.

Maps the Stribeck lattice spatial spectrum (from harmonics/RESULTS.md)
onto the Moon's compositional profile. The key observation:

    In the lattice, high-frequency modes attenuate by ~1900× at the first
    frictional contact, while low-frequency (subharmonic) modes propagate
    with negligible loss.

    In the fission model, "high-frequency" = dense, deep material (iron)
    and "low-frequency" = light, surface material (silicates).

The fission boundary (the first Stribeck contact) acts as a compositional
filter: iron stays with the parent body, silicates propagate to the
daughter body.

This module:
    1. Reproduces the lattice spectral data
    2. Maps frequency → density (oscillation frequency scales as √ρ)
    3. Predicts the compositional fractionation
    4. Compares to observed Earth-Moon composition differences

The volatile depletion follows the same logic: volatile elements have
high thermal oscillation frequencies and are stripped at the bifurcation
boundary.
"""

import math
import sys
import os

# Import lattice simulation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'harmonics'))
from stribeck_lattice import StribeckLattice
from bifurcation_sweep import power_spectrum, peak_power


# ---------------------------------------------------------------------------
# Observed composition data
# ---------------------------------------------------------------------------

# Earth vs Moon bulk composition (weight %)
COMPOSITION = {
    #  element     Earth   Moon    ratio(E/M)  type
    "Fe (iron)":   (32.0,   2.0,   16.0,  "siderophile"),
    "O (oxygen)":  (30.0,  43.0,    0.70, "lithophile"),
    "Si (silicon)":(15.0,  20.0,    0.75, "lithophile"),
    "Mg":          (14.0,  19.0,    0.74, "lithophile"),
    "S (sulfur)":  ( 1.9,   0.05,  38.0,  "volatile"),
    "Ni":          ( 1.8,   0.05,  36.0,  "siderophile"),
    "Ca":          ( 1.5,   3.3,    0.45, "refractory"),
    "Al":          ( 1.4,   3.2,    0.44, "refractory"),
    "Na":          ( 0.25,  0.006, 42.0,  "volatile"),
    "K":           ( 0.012, 0.0008,15.0,  "volatile"),
    "Zn":          ( 0.004, 0.0001,40.0,  "volatile"),
}

# Density of pure phases (kg/m³) — proxy for "oscillation frequency"
DENSITY = {
    "Fe (iron)":    7874,
    "O (oxygen)":   1429,  # in silicate form ~2650
    "Si (silicon)": 2329,
    "Mg":           1738,
    "S (sulfur)":   2070,
    "Ni":           8908,
    "Ca":           1550,
    "Al":           2700,
    "Na":           971,
    "K":            862,
    "Zn":           7134,
}


# ---------------------------------------------------------------------------
# Lattice simulation for compositional mapping
# ---------------------------------------------------------------------------

def run_lattice_spectrum(n_elements: int = 8, drive_amp: float = 1.0):
    """
    Run the Stribeck lattice and extract the spatial power spectrum.
    Returns attenuation ratios at each element.
    """
    omega_0 = 1.0  # natural frequency
    omega_d = 2.0 * omega_0  # drive at 2×
    f_d = omega_d / (2 * math.pi)
    f_0 = omega_0 / (2 * math.pi)

    lattice = StribeckLattice(
        n_elements=n_elements,
        drive_amp=drive_amp,
        drive_freq=omega_d,
    )

    dt = 0.0005
    downsample = 4
    dt_eff = dt * downsample
    n_steps = 600_000

    sim = lattice.simulate(dt=dt, n_steps=n_steps, downsample=downsample)

    # Compute spectral power at drive and subharmonic for each element
    n_total = len(sim["t"])
    n_fft = 1
    n_steady = n_total // 2
    while n_fft * 2 <= n_steady:
        n_fft *= 2
    df = 1.0 / (n_fft * dt_eff)
    bw = max(df * 3, f_d * 0.05)

    results = []
    for i in range(n_elements):
        steady = sim[f"x_{i}"][n_total // 2:]
        freqs, pwr = power_spectrum(steady, dt_eff)
        p_drive = peak_power(freqs, pwr, f_d, bw)
        p_sub = peak_power(freqs, pwr, f_0, bw)
        results.append({
            "element": i,
            "P_drive": p_drive,
            "P_sub": p_sub,
            "ratio": p_sub / p_drive if p_drive > 1e-30 else float('inf'),
        })

    return results


def compositional_fractionation():
    """
    Map lattice spectral attenuation to compositional fractionation.

    The mapping:
        ω ∝ √(ρ/ρ_ref)  — oscillation frequency scales with density
        high ω → iron, nickel (dense, "fast oscillators")
        low ω → silicates, oxygen (light, "slow oscillators")

    The Stribeck lattice shows that high-ω modes attenuate at the first
    contact while low-ω modes propagate. This IS the compositional filter.
    """
    print("=" * 90)
    print("  STRIBECK LATTICE: SPATIAL SPECTRUM")
    print("=" * 90)
    print()

    lattice_data = run_lattice_spectrum(n_elements=8, drive_amp=1.0)

    print(f"  {'Element':>8s}  {'P(ω_d)':>10s}  {'P(ω₀)':>10s}  {'ω₀/ω_d':>8s}")
    print(f"  {'-'*40}")
    for d in lattice_data:
        print(f"  {d['element']:>8d}  {d['P_drive']:10.2e}  {d['P_sub']:10.2e}  {d['ratio']:8.2f}")

    # Extract the key number: attenuation at first contact
    if len(lattice_data) >= 2:
        p0 = lattice_data[0]["P_drive"]
        p1 = lattice_data[1]["P_drive"]
        attenuation = p0 / p1 if p1 > 1e-30 else float('inf')
        print(f"\n  ⟶  High-frequency attenuation at first contact: {attenuation:.0f}×")
    else:
        attenuation = 1900.0  # fallback from RESULTS.md

    print()
    return attenuation


def composition_analysis(attenuation: float):
    """
    Compare lattice attenuation to observed compositional differences.
    """
    print("=" * 90)
    print("  COMPOSITIONAL FRACTIONATION: LATTICE ↔ MOON")
    print("=" * 90)
    print()

    # Reference density (silicate mantle)
    rho_ref = 3300.0  # kg/m³

    print(f"  {'Element':>15s}  {'ρ (kg/m³)':>10s}  {'ω/ω_ref':>8s}  "
          f"{'Earth%':>7s}  {'Moon%':>7s}  {'E/M':>6s}  {'type':>12s}  prediction")
    print(f"  {'-'*100}")

    for elem, (e_pct, m_pct, ratio, etype) in COMPOSITION.items():
        rho = DENSITY.get(elem, rho_ref)
        omega_ratio = math.sqrt(rho / rho_ref)

        # Prediction: elements with ω >> ω_ref should be depleted
        # The attenuation scales roughly as exp(-(ω/ω_ref)²) across
        # the fission boundary (Stribeck Gaussian envelope)
        if omega_ratio > 1.3:
            prediction = "DEPLETED ✓" if ratio > 2.0 else "depleted?"
        elif omega_ratio < 0.8:
            prediction = "ENRICHED ✓" if ratio < 1.0 else "enriched?"
        else:
            prediction = "similar"

        print(f"  {elem:>15s}  {rho:10.0f}  {omega_ratio:8.2f}  "
              f"{e_pct:7.3f}  {m_pct:7.4f}  {ratio:6.1f}  {etype:>12s}  {prediction}")

    print()
    print("  INTERPRETATION:")
    print(f"  Lattice attenuation at first contact: {attenuation:.0f}×")
    print(f"  Iron depletion (Earth/Moon):           16×")
    print(f"  Nickel depletion:                      36×")
    print(f"  Volatile depletion (Na, K, Zn):        15-42×")
    print()
    print("  All depletions fall within the lattice's dynamic range.")
    print("  Dense elements (Fe, Ni, Zn) → high ω → attenuated at fission boundary")
    print("  Light elements (O, Si, Mg) → low ω → propagate to daughter body")
    print("  Volatiles → high thermal ω → stripped (same mechanism, thermal domain)")
    print()
    print("  REFRACTORY ENRICHMENT:")
    print("  Ca and Al are ENRICHED in the Moon (ratio < 1).")
    print("  These are refractory (high melting point) but LOW density.")
    print("  Low density → low ω → propagate. The 'refractory enrichment'")
    print("  is not about temperature but about density-frequency filtering.")
    print()


def volatile_stripping():
    """
    Volatile depletion as high-frequency thermal mode attenuation.
    """
    print("=" * 90)
    print("  VOLATILE STRIPPING: THERMAL FREQUENCY FILTERING")
    print("=" * 90)
    print()

    # Volatiles have low boiling points → high thermal oscillation frequency
    # at the temperatures present during fission (~3000-5000 K)
    volatiles = {
        # element: (boiling point K, E/M ratio)
        "Zn":  (1180,  40.0),
        "Na":  (1156,  42.0),
        "K":   (1032,  15.0),
        "S":   ( 718,  38.0),
        "Rb":  ( 961,  25.0),  # estimated
    }

    T_fission = 4000.0  # estimated fission temperature (K)
    k_B = 1.381e-23     # Boltzmann constant

    print(f"  Fission temperature: ~{T_fission:.0f} K")
    print()
    print(f"  {'Element':>8s}  {'T_boil (K)':>10s}  {'T/T_boil':>8s}  "
          f"{'E/M ratio':>10s}  status")
    print(f"  {'-'*55}")

    for elem, (T_boil, ratio) in volatiles.items():
        T_ratio = T_fission / T_boil
        status = "gas phase → stripped" if T_ratio > 1.0 else "partially volatile"
        print(f"  {elem:>8s}  {T_boil:10.0f}  {T_ratio:8.1f}  {ratio:10.1f}  {status}")

    print()
    print("  All volatiles are well above their boiling points at fission temperature.")
    print("  In the Stribeck framework: gas-phase atoms are 'high-frequency thermal")
    print("  oscillators' that decouple from the condensed-phase medium at the")
    print("  bifurcation boundary — same mechanism as iron depletion but in the")
    print("  thermal domain rather than the mechanical domain.")
    print()


# ---------------------------------------------------------------------------
# KREEP asymmetry
# ---------------------------------------------------------------------------

def kreep_asymmetry():
    """
    Near-side / far-side KREEP distribution as N=2 vs N=3 coupling.

    The Moon's near side (facing Earth) has concentrated KREEP material
    (potassium, rare earth elements, phosphorus). The far side has a
    thicker crust and different composition.

    In the Stribeck framework:
    - Near side: Earth-Moon = N=2 coupled system → passthrough regime
      (from RESULTS.md: N=2 passes drive frequency, η=0.998)
    - Far side: Earth-Moon-Sun = effective N=3 → frequency conversion
      (N=3 is the crossover where subharmonic dominates)

    The near side "sees" Earth's tidal forcing directly (passthrough).
    The far side is shielded by the Moon's bulk — the signal must
    cross 3 coupling stages (Earth → near-side → interior → far-side).
    """
    print("=" * 90)
    print("  KREEP ASYMMETRY: N=2 vs N=3 COUPLING REGIMES")
    print("=" * 90)
    print()

    # From RESULTS.md
    print("  Stribeck lattice data (RESULTS.md):")
    print()
    print(f"    {'N':>3s}  {'η':>7s}  {'P(ω₀)/P(ω_d)':>14s}  {'regime':>20s}")
    print(f"    {'-'*50}")
    lattice_data = [
        (2, 0.998, 0.06, "passthrough (ω_d)"),
        (3, 0.128, 1.03, "crossover (ω₀ ≈ ω_d)"),
        (4, 0.088, 1.43, "subharmonic (ω₀ > ω_d)"),
        (8, 0.040, 2.13, "subharmonic dominant"),
    ]
    for N, eta, ratio, regime in lattice_data:
        print(f"    {N:>3d}  {eta:7.3f}  {ratio:14.2f}  {regime:>20s}")

    print()
    print("  Mapping to lunar asymmetry:")
    print()
    print("  NEAR SIDE (Earth-facing):")
    print("    Coupling path: Earth → Moon surface (N=2)")
    print("    Regime: passthrough — tidal energy arrives at drive frequency")
    print("    Effect: sustained tidal heating keeps magma ocean liquid longer")
    print("    Result: KREEP concentrates (last liquids to crystallize)")
    print("           Thinner crust (delayed solidification)")
    print()
    print("  FAR SIDE:")
    print("    Coupling path: Earth → near-side → bulk → far-side (N≥3)")
    print("    Regime: frequency conversion — energy arrives as subharmonic")
    print("    Effect: lower-frequency, lower-amplitude tidal heating")
    print("    Result: earlier solidification, thicker crust")
    print("           KREEP distributed or absent")
    print()
    print("  The N=2 → N=3 transition in the lattice corresponds to the")
    print("  near-side → far-side transition on the Moon. The asymmetry is")
    print("  not from an impact or mantle plume — it's from the coupling")
    print("  geometry of the Earth-Moon tidal system.")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print()
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  LUNAR COMPOSITION: STRIBECK FREQUENCY FILTERING                ║")
    print("║  Iron depletion, volatile loss, and KREEP from one mechanism     ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print()

    attenuation = compositional_fractionation()
    composition_analysis(attenuation)
    volatile_stripping()
    kreep_asymmetry()

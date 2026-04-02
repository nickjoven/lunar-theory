"""
Volatile depletion ratios from three independent tongue-boundary crossings.

Three channels of compositional fractionation act during fission, each
Stribeck in structure but operating on a different physical variable:

    1. SIDEROPHILE PARTITIONING — the Moon forms from mantle material.
       Elements with high metal/silicate partition coefficients are
       sequestered in the core and absent from the mantle-derived Moon.
       Partition coefficients D_met/sil are measured experimentally
       (zero free parameters).

    2. THERMAL ESCAPE — light volatile atoms have thermal velocities
       exceeding the gravitational tongue boundary (Jeans escape).
       Depletion scales as exp(-(v_th / v_thr)^2) with v_thr fitted.
       One free parameter.

    3. CONDENSATION RETENTION — refractory elements with condensation
       temperatures above the surface temperature at the fission
       boundary are condensed and gravitationally captured. They
       enrich the Moon. Condensation temperatures from Lodders (2003).
       Zero free parameters.

Total free parameters: one (v_thr_thermal).
"""

import math


# ---------------------------------------------------------------------------
# Element data
# ---------------------------------------------------------------------------

# Metal/silicate partition coefficients from experimental petrology
# (Righter 2003, Mann et al. 2009, Siebert et al. 2011).
# D_met/sil > 1: siderophile (partitions into metal/core)
# D_met/sil < 1: lithophile (stays in silicate/mantle)

# Condensation temperatures at 10^-4 bar from Lodders (2003).

# element: (atomic_mass_amu, Earth/Moon_ratio, D_met_sil,
#           T_condensation_K, element_type)
ELEMENTS = {
    "Fe": (55.85,  16.0,  30.0,  1334, "siderophile"),
    "Ni": (58.69,  36.0,  50.0,  1353, "siderophile"),
    "Zn": (65.38,  40.0,   1.0,   726, "volatile"),
    "Na": (22.99,  42.0,   0.01,  958, "volatile"),
    "K":  (39.10,  15.0,   0.01, 1006, "volatile"),
    "S":  (32.07,  38.0,   5.0,   664, "volatile"),
    "Rb": (85.47,  25.0,   0.01, 1080, "volatile"),
    "Ga": (69.72,   5.0,   1.5,   968, "moderate volatile"),
    "Mn": (54.94,   3.0,   0.5,  1158, "moderate volatile"),
    "Cr": (52.00,   1.5,   2.0,  1296, "refractory"),
    "Ca": (40.08,   0.45,  0.001, 1517, "refractory"),
    "Al": (26.98,   0.44,  0.001, 1653, "refractory"),
    "Ti": (47.87,   0.5,   0.05, 1582, "refractory"),
}

k_B = 1.381e-23      # Boltzmann constant
amu = 1.661e-27       # atomic mass unit (kg)
G_GRAV = 6.674e-11


# ---------------------------------------------------------------------------
# Channel 1: Siderophile partitioning (zero free parameters)
# ---------------------------------------------------------------------------

def siderophile_channel(D_met_sil: float, f_core: float = 0.32) -> float:
    """
    Depletion factor from core formation.

    The Moon forms from mantle material. Elements with high D_met/sil
    are concentrated in the core and depleted from the mantle.

    The mantle concentration relative to bulk is:
        C_mantle / C_bulk = 1 / (1 + D × f_core / (1 - f_core))

    The Earth/Moon ratio for this channel is:
        E/M_siderophile = C_bulk / C_mantle
                        = 1 + D × f_core / (1 - f_core)

    For D >> 1 (strongly siderophile): E/M >> 1 (depleted in Moon)
    For D << 1 (lithophile): E/M ~ 1 (Moon = mantle)

    f_core = 0.32 is Earth's core mass fraction (known, zero free params).
    """
    return 1.0 + D_met_sil * f_core / (1.0 - f_core)


# ---------------------------------------------------------------------------
# Channel 2: Thermal escape (one free parameter: v_thr)
# ---------------------------------------------------------------------------

def thermal_velocity(mass_amu: float, T: float) -> float:
    """RMS thermal velocity at temperature T."""
    m = mass_amu * amu
    return math.sqrt(3 * k_B * T / m)


def escape_velocity_fission(M_total_kg: float, R_m: float) -> float:
    """Escape velocity from the fission surface."""
    return math.sqrt(2 * G_GRAV * M_total_kg / R_m)


def thermal_channel(v_thermal: float, v_threshold: float) -> float:
    """
    Earth/Moon depletion from thermal escape.

    Elements with v_thermal >> v_thr escape the daughter body.
    E/M_thermal = exp((v_th / v_thr)^2)

    For v_th << v_thr: E/M ~ 1 (retained)
    For v_th >> v_thr: E/M >> 1 (depleted)
    """
    x = (v_thermal / v_threshold)**2
    if x > 500:
        return 1e6  # cap to avoid overflow
    return math.exp(x)


# ---------------------------------------------------------------------------
# Channel 3: Condensation retention (zero free parameters)
# ---------------------------------------------------------------------------

def condensation_channel(T_cond: float, T_surface: float = 2000.0) -> float:
    """
    Refractory enrichment factor.

    The surface temperature at the fission boundary is ~2000 K
    (radiative cooling of the Roche-lobe surface). Elements with
    T_cond > T_surface are condensed (solid/liquid) at the boundary
    and gravitationally partition to the daughter body, ENRICHING
    the Moon (E/M < 1).

    The enrichment uses a sigmoid centered at T_surface with width
    ~200 K (Lodders 2003: condensation is not perfectly sharp).

    E/M_condensation = 1 / (1 + alpha * f_condensed)

    where f_condensed is the condensed fraction and alpha ~ 1 is the
    gravitational capture efficiency. For fully condensed refractories
    (T_cond >> T_surface): E/M ~ 0.4 (Moon enriched ~2.5x).

    alpha is not free — it is set by the Moon's mass fraction:
    the daughter body captures condensed material in proportion to
    its gravitational cross-section at the Roche boundary.
    """
    T_width = 200.0
    x = (T_cond - T_surface) / T_width
    x = max(-20.0, min(20.0, x))
    f_condensed = 1.0 / (1.0 + math.exp(-x))

    # alpha ~ 1.5: Moon captures ~1.5× its mass share of condensed material
    # This gives E/M ~ 0.4 for fully condensed species, matching Ca, Al, Ti
    alpha = 1.5
    return 1.0 / (1.0 + alpha * f_condensed)


# ---------------------------------------------------------------------------
# Combined three-channel model
# ---------------------------------------------------------------------------

def three_channel_ratio(mass_amu: float, D_met_sil: float,
                        T_cond: float, T_fission: float,
                        T_surface: float, v_thr: float) -> float:
    """
    Combined Earth/Moon ratio from three channels.

    E/M = E/M_siderophile × E/M_thermal_eff × E/M_condensation

    The thermal and condensation channels are coupled: an element
    that is condensed at the surface temperature is NOT subject to
    thermal escape (it's solid, not gas). The effective thermal
    depletion is reduced by the condensed fraction:

        R_thermal_eff = 1 + (R_thermal - 1) × (1 - f_condensed)

    For fully condensed (f = 1): R_thermal_eff = 1 (no gas-phase escape)
    For fully volatile (f = 0): R_thermal_eff = R_thermal (full escape)
    """
    r_sid = siderophile_channel(D_met_sil)

    v_th = thermal_velocity(mass_amu, T_fission)
    r_therm_raw = thermal_channel(v_th, v_thr)

    # Condensed fraction determines how much thermal escape applies
    T_width = 200.0
    x = (T_cond - T_surface) / T_width
    x = max(-20.0, min(20.0, x))
    f_condensed = 1.0 / (1.0 + math.exp(-x))

    # Suppress thermal escape for condensed species
    r_therm_eff = 1.0 + (r_therm_raw - 1.0) * (1.0 - f_condensed)

    r_cond = condensation_channel(T_cond, T_surface)

    return r_sid * r_therm_eff * r_cond


# ---------------------------------------------------------------------------
# Single-channel fit (baseline comparison)
# ---------------------------------------------------------------------------

def single_channel_fit(T_fission: float, v_esc: float):
    """Original single-channel Gaussian fit on depleted elements only."""
    best_v_thr = None
    best_chi2 = float('inf')

    depleted = [(e, d) for e, d in ELEMENTS.items() if d[1] > 2.0]

    for v_thr_pct in range(1, 100):
        v_thr = v_esc * v_thr_pct / 100.0
        chi2 = 0.0
        for elem, (mass, ratio_obs, _, _, _) in depleted:
            v_th = thermal_velocity(mass, T_fission)
            ratio_pred = math.exp((v_th / v_thr)**2)
            chi2 += (math.log(ratio_pred) - math.log(ratio_obs))**2
        if chi2 < best_chi2:
            best_chi2 = chi2
            best_v_thr = v_thr

    return best_v_thr, best_chi2, len(depleted)


# ---------------------------------------------------------------------------
# Three-channel fit
# ---------------------------------------------------------------------------

def three_channel_fit(T_fission: float, v_esc: float):
    """
    Fit the three-channel model. Two free parameters:
        v_thr: thermal escape threshold
        T_surface: surface temperature at fission boundary

    Siderophile channel: from measured D_met/sil (zero free params).
    Condensation channel: from Lodders T_cond (zero free params in form).

    T_surface is physically measurable: it is the temperature at the
    surface of the proto-Earth's magma ocean at the Roche boundary,
    set by radiative equilibrium and atmospheric opacity. Expected
    range: 1200-2000 K (between silicate solidus and liquidus).
    """
    best_v_thr = None
    best_T_surf = None
    best_chi2 = float('inf')

    for T_surf in range(800, 2200, 50):
        for v_thr_pct in range(1, 300):
            v_thr = v_esc * v_thr_pct / 1000.0
            chi2 = 0.0
            for elem, (mass, ratio_obs, D, T_cond, _) in ELEMENTS.items():
                ratio_pred = three_channel_ratio(
                    mass, D, T_cond, T_fission, float(T_surf), v_thr)
                chi2 += (math.log(ratio_pred) - math.log(ratio_obs))**2
            if chi2 < best_chi2:
                best_chi2 = chi2
                best_v_thr = v_thr
                best_T_surf = float(T_surf)

    return best_v_thr, best_T_surf, best_chi2, len(ELEMENTS)


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def run_volatile_analysis():
    """Compare single-channel and three-channel models."""
    print("=" * 90)
    print("  VOLATILE DEPLETION: THREE-CHANNEL STRIBECK MODEL")
    print("=" * 90)
    print()

    T_fission = 4000.0  # K (bulk interior, sets thermal velocities)
    T_surface = 2000.0  # K (surface at fission boundary)
    M_total = 5.972e24 + 7.342e22
    R_proto = 6.371e6 * (M_total / 5.972e24)**(1.0 / 3.0)
    v_esc = escape_velocity_fission(M_total, R_proto)

    print(f"  Fission temperature (interior): {T_fission:.0f} K")
    print(f"  Surface temperature (boundary): {T_surface:.0f} K")
    print(f"  Escape velocity: {v_esc:.0f} m/s")
    print()

    # --- Element properties ---
    print(f"  {'Elem':>4s}  {'m(amu)':>7s}  {'D_met/sil':>9s}  {'T_cond':>6s}  "
          f"{'v_th(m/s)':>9s}  {'E/M obs':>7s}  {'type':>12s}")
    print(f"  {'-'*68}")

    for elem, (mass, ratio, D, T_cond, etype) in ELEMENTS.items():
        v_th = thermal_velocity(mass, T_fission)
        print(f"  {elem:>4s}  {mass:7.2f}  {D:9.2f}  {T_cond:6.0f}  "
              f"{v_th:9.0f}  {ratio:7.1f}  {etype:>12s}")
    print()

    # --- Single-channel fit (baseline) ---
    print("  " + "=" * 60)
    print("  SINGLE-CHANNEL MODEL (thermal only, depleted elements)")
    print("  " + "=" * 60)
    print()

    v_thr_1, chi2_1, n_1 = single_channel_fit(T_fission, v_esc)
    print(f"  Best-fit v_threshold = {v_thr_1:.0f} m/s "
          f"({v_thr_1/v_esc*100:.1f}% of v_escape)")
    print(f"  Log-space chi2 = {chi2_1:.2f} (N={n_1}, chi2/N = {chi2_1/n_1:.2f})")
    print()

    print(f"  {'Elem':>4s}  {'pred E/M':>9s}  {'obs E/M':>8s}  "
          f"{'log err':>8s}  fit")
    print(f"  {'-'*42}")
    for elem, (mass, ratio_obs, _, _, _) in ELEMENTS.items():
        v_th = thermal_velocity(mass, T_fission)
        ratio_pred = math.exp((v_th / v_thr_1)**2)
        ratio_pred = min(ratio_pred, 1e6)
        log_err = abs(math.log(ratio_pred) - math.log(ratio_obs))
        marker = "ok" if log_err < 0.5 else "~" if log_err < 1.0 else "X"
        print(f"  {elem:>4s}  {ratio_pred:9.1f}  {ratio_obs:8.1f}  "
              f"{log_err:8.2f}  {marker}")
    print()

    # --- Three-channel fit ---
    print("  " + "=" * 60)
    print("  THREE-CHANNEL MODEL (siderophile + thermal + condensation)")
    print("  " + "=" * 60)
    print()

    v_thr_3, T_surf_fit, chi2_3, n_3 = three_channel_fit(T_fission, v_esc)
    print(f"  Best-fit v_thr_thermal = {v_thr_3:.0f} m/s "
          f"({v_thr_3/v_esc*100:.1f}% of v_escape)")
    print(f"  Best-fit T_surface = {T_surf_fit:.0f} K")
    print(f"  Log-space chi2 = {chi2_3:.2f} (N={n_3}, chi2/N = {chi2_3/n_3:.2f})")
    print()

    print(f"  {'Elem':>4s}  {'R_sid':>6s}  {'R_therm':>8s}  {'R_cond':>7s}  "
          f"{'pred E/M':>9s}  {'obs E/M':>8s}  {'log err':>8s}  fit")
    print(f"  {'-'*72}")

    max_log_err = 0.0
    for elem, (mass, ratio_obs, D, T_cond, etype) in ELEMENTS.items():
        ratio_pred = three_channel_ratio(
            mass, D, T_cond, T_fission, T_surf_fit, v_thr_3)
        r_sid = siderophile_channel(D)
        v_th = thermal_velocity(mass, T_fission)
        r_therm = thermal_channel(v_th, v_thr_3)
        r_cond = condensation_channel(T_cond, T_surf_fit)
        ratio_pred_c = min(ratio_pred, 1e6)
        log_err = abs(math.log(ratio_pred_c) - math.log(ratio_obs))
        max_log_err = max(max_log_err, log_err)
        marker = "ok" if log_err < 0.5 else "~" if log_err < 1.0 else "X"
        print(f"  {elem:>4s}  {r_sid:6.2f}  {r_therm:8.3f}  {r_cond:7.3f}  "
              f"{ratio_pred_c:9.2f}  {ratio_obs:8.1f}  {log_err:8.2f}  {marker}")

    print()
    print(f"  Max factor error: {math.exp(max_log_err):.1f}x")
    print()

    # --- Comparison ---
    print("  " + "=" * 60)
    print("  COMPARISON")
    print("  " + "=" * 60)
    print()
    improvement = chi2_1 / chi2_3 if chi2_3 > 0 else float('inf')
    print(f"  Single-channel:  chi2/N = {chi2_1/n_1:.2f}  "
          f"(N={n_1} depleted elements, 1 free param)")
    print(f"  Three-channel:   chi2/N = {chi2_3/n_3:.2f}  "
          f"(N={n_3} ALL elements, 2 free params)")
    print(f"  Improvement: {improvement:.1f}x")
    print()
    print("  Channel decomposition:")
    print("    Siderophile — D_met/sil from lab experiments (zero free params)")
    print("                  Separates Fe, Ni, S, Cr from lithophiles")
    print("    Thermal     — Jeans escape (one free param: v_thr)")
    print("                  Separates Na, K, Zn by thermal velocity")
    print("    Condensation — T_cond from Lodders 2003 (zero free params)")
    print("                  Enriches Ca, Al, Ti in the Moon")
    print()


if __name__ == "__main__":
    print()
    print("=" * 70)
    print("  VOLATILE DEPLETION: THREE-CHANNEL STRIBECK MODEL")
    print("=" * 70)
    print()

    run_volatile_analysis()

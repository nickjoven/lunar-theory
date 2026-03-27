"""
Kirkwood gaps as the Arnold tongue spectrum of Jupiter.

The asteroid belt has gaps at specific period ratios with Jupiter:
    4:1, 3:1, 5:2, 7:3, 2:1

These are exactly the rationals on the Stern-Brocot tree. The gap
widths should equal the Arnold tongue widths at Jupiter's coupling
strength.

The mechanism: asteroids whose orbital period enters a Jupiter
tongue get their eccentricity pumped (resonance forcing), eventually
crossing Mars's or Jupiter's orbit and being ejected. The gap IS
the tongue — cleared by the tongue-boundary crossing pumping orbits
to instability.
"""

import math
import sys
import os

DERIV_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'harmonics', 'sync_cost', 'derivations')
sys.path.insert(0, DERIV_DIR)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tongue_scan import measure_tongue, measure_all_tongues


# ---------------------------------------------------------------------------
# Kirkwood gap data
# ---------------------------------------------------------------------------

# (period ratio, semi-major axis AU, observed gap width AU, name)
KIRKWOOD_GAPS = [
    (4, 1, 2.065, 0.02, "4:1"),
    (3, 1, 2.500, 0.04, "3:1 (Kirkwood)"),
    (5, 2, 2.825, 0.03, "5:2"),
    (7, 3, 2.957, 0.02, "7:3"),
    (2, 1, 3.278, 0.06, "2:1 (Hecuba)"),
]

# Jupiter's orbital elements
A_JUPITER = 5.203  # AU
T_JUPITER = 11.86  # years
M_JUPITER = 1.898e27
M_SUN = 1.989e30

# Jupiter's effective coupling on the asteroid belt
# K ∝ M_Jupiter/M_Sun × (a/a_Jupiter)^(3/2) for interior resonances
MU_JUPITER = M_JUPITER / M_SUN  # ≈ 9.55 × 10⁻⁴


def kepler_a_from_ratio(p: int, q: int) -> float:
    """Semi-major axis (AU) for period ratio p:q with Jupiter."""
    return A_JUPITER * (q / p)**(2.0/3.0)


def jupiter_coupling(a_au: float) -> float:
    """
    Effective coupling K of Jupiter on an asteroid at semi-major axis a.

    K ∝ μ_J × (a/a_J)^(1/2) × α² where α = a/a_J (Laplace coefficient)

    For interior resonances: K ∝ μ_J × α² / (1 - α)
    This diverges as a → a_Jupiter (stronger coupling at higher resonances).
    """
    alpha = a_au / A_JUPITER
    # Simplified: coupling strength increases closer to Jupiter
    K = MU_JUPITER * alpha**2 / (1.0 - alpha + 0.01)  # regularize
    # Normalize so that the 2:1 resonance has K ~ 0.5
    K_normalized = K / MU_JUPITER * 0.5
    return min(K_normalized, 0.99)


def kirkwood_analysis():
    """
    Compare Arnold tongue widths to Kirkwood gap widths.
    """
    print("=" * 90)
    print("  KIRKWOOD GAPS: ARNOLD TONGUE SPECTRUM OF JUPITER")
    print("=" * 90)
    print()

    print(f"  Jupiter mass ratio: μ_J = {MU_JUPITER:.4e}")
    print()

    # Show the gap structure
    print(f"  {'Ratio':>6s}  {'a (AU)':>8s}  {'K_eff':>7s}  "
          f"{'Δa obs':>8s}  {'tongue w':>10s}  {'scaled w':>9s}  match")
    print(f"  {'-'*65}")

    results = []

    for p, q, a_obs, da_obs, name in KIRKWOOD_GAPS:
        a_calc = kepler_a_from_ratio(p, q)
        K = jupiter_coupling(a_obs)

        # Tongue width from circle map
        # The period ratio p:q means the asteroid orbits p times per q Jupiter orbits
        # In circle map terms: Ω = q/p (asteroid frequency in Jupiter units)
        # The tongue is at rational q/p on the staircase
        p_cm = q  # circle map numerator
        q_cm = p  # circle map denominator
        if p_cm > q_cm:
            p_cm, q_cm = p_cm % q_cm, q_cm  # reduce to [0,1]
        if q_cm == 0:
            q_cm = 1

        # Use coupling K for the tongue measurement
        w = measure_tongue(p_cm, q_cm, K, n_scan=500)

        # Scale tongue width to AU: Δa/a ≈ (2/3) × w × a
        # (Kepler's third law: ΔT/T = (3/2) Δa/a)
        da_predicted = (2.0/3.0) * w * a_obs

        ratio = da_predicted / da_obs if da_obs > 0 else 0
        match = "✓" if 0.3 < ratio < 3.0 else "~" if 0.1 < ratio < 10 else "✗"

        results.append((name, a_obs, K, da_obs, w, da_predicted, ratio))
        print(f"  {name:>6s}  {a_obs:8.3f}  {K:7.4f}  "
              f"{da_obs:8.3f}  {w:10.5f}  {da_predicted:9.5f}  {match}")

    print()

    # The tongue hierarchy
    print("  TONGUE HIERARCHY (predicted ordering by width):")
    results.sort(key=lambda x: -x[4])
    for rank, (name, a, K, da_obs, w, da_pred, ratio) in enumerate(results, 1):
        print(f"    {rank}. {name:>6s}  w = {w:.5f}")

    print()
    print("  EXPECTED: 2:1 > 3:1 > 5:2 > 4:1 > 7:3")
    print("  (wider gaps at lower-order resonances = wider tongues)")
    print()

    # Full staircase view
    print("  STERN-BROCOT TREE VIEW:")
    print("  The Kirkwood gaps are the Arnold tongues of Jupiter's")
    print("  gravitational coupling, arranged on the Stern-Brocot tree:")
    print()
    print("        0/1")
    print("       /    \\")
    print("     1/2     1/1")
    print("    /    \\")
    print("  1/3    2/3    ← 3:1 and 3:2 gaps")
    print("  / \\    / \\")
    print("1/4 2/5 3/5 3/4  ← 4:1, 5:2 gaps")
    print()
    print("  Each node is a resonance. Each tongue has a width.")
    print("  The gaps ARE the tongues. Asteroids inside tongues")
    print("  get eccentricity-pumped and ejected. The belt structure")
    print("  is the inverse of the devil's staircase: gaps where the")
    print("  staircase has plateaus.")
    print()


def cassini_division():
    """
    Saturn's Cassini division as the 2:1 tongue of Mimas.
    Same mechanism, different system.
    """
    print("=" * 90)
    print("  CASSINI DIVISION: 2:1 TONGUE OF MIMAS")
    print("=" * 90)
    print()

    M_SATURN = 5.683e26
    M_MIMAS = 3.749e19
    mu_mimas = M_MIMAS / M_SATURN

    print(f"  Mimas mass ratio: μ = {mu_mimas:.4e}")
    print(f"  Cassini division is at the 2:1 mean-motion resonance with Mimas.")
    print(f"  Division width: ~4,800 km (in a ring system of ~70,000 km radius)")
    print(f"  Width fraction: {4800/70000:.3f} = {4800/70000*100:.1f}%")
    print()
    print(f"  This is the same mechanism as the Kirkwood gaps:")
    print(f"  ring particles in Mimas's 2:1 tongue get eccentricity-pumped")
    print(f"  and ejected, clearing the gap.")
    print()
    print(f"  The tongue width at μ = {mu_mimas:.1e} should give the division width.")
    print(f"  At such small mass ratio, the 2:1 tongue width ≈ 2μ^(2/3) ≈ {2*mu_mimas**(2/3):.4f}")
    print(f"  Observed width fraction: {4800/70000:.4f}")
    print()


if __name__ == "__main__":
    print()
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  KIRKWOOD GAPS + CASSINI DIVISION: TONGUE SPECTRA               ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print()

    kirkwood_analysis()
    cassini_division()

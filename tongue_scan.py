"""
Direct tongue width measurement by scanning the devil's staircase.

The tongue_boundary bisection in circle_map.py returns near-zero widths
due to numerical issues. This module measures widths directly by scanning
Ω and detecting where the winding number locks to each rational.
"""

import math
import sys
import os

DERIV_DIR = os.path.join(os.path.dirname(__file__), '..', 'harmonics', 'sync_cost', 'derivations')
sys.path.insert(0, DERIV_DIR)

from circle_map import winding_number


def measure_tongue(p: int, q: int, K: float,
                   n_scan: int = 500, tol: float = 0.002) -> float:
    """
    Measure Arnold tongue width by scanning Ω ∈ [0,1].

    Scans n_scan points and finds the range of Ω where the
    winding number W(Ω) matches p/q within tolerance.
    """
    target = p / q
    lo, hi = None, None
    for i in range(n_scan + 1):
        omega = i / n_scan
        W = winding_number(omega, K)
        if abs(W - target) < tol:
            if lo is None:
                lo = omega
            hi = omega
    if lo is not None and hi is not None:
        return hi - lo
    return 0.0


def measure_all_tongues(K: float, q_max: int = 8,
                        n_scan: int = 500) -> list:
    """
    Measure all tongue widths for rationals with denominator ≤ q_max.
    Returns list of (p, q, value, width) sorted by width descending.
    """
    tongues = []
    for q in range(1, q_max + 1):
        for p in range(0, q + 1):
            if math.gcd(p, q) != 1:
                continue
            val = p / q
            if val > 1.0:
                continue
            w = measure_tongue(p, q, K, n_scan=n_scan)
            tongues.append((p, q, val, w))
    tongues.sort(key=lambda x: -x[3])
    return tongues


def total_locked_fraction(K: float, q_max: int = 8,
                          n_scan: int = 500) -> float:
    """Total fraction of frequency space covered by tongues."""
    tongues = measure_all_tongues(K, q_max, n_scan)
    return sum(t[3] for t in tongues)


if __name__ == "__main__":
    print("Tongue width measurements:")
    for K in [0.3, 0.5, 0.7, 0.8, 0.9, 1.0]:
        tongues = measure_all_tongues(K, q_max=6, n_scan=400)
        total = sum(t[3] for t in tongues)
        print(f"\nK = {K:.1f}  (total locked: {total*100:.1f}%)")
        for p, q, val, w in tongues[:8]:
            if w > 0:
                print(f"  {p}/{q}  w={w:.4f}")

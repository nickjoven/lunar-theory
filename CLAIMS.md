# Predictions and Falsification Criteria

Every prediction is one instance of the same mechanism: an oscillation
reaching an Arnold tongue boundary and entering the lower-cost locked
regime. The framework inputs are the four primitives (Z, mediant, fixed
point, parabola), the circle map, and physical constants (G, M, R) for
dimensional mapping.

Organized by epoch.

## ~4.5 Gya: Fission

The l=2 bar-mode deformation enters the 1/2 Arnold tongue.

| # | Claim | Prediction | Observed | Residual | Falsification |
|---|-------|-----------|----------|----------|---------------|
| 1 | Fission at 1/2 tongue boundary | T = 3.96 hr at K_crit = 0.45 | Impact models require 4–5 hr | 12% | Jacobi bifurcation cannot produce Moon-mass daughter at Earth density |
| 2 | Isotopic identity forced | Same pre-fission state → identical ratios | O, Ti, W, Cr, Si identical to ppm | 0 | A refractory isotope differs between Earth and Moon at >5σ |
| 3 | Angular momentum from I × ω_crit | L = 1.05 × L_obs | L = 3.44 × 10³⁴ kg m²/s | 5% | Tongue width gives L off by >20% |
| 4 | Mass ratio from tongue population | N(1/2) = 1.6% (raw), 2.7% (field eq.) | M_Moon/M_total = 1.21% | 32–120% | Tongue width at 1/2 excludes observed mass ratio at >3σ |
| 5 | One Moon from tongue competition | 1/2 captures mass → suppresses 1/3, 2/5 | One Moon | — | Multiple fragments stable in the field equation |

## ~4.5 Gya: Composition at the fission boundary

Each element crosses or does not cross its tongue boundary at fission.

| # | Claim | Prediction | Observed | Residual | Falsification |
|---|-------|-----------|----------|----------|---------------|
| 6 | Iron outside tongue at fission coupling | High-ω attenuates at boundary (lattice: 1900×) | Moon Fe ~2% vs Earth 32% (16×) | direction ✓ | A high-density element enriched in Moon vs Earth |
| 7 | Volatiles exit bound regime | exp(-(v_th/v_thr)²), v_thr = 8% v_esc | K: 15×, S: 38×, Na: 42× | K, S within 1.6× | A low-boiling-point element NOT depleted in Moon |
| 8 | Refractories inside tongue at all scales | Low density → low ω → propagates | Ca, Al enriched in Moon | direction ✓ | A low-density refractory depleted in Moon |
| 9 | KREEP from N=2 passthrough vs N=3 conversion | Near side inside fundamental tongue | KREEP on near side | direction ✓ | KREEP uncorrelated with tidal coupling geometry |

## ~4.5 Gya: Post-fission tongue crossings

Three boundary crossings in rapid succession after fission.

| # | Claim | Prediction | Observed | Residual | Falsification |
|---|-------|-----------|----------|----------|---------------|
| 10 | Post-Roche: spin above 1:1 tongue | Ω = 1.4 → outward torque | Moon exists | — | Ω < 1 at fission distance (inward torque) |
| 11 | Tidal locking: spin enters 1:1 tongue | 0/1 tongue widest (0.126 at K=0.8) | Moon is locked 1:1 | — | A wider tongue exists for a different resonance |
| 12 | Inclination from Cassini bifurcation | Nodal precession crosses solar tongue at 4–5 R_E | i = 5.145° = 22% of Earth's obliquity | — | Inclination requires formation geometry, not tidal dynamics |

## 4.5 Gya → present: Recession through the staircase

Ω sweeps from ~1.5 to ~27, entering and exiting every Arnold tongue on
the Stern-Brocot tree. Each entry stalls the recession.

| # | Claim | Prediction | Observed | Residual | Falsification |
|---|-------|-----------|----------|----------|---------------|
| 13 | Staircase extends recession | Lock-stall-unlock at each rational | Moon age: 4.5 Gyr | bounded [1.65, 8.42] Gyr | Self-consistent bounds exclude 4.5 Gyr |
| 14 | Q ≈ 40 is non-resonant baseline | Stribeck fit determines intrinsic Q | Q(current) ≈ 12 (anomalous) | Q fit: χ²/N = 0.81 | Stribeck baseline Q inconsistent with recession bounds |
| 15 | Current Q = 12 from ocean resonance | Ocean basin frequency inside tidal tongue | Q dropped ~200 Myr ago | — | Ocean resonance cannot produce 3× Q reduction |
| 16 | Evection = one staircase crossing | Perigee precession tongue at 30–35 R_E | Debated for synestia | — | Fission L budget requires evection L removal |

## Present: Tongue-boundary signatures

Two observables of the current tongue geometry.

| # | Claim | Prediction | Observed | Residual | Falsification |
|---|-------|-----------|----------|----------|---------------|
| 17 | Tidal Q from one Stribeck curve | Stick/slip threshold at v_thr = 10⁻⁷ m/s | Q: 38–200 across periods | χ²/N = 0.81 | Q at any period off by >3σ from curve |
| 18 | Librations = 1:1 tongue boundary riding | Equilibrium stick-slip oscillation at edge | 1.5" longitude, 8.2" wobble | mechanism ✓ | Librations require external excitation with measured energy |

## Self-consistency

The Q fit (claim 17) determines the Stribeck parameters. Those parameters
determine Q(a) at every orbital distance. Q(a) determines K(a), which
determines the local staircase locked fraction. Integrating over the full
recession (claim 13) gives the timeline bounds.

This loop has **zero additional free parameters**. The Q-fit Stribeck
baseline (Q ≈ 40) gives 8.42 Gyr. The constant-Q anomaly (Q ≈ 12) gives
1.65 Gyr. The observed 4.5 Gyr falls between — consistent with Q ≈ 40
for most of history, Q ≈ 12 during the current ocean-resonance epoch
(claim 15).

The mass ratio residual (claim 4) is bounded by the bare-frequency
distribution g(1/2), which is constrained by the proto-Earth's moment of
inertia (C/MR² = 0.33). Reversing: g(1/2) = 0.012/0.016 = 0.76 is a
testable prediction against the l=2 normal-mode spectral weight of a
body with Earth's density profile.

## Known Residuals

The mass ratio (claim 4) is the largest residual. The raw tongue width
(1.6%) overshoots by 32%; the self-consistent field equation (2.7%)
overshoots by 120%. The scan resolution (n_scan=300) discretizes tongue
boundaries, and the uniform g(ω) assumption ignores the proto-Earth's
radial density structure. The inferred g(1/2) = 0.76 is independently
checkable.

The volatile model (claim 7) fits the thermal escape channel (K, S, Ga
within 1.6×) but cannot distinguish it from density sorting (siderophiles)
or condensation retention (refractories) in a single Gaussian. These are
three tongue-boundary crossings at three different velocity scales — each
Stribeck in structure, each requiring its own v_thr. The thermal channel's
v_thr/v_esc = 0.08 matches the Jeans escape criterion (λ_crit ≈ 10,
v_thr/v_esc ≈ 0.1).

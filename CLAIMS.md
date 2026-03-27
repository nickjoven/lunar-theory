# Predictions and Falsification Criteria

Predictions from the synchronization cost framework applied to the
Earth-Moon system. The framework inputs are the four primitives
(Z, mediant, fixed point, parabola) and the circle map. Physical
constants (G, M_Earth, R_Earth) enter only for dimensional mapping.

## Origin

| # | Claim | Prediction | Observed | Residual | Falsification |
|---|-------|-----------|----------|----------|---------------|
| O1 | Fission at saddle-node bifurcation | T_fission = 3.96 hr (1/2 tongue at K=0.45) | Impact models require 4–5 hr | 12% | Show Jacobi bifurcation cannot produce Moon-mass daughter at Earth density |
| O2 | Isotopic identity forced | Both bodies from same pre-fission state → identical ratios | O, Ti, W, Cr, Si identical to ppm | 0 | Find a refractory isotope that differs between Earth and Moon at >5σ |
| O3 | Angular momentum from I × ω_crit | L_proto = 1.05 × L_obs | L = 3.44 × 10³⁴ kg m²/s | 5% | Tongue width calculation gives L off by >20% |
| O4 | Mass ratio from tongue population | N(1/2) = 1.6% (raw) / 2.7% (self-consistent) | M_Moon/M_total = 1.21% | 32%–120% | Measured tongue width at 1/2 excludes observed mass ratio at >3σ |
| O5 | One Moon from tongue competition | 1/2 tongue dominates; captures mass → suppresses 1/3, 2/5 | One Moon | — | Show multiple fragments are stable post-fission in the field equation |
| O6 | Inclination from Cassini bifurcation | Cassini state transition at 4–5 R_E pumps i = ε × sin(η) | i = 5.145° = 22% of ε | — | Show inclination requires formation mechanism, not post-formation dynamics |
| O7 | Post-Roche survival | Ω = 1.4 at fission → outward tidal torque | Moon exists | — | Show Ω < 1 at fission distance (inward torque → disruption) |

## Composition

| # | Claim | Prediction | Observed | Residual | Falsification |
|---|-------|-----------|----------|----------|---------------|
| C1 | Iron depletion from frequency filtering | High-ω modes attenuate at fission boundary (lattice: 1900×) | Moon Fe ~2% vs Earth 32% (16×) | direction ✓ | Find a high-density element enriched in Moon relative to Earth |
| C2 | Volatile depletion from thermal Stribeck | exp(-(v_th/v_thr)²) with v_thr = 8% of v_escape | K: 15×, S: 38×, Na: 42× | K, S within 1.6× | Find a low-boiling-point element NOT depleted in the Moon |
| C3 | Refractory enrichment = low-density propagation | Low-density phases propagate to daughter body | Ca, Al enriched in Moon | direction ✓ | Find a low-density refractory depleted in the Moon |
| C4 | KREEP near-side from N=2 passthrough | N=2 tidal coupling delays near-side solidification | KREEP concentrated on near side | direction ✓ | Show KREEP distribution uncorrelated with tidal heating geometry |

## History

| # | Claim | Prediction | Observed | Residual | Falsification |
|---|-------|-----------|----------|----------|---------------|
| H1 | Recession via devil's staircase | Resonance trapping extends timeline: 2.13× at K=1.0, q≤8 | Moon age: 4.5 Gyr | 3.51 vs 4.5 Gyr | Full staircase (q→∞) at physical K gives age <3 Gyr or >6 Gyr |
| H2 | Stribeck suppresses early recession | Velocity-dependent friction: 5–16× slower at close approach | Constant-Q gives 1.65 Gyr (paradox) | 1.92 Gyr | Find geological evidence that early recession was FASTER than today |
| H3 | Evection = staircase crossing | Perigee precession resonance at 30–35 R_E; no L removal needed | Evection resonance debated for synestia | — | Show fission L budget requires evection L removal |

## Behavior

| # | Claim | Prediction | Observed | Residual | Falsification |
|---|-------|-----------|----------|----------|---------------|
| B1 | Tidal Q from one Stribeck curve | μ_s/μ_k=5, v_thr=10⁻⁷ m/s, Q_scale=40 | Q: 38 (semidiurnal) to 200 (nodal) | χ²/N = 0.81 | Published Q at any period off by >3σ from fit |
| B2 | Free librations = tongue boundary riding | Equilibrium oscillation at Arnold tongue edge | Longitude: 1.5", wobble: 8.2" | mechanism ✓ | Show librations require external excitation with measured energy input |
| B3 | Variable Q is velocity-dependent friction | Stick (long period) → high Q; slip (short period) → low Q | Semidiurnal Q~38, nodal Q~200 | trend ✓ | Find a period where Q violates the monotonic Stribeck trend |

## Known Residuals

The mass ratio (O4) is the largest open residual: raw tongue width gives
1.3× the observed value, self-consistent field equation gives 2.2×. This
likely reflects scan resolution (n_scan=300 discretizes tongue boundaries)
and the uniform bare-frequency assumption (g = const). The field equation's
self-consistency narrows tongues relative to raw measurement, but the
fixed point overshoots. Higher scan resolution and a physically motivated
g(ω) are the next steps.

The recession timeline (H1) at 3.51 Gyr (q≤8) falls 22% short of
4.5 Gyr. Each increase in q_max adds stalling time from newly resolved
resonances. The progression q≤4 → q≤6 → q≤8 adds 1–3% locked fraction
per step. The full staircase (q→∞) at K=1.0 covers 100% of frequency
space; the 4.5 Gyr target sits at moderate q_max with physical K.

The volatile model (C2) fits volatiles proper (K, S, Ga within 1.6×) but
the Gaussian thermal envelope cannot distinguish volatile escape from
siderophile sinking or refractory retention. These are three distinct
depletion mechanisms — each Stribeck in character, but operating at
different scales (thermal velocity, density oscillation, condensation
temperature). A multi-channel model is identified but not yet computed.

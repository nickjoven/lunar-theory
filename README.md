# lunar-theory

The Moon's origin, composition, history, and behavior derived from
synchronization cost physics — the same framework that produces the
spectral tilt (n_s ≈ 0.965), the Born rule, and general relativity
from four irreducible primitives.

## The Problem

The giant impact hypothesis has one fatal flaw: simulations predict a
moon made of 70%+ foreign impactor material, but lunar samples are
isotopically identical to Earth — oxygen, titanium, tungsten, chromium,
silicon — to parts per million. Every proposed fix trades one problem
for another:

- **Synestia**: homogenizes isotopes but requires 2× the observed angular
  momentum, needing debatable evection resonance to remove it.
- **Multiple impacts**: more mixing but scattering prevents accretion.
- **Same-neighborhood Theia**: requires Venus samples to test; considered
  unlikely by most researchers.

## The Framework

Four primitives — integers, mediants, fixed points, parabolas — operating
on the Stern-Brocot tree produce a self-consistent field equation whose
solutions include the circle map, the devil's staircase, and Arnold
tongues. Applied to the Earth-Moon system, this framework resolves
thirteen lunar puzzles.

**Depends on**: [harmonics](https://github.com/nickjoven/harmonics)
(synchronization cost framework, Stribeck lattice, circle map machinery).

## Results

### Origin (`origin/`)

The Moon formed by **saddle-node bifurcation** of the proto-Earth's l=2
bar-mode deformation, not by giant impact.

| Quantity | Predicted | Observed | Module |
|---|---|---|---|
| Critical rotation period | 3.96 hours | 4–5 hours (impact models) | `bifurcation_fission.py` |
| Angular momentum | 1.05 × L_obs | L = 3.44 × 10³⁴ kg m²/s | `bifurcation_fission.py` |
| Mass ratio (tongue width) | 1.6% | 1.21% (M_Moon/M_total) | `bifurcation_fission.py` |
| Mass ratio (field equation) | 2.7% | 1.21% | `field_equation.py` |
| Isotopic identity | Forced (same pre-fission state) | Identical to ppm | — |
| One Moon, not fragments | 1/2 tongue dominates; competition suppresses 1/3, 2/5 | One Moon | `field_equation.py` |

The 1/2 Arnold tongue on the Stern-Brocot tree captures ~1.5% of
frequency space at K_crit = 0.45, matching the Moon's mass fraction.
The saddle-node bifurcation (parabola primitive) at the tongue boundary
creates two fixed points — one becomes the Moon. Both bodies inherit
the same pre-bifurcation isotopic state. No foreign material.

### Composition (`composition/`)

Iron depletion, volatile loss, and near/far-side asymmetry from
**Stribeck frequency filtering** and the N=2 → N=3 lattice transition.

| Quantity | Mechanism | Observed | Module |
|---|---|---|---|
| Iron depletion (16×) | High-frequency modes attenuate at fission boundary | Moon Fe ~2% vs Earth 32% | `iron_depletion.py` |
| Volatile depletion (K, S) | Thermal Stribeck stripping: exp(-(v_th/v_thr)²) | K: 15×, S: 38× | `volatile_ratios.py` |
| KREEP near-side concentration | N=2 passthrough (near side) vs N=3 conversion (far side) | KREEP on near side | `iron_depletion.py` |
| Refractory enrichment (Ca, Al) | Low density → low ω → propagates to daughter | Ca, Al enriched in Moon | `iron_depletion.py` |

The Stribeck lattice spatial spectrum (harmonics/RESULTS.md) shows
high-frequency modes attenuating by 1900× at the first frictional
contact while subharmonics propagate with negligible loss. This maps
directly onto the Moon's compositional fractionation.

Volatile depletion ratios fit a Stribeck Gaussian envelope for volatiles
proper (K, S, Ga within a factor of 1.6), but the single-channel thermal
model cannot distinguish volatile escape from siderophile sinking or
refractory retention. These are three distinct physical mechanisms sharing
the Stribeck structure at different scales.

### History (`history/`)

The recession rate paradox dissolves: the Moon's orbital evolution is a
trajectory on the **devil's staircase**, with resonance trapping at
every rational frequency ratio extending the timeline.

| Quantity | Predicted | Observed | Module |
|---|---|---|---|
| Recession timeline (K=1.0, q≤8) | 3.51 Gyr | 4.5 Gyr | `recession_hires.py` |
| Extension from staircase (K=1.0) | 2.13× | — | `recession_hires.py` |
| Stribeck rate suppression at 10 R_E | 16× slower than constant-Q | — | `tidal_stribeck.py` |
| Evection resonance | Staircase crossing at ~30-35 R_E; no L removal needed | Debated in synestia model | `recession_hires.py` |

The constant-Q model gives 1.65 Gyr — the classic recession paradox.
The devil's staircase at K=1.0 with q≤8 extends this to 3.51 Gyr.
Each increase in q_max (more resonances resolved) adds stalling time.
The true staircase (q_max → ∞) at K=1.0 has 100% locked fraction. The
4.5 Gyr target is reachable with the full resonance spectrum.

The Stribeck tidal friction model independently shows velocity-dependent
dissipation suppresses early recession rates by 5–16× at close approach,
providing a complementary mechanism.

### Behavior (`behavior/`)

Tidal Q, free librations, orbital inclination, and post-fission survival
from **Arnold tongue geometry** and **Cassini state bifurcations**.

| Quantity | Predicted | Observed | Module |
|---|---|---|---|
| Tidal Q (χ²/N = 0.81, 3 params) | Single Stribeck curve | Q: 38–200 across periods | `tidal_q_stribeck.py` |
| Free librations | Tongue boundary riding (no excitation source needed) | 1.5" longitude, 8.2" wobble | `libration_tongue_edge.py` |
| Orbital inclination | 5.14° from Cassini state bifurcation at 4–5 R_E | 5.145° | `cassini_inclination.py` |
| Post-Roche survival | Ω = 1.4 at fission → outward torque, no disruption | Moon exists | `cassini_inclination.py` |

The tidal Q result is the strongest quantitative prediction: one
Stribeck friction curve with 3 parameters (μ_s/μ_k = 5, v_thr = 10⁻⁷
m/s, Q_scale = 40) fits all published period-dependent lunar Q
measurements with χ²/N = 0.81 — competitive with 5-parameter
rheological models.

The 5.14° orbital inclination, historically considered fatal to fission
models, is the natural output of the Cassini state bifurcation that every
tidally evolving satellite passes through at 4–5 R_E. The inclination is
set by the transition, not by the formation mechanism.

## Running

Requires `harmonics/` as a sibling directory. Python 3.10+, no external
packages.

```bash
# Origin
python3 origin/bifurcation_fission.py   # Tongue width → fission period, L, mass ratio
python3 origin/field_equation.py         # Self-consistent populations, tongue competition

# Composition
python3 composition/iron_depletion.py    # Lattice spectrum → fractionation + KREEP
python3 composition/volatile_ratios.py   # Thermal Stribeck → depletion ratios

# History
python3 history/tidal_stribeck.py        # Stribeck recession rate table
python3 history/recession_hires.py       # Devil's staircase extension + LHB + evection

# Behavior
python3 behavior/tidal_q_stribeck.py     # One curve fits all Q measurements
python3 behavior/libration_tongue_edge.py # Arnold tongue boundary simulation
python3 behavior/cassini_inclination.py  # Inclination pump + post-Roche survival
```

## Predictions

See [CLAIMS.md](CLAIMS.md) for numbered predictions with falsification
criteria and current residuals.

## License

CC0 1.0 Universal — public domain.

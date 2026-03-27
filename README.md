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

## One Mechanism

Every lunar phenomenon in this repository is one thing: **an oscillation
reaching an Arnold tongue boundary and entering the lower-cost locked
regime**. The Stribeck friction curve, the devil's staircase, saddle-node
bifurcations, and resonance trapping are not separate mechanisms — they
are the same transition (stick/slip, locked/unlocked, inside tongue/outside
tongue) seen at different scales and epochs.

The four primitives (Z, mediant, fixed point, parabola) on the Stern-Brocot
tree produce a self-consistent field equation. Its solutions are the circle
map and the Arnold tongue spectrum. Every claim below is a specific instance
of one oscillation crossing one tongue boundary.

**Depends on**: [harmonics](https://github.com/nickjoven/harmonics)
(synchronization cost framework, Stribeck lattice, circle map machinery).

## Epoch Sequence

The Earth-Moon system's history is a sequence of tongue-boundary crossings,
ordered by time. Each crossing is the same mechanism at a different scale.

### ~4.5 Gya: Fission

The proto-Earth's l=2 bar-mode deformation oscillation **enters the 1/2
Arnold tongue** as gravitational coupling increases during contraction.
At the tongue boundary, the saddle-node bifurcation (parabola primitive)
creates two fixed points. One becomes the Moon.

| Quantity | Predicted | Observed | Module |
|---|---|---|---|
| Critical rotation period | 3.96 hours | 4–5 hours | `origin/bifurcation_fission.py` |
| Angular momentum | 1.05 × L_obs | L = 3.44 × 10³⁴ kg m²/s | `origin/bifurcation_fission.py` |
| Mass ratio | 1.6% (tongue width) | 1.21% (M_Moon/M_total) | `origin/bifurcation_fission.py` |
| Isotopic identity | Forced | Identical to ppm | — |

Both bodies inherit the same pre-fission state. The 1/2 tongue dominates
because it is the widest non-fundamental tongue on the tree; when it
captures mass, it reduces the effective coupling, narrowing all smaller
tongues (1/3, 2/5, …). This is why there is one Moon, not fragments
(`origin/field_equation.py`).

### ~4.5 Gya: Composition set at the fission boundary

At the fission boundary, each element either crosses or does not cross
its relevant tongue boundary. Three scales, one structure:

- **Iron, nickel** (siderophile): dense material oscillates at high
  frequency. High-ω modes are **outside their Arnold tongues** at the
  fission coupling — they do not lock, do not propagate coherently, and
  attenuate at the first frictional contact (1900× in the lattice). Iron
  stays with the parent. Moon Fe: 2% vs Earth 32%.

- **Na, K, S, Zn** (volatile): thermal oscillation velocity exceeds the
  gravitational tongue boundary (Jeans escape parameter). These atoms
  **exit the bound regime** at fission temperature. Depletion scales as
  exp(-(v_thermal/v_threshold)²) — the Stribeck Gaussian at thermal scale.
  K, S, Ga fit within 1.6×. (`composition/volatile_ratios.py`)

- **Ca, Al, Ti** (refractory): low thermal velocity, low density. These
  modes **remain inside their tongues** at all relevant scales — they
  propagate to the daughter body and are enriched.

KREEP concentrates on the near side because the near-side tidal coupling
path (Earth → Moon surface, N=2) **stays inside the fundamental tongue**
(passthrough), while the far side (Earth → near-side → bulk → far-side,
N≥3) **crosses the frequency-conversion threshold** where the subharmonic
regime activates. (`composition/iron_depletion.py`)

### ~4.5 Gya: Post-fission dynamics

Three tongue-boundary crossings in rapid succession after fission:

1. **Post-Roche survival**: At fission (~3 R_E), the Earth's spin-orbit
   ratio Ω = 1.4 — the spin oscillation is **above the 1:1 tongue**,
   generating outward tidal torque. The Moon migrates past the Roche
   limit without disruption. (`behavior/cassini_inclination.py`)

2. **Tidal locking**: The Moon's spin **enters the 1:1 tongue** (the
   widest on the Stern-Brocot tree, width 0.126 at K=0.8). Locking is
   immediate and inevitable — it is the lowest-cost synchronization
   state. (`origin/bifurcation_fission.py`)

3. **Cassini state transition at 4–5 R_E**: The Moon's nodal precession
   rate **crosses a resonance with the solar orbital frequency**. This
   tongue-boundary crossing bifurcates the equilibrium spin-orbit geometry,
   pumping the orbital inclination from 0° to 5.14°. The inclination is
   set by the bifurcation, not by the formation mechanism.
   (`behavior/cassini_inclination.py`)

### 4.5 Gya → present: Recession via the devil's staircase

As tidal torque transfers angular momentum from Earth's spin to the Moon's
orbit, the spin-orbit ratio Ω sweeps from ~1.5 to ~27. This trajectory
crosses every rational frequency ratio on the Stern-Brocot tree.

At each rational p/q, the system **enters the corresponding Arnold tongue**
— it locks, stalls, and the recession pauses. The wider the tongue, the
longer the stall. The cumulative stalling time across all tongue crossings
extends the recession timeline.

| Model | Recession time | Mechanism |
|---|---|---|
| Constant-Q (Q=12 everywhere) | 1.65 Gyr | No tongue structure; too fast |
| Stribeck baseline (Q=40 everywhere) | 8.42 Gyr | Intrinsic Q from Stribeck fit; too slow |
| **Physical** (Q≈40 baseline, Q≈12 at ocean resonance) | **~4–5 Gyr** | **Staircase + epoch-dependent Q** |

The constant-Q model extrapolates today's anomalously low Q backward.
The Stribeck fit gives Q ≈ 40 as the natural (non-resonant) baseline.
The current Q ≈ 12 is itself a tongue-boundary crossing: the ocean
basins' natural frequency **entering a tidal resonance tongue**, amplifying
dissipation by ~3×. This ocean resonance epoch is geologically recent
(~200 Myr). Most of the 4.5 Gyr recession was at Q ≈ 40.

The self-consistent calculation (`history/self_consistent_recession.py`)
confirms: the Q-fit parameters bound the recession between 1.65 and
8.42 Gyr with zero additional free parameters. The observed 4.5 Gyr
falls inside these bounds.

The evection resonance (perigee precession entering the solar-frequency
tongue at ~30–35 R_E) is one of these crossings. The fission model does
not need it to remove angular momentum — it already has the right L.
(`history/recession_hires.py`)

### Present: Tidal Q and librations

Two signatures of the **current** tongue-boundary geometry:

- **Tidal Q varies by forcing period** because different periods drive
  tidal deformation at different velocities. Short-period forcing (high
  velocity) is **in the slip regime** (outside the stick tongue): more
  dissipation, Q ≈ 38. Long-period forcing (low velocity) is **in the
  stick regime** (inside the tongue): less dissipation, Q ≈ 200. One
  Stribeck curve, χ²/N = 0.81, 3 parameters. (`behavior/tidal_q_stribeck.py`)

- **Free librations** exist because the Moon sits **at the 1:1 tongue
  boundary**, not at its center. The boundary-riding oscillation between
  stick and slip micro-states IS the free libration. No excitation source
  is needed; no damping paradox exists. The 1.5" longitude libration and
  8.2" wobble are the equilibrium amplitude of this boundary oscillation.
  (`behavior/libration_tongue_edge.py`)

## Summary

Thirteen phenomena, one mechanism:

| Phenomenon | Oscillation | Tongue boundary | Regime entered |
|---|---|---|---|
| Fission | l=2 bar-mode | 1/2 tongue at K=0.45 | Locked → daughter body |
| Isotopic identity | — | Same pre-fission state | — |
| One Moon | 1/2 vs 1/3 tongues | Competition at field eq. fixed point | 1/2 dominates |
| Iron depletion | Density oscillation | Fission boundary | High-ω outside tongue → attenuated |
| Volatile depletion | Thermal velocity | Jeans escape threshold | Above threshold → escapes |
| Refractory enrichment | Low-ω mode | Inside tongue at all scales | Propagates to daughter |
| KREEP asymmetry | Tidal coupling path | N=2 → N=3 conversion threshold | Near side: passthrough; far side: converted |
| Post-Roche survival | Earth spin vs orbit | Above 1:1 tongue (Ω=1.4) | Outward torque |
| Cassini inclination | Nodal precession | Solar frequency resonance | Bifurcation → 5.14° |
| Recession | Ω sweep 1.5 → 27 | Every rational on Stern-Brocot tree | Lock-stall-unlock at each |
| Tidal Q | Tidal velocity | Stribeck stick/slip threshold | Short period: slip; long period: stick |
| Librations | Spin-orbit | 1:1 tongue edge | Boundary riding |
| Ocean resonance (Q=12) | Ocean basin frequency | Tidal resonance tongue | Currently inside → enhanced dissipation |

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
python3 history/self_consistent_recession.py  # Q fit → K(a) → staircase → timeline

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

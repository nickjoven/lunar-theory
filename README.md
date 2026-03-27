# lunar-theory

> *"We have three theories of the origin of the Moon, and none of them
> work. So the Moon must not exist."* — Irwin Shapiro, 1984 Hawaii
> conference

How did we end up with our big weird perfect Moon? This repository
takes the question seriously — not with a new story, but with a
framework that already produces the spectral tilt, the Born rule,
and general relativity from four primitives. Applied to the
Earth-Moon system, it resolves the fatal flaw of the giant impact
hypothesis and twelve other lunar puzzles, all as instances of one
mechanism.

## Why now?

Physics is missing a unifying model for systems that are simply translations of the same phenomenon. Discretely, this is no longer missing. [A theorem of subharmonics, nonlinear dynamics, and LOONA lore.](https://nickjoven.github.io/submediant-site/03_einstein/13_einstein_from_kuramoto.html#derivation-13-einstein-field-equations-from-the-rational-field-equation)

## The fatal flaw

The [video](https://youtu.be/ghW7BEC0byg) that prompted this work
identifies the problem clearly: Robin Canup's simulations show that
to get the right angular momentum, 70%+ of the Moon must come from
the impactor Theia, not from Earth. But Apollo samples — 382 kg of
them, measured and re-measured for fifty years — show the Moon and
Earth are isotopically identical to parts per million. Oxygen,
titanium, tungsten, chromium, silicon. Every new element tested
tightens the match.

If the physics demands a foreign moon and the chemistry demands an
identical one, something deeper is wrong.

The video walks through the attempted fixes:

- **Synestia** (vaporize everything, homogenize): solves isotopes
  but needs 2× the angular momentum. The proposed escape hatch —
  evection resonance removing L via the Sun — is, as the video's
  interviewee says, "less likely."

- **Multiple impacts** (more mixing): "more likely scenarios that
  you're going to scatter them and you're not going to grow enough."

- **Same-neighborhood Theia** (isotopically identical impactor):
  needs Venus samples to check. Nobody has those.

The video ends openly: "We might have a selection effect… it's worth
wondering if we're here in part because of our big weird Moon."

This repository offers a different ending.

## One mechanism

The fatal flaw dissolves if you question the substrate underneath
every simulation in the video. All of them — Canup's SPH, synestia,
multiple-impact — treat gravity as a static force between mass points
with constant-viscosity tidal friction. They have to, because they
don't have the tongue structure.

The tongue structure comes from coupled oscillators. When two
oscillators interact through a medium, they lock at rational frequency
ratios — 1:1, 1:2, 2:3, 3:5 — forming Arnold tongues in parameter
space. The set of all locked states is the devil's staircase. The
boundary of each tongue is a saddle-node bifurcation. The medium's
coupling is velocity-dependent (Stribeck friction: strong at low
relative velocity, weak at high).

These are not separate mechanisms. They are the same transition —
**an oscillation reaching a tongue boundary and entering the
lower-cost locked regime** — seen at different scales.

The framework that produces this structure uses four irreducible
primitives (integers, mediants, fixed points, parabolas) on the
Stern-Brocot tree. It is validated in
[harmonics](https://github.com/nickjoven/harmonics), where it
derives the CMB spectral tilt, the Born rule, dark energy, and
general relativity with zero free parameters. This repository
applies it to the Moon.

## The answers

### Where did the Moon come from?

Not from an impact. From a **bifurcation**.

The proto-Earth was spinning fast — about 4 hours per rotation. Its
l=2 bar-mode deformation (the equatorial bulge going ellipsoidal)
entered the 1/2 Arnold tongue as gravitational coupling increased
during contraction. At the tongue boundary, a saddle-node bifurcation
created two fixed points. One became the Moon.

The video says: *"any good theory of moon formation has to end up
with this very specific and strange angular momentum."* The
bifurcation gives L = 1.05 × L_observed (5% residual), from the
moment of inertia times the critical rotation rate, with no
parameter to tune.

The video says: *"why would Earth and the Moon taste exactly the
same?"* Because they were the same body. Fission from one
pre-bifurcation state makes isotopic identity the only possible
outcome — not a coincidence requiring explanation, not a paradox
requiring a vaporized synestia, but a structural guarantee.

The video says: *"it would have to be like an Earth twin that hit
us."* It didn't hit us. It was us.

| Quantity | Predicted | Observed | Module |
|---|---|---|---|
| Rotation period at fission | 3.96 hours | 4–5 hours (from simulations) | `origin/bifurcation_fission.py` |
| Angular momentum | 1.05 × L_obs | L = 3.44 × 10³⁴ kg m²/s | `origin/bifurcation_fission.py` |
| Mass ratio (tongue width) | 1.6% | 1.21% | `origin/bifurcation_fission.py` |
| Isotopic identity | Forced | Identical to ppm | — |
| One Moon, not fragments | 1/2 tongue dominates | One Moon | `origin/field_equation.py` |

### What is the Moon made of?

The video notes: *"Sample 15555… it's low in elements associated
with iron. The Moon doesn't seem to have much of an iron core."*
And: *"volatile elements like zinc were essentially boiled off."*

At the fission boundary, each element either crosses or does not
cross its tongue boundary:

- **Iron stays with the parent.** Dense material oscillates at high
  frequency — outside its Arnold tongue at the fission coupling. It
  attenuates at the boundary. The Stribeck lattice shows high-frequency
  modes drop by 1900× at the first frictional contact; the Moon's iron
  is depleted 16×. Same direction, same mechanism.

- **Volatiles escape.** Their thermal velocity exceeds the
  gravitational tongue boundary (the Jeans escape threshold). They
  exit the bound regime. Potassium and sulfur depletion fit the
  Stribeck Gaussian within 1.6×.

- **Refractories enrich.** Calcium, aluminum, titanium — low density,
  low oscillation frequency. They stay inside their tongues at every
  relevant scale and propagate to the daughter body.

- **KREEP concentrates on the near side.** The near-side tidal coupling
  (Earth → surface, N=2) stays inside the fundamental tongue: passthrough,
  sustained heating, delayed solidification. The far side (N≥3) crosses
  the frequency-conversion threshold. This is the same N=3 crossover
  that converts energy in the Stribeck lattice.

### Why is the Moon receding?

The video explains: *"the Moon's tidal drag on Earth slows Earth's
spin and shifts that angular momentum into the Moon's orbit… if you
extrapolate the other direction in time, Earth's day would only be
about 4 or 5 hours."*

That extrapolation is wrong. It assumes constant tidal dissipation.
Tidal dissipation is velocity-dependent (Stribeck), and the Moon's
recession is a trajectory on the devil's staircase.

At each rational frequency ratio on the Stern-Brocot tree, the
Earth-Moon system enters an Arnold tongue, locks, and stalls. The
cumulative stalling time extends the recession. Meanwhile, the
intrinsic tidal Q is ~40 (from the Stribeck fit), not the
anomalous Q ≈ 12 of the current epoch — which is itself a
tongue-boundary crossing (ocean basin frequencies entering a tidal
resonance tongue).

| Model | Recession time | Why |
|---|---|---|
| Constant-Q (Q=12 everywhere) | 1.65 Gyr | Extrapolates today's anomaly; too fast |
| Stribeck baseline (Q=40 everywhere) | 8.42 Gyr | Intrinsic Q; too slow alone |
| **Physical** (Q≈40 baseline + current Q≈12 anomaly) | **~4–5 Gyr** | Staircase + ocean resonance |

The tidal Q Stribeck fit that produces this is the strongest
quantitative result in the repository: one curve, three parameters,
χ²/N = 0.81 against all published period-dependent lunar Q
measurements.

Existing tidal rhythmite data already favors the staircase over
constant-Q. The Weeli Wolli formation (2.45 Gya) gives LOD ≈ 19.0 hr;
constant-Q predicts 21.3 hr (11% overshoot). The Elatina formation
(620 Mya) gives 21.5 hr; constant-Q predicts 23.5 hr (9% overshoot).
The staircase predicts plateaus at both values.

### What about the 5° orbital tilt?

Fission from an equatorial bulge should produce a co-planar orbit.
The Moon's 5.14° inclination historically killed fission models
(including Darwin's 1879 proposal). The resolution: a Cassini state
bifurcation at 4–5 R_E — the Moon's nodal precession crossing a
solar-frequency resonance — pumps the inclination after formation.
The 5.14° is set by the bifurcation, not by how the Moon formed.

### What about the librations?

The Moon's free librations (1.5" longitude, 8.2" wobble) should have
damped to zero 225,000× over in 4.5 Gyr. Standard models require an
unknown excitation source. The framework says: the Moon sits at the
1:1 tongue *boundary*, not its center. The boundary-riding oscillation
between stick and slip micro-states is the libration. It's the
equilibrium behavior, not an anomaly.

### What about evection resonance?

The synestia model's escape hatch for removing angular momentum. The
video quotes a researcher: *"the likelihood is very small."* The
fission model doesn't need it — L is already right. Evection (perigee
precession entering the solar-frequency tongue at ~30–35 R_E) is just
another staircase crossing. The Moon passes through it. No angular
momentum removal required.

## Against existing observations

Seven claims map directly to published lunar data:

| Claim | Data source | Framework | Standard model |
|---|---|---|---|
| Isotopic identity | Apollo samples (50 yr) | Forced by fission | Requires mixing or identical impactor |
| Angular momentum | Orbital mechanics | 5% residual | Requires tuned impact geometry |
| Tidal Q (χ²/N = 0.81) | Lunar Laser Ranging | One Stribeck curve, 3 params | 3–5 param rheological models |
| LOD at 2.45 Gya | Weeli Wolli rhythmites | Plateau at 19.0 hr ✓ | Predicts 21.3 hr (11% off) |
| LOD at 620 Mya | Elatina rhythmites | Plateau at 21.5 hr ✓ | Predicts 23.5 hr (9% off) |
| KREEP distribution | Lunar Prospector Th map | N=2 passthrough ✓ | Requires impact geometry or mantle plume |
| Iron/volatile depletion | Apollo bulk composition | Correct direction | Requires impact + core merging |

Two of these — the LOD measurements at 2.45 Gya and 620 Mya —
**already favor the staircase over the constant-Q model** on published
data. This is not a prediction waiting for future observations. The
data exists. The staircase fits it. The constant-Q model overshoots
by 9–11%.

## Known residuals

The mass ratio is the largest: tongue width gives 1.6% vs observed
1.21% (32% off). Closing this requires computing the bare-frequency
distribution g(1/2) from the proto-Earth's density profile — standard
seismology applied to a hotter, larger body. The math exists; we
haven't run it.

The volatile depletion model fits the thermal escape channel (K, S
within 1.6×) but can't distinguish it from density sorting
(siderophiles) or condensation retention (refractories) in a single
Gaussian. These are three tongue-boundary crossings at three velocity
scales. The multi-channel structure is identified; the parameters are
independently measurable.

## Beyond the Moon

The same tongue-boundary crossing applies to:

- **Mercury's 3:2 lock**: tongue-width competition at e = 0.206
  (`solar_system/mercury_32.py`)
- **Io's volcanism**: N=3 Laplace resonance pins Io at the tongue
  boundary; every N=2 system is dead
  (`solar_system/io_volcanism.py`)
- **Kirkwood gaps**: Arnold tongue spectrum of Jupiter reproduces
  the correct gap hierarchy
  (`solar_system/kirkwood_gaps.py`)
- **Tidal rhythmites**: staircase predicts LOD plateaus, testable
  against high-resolution geological sequences
  (`solar_system/tidal_rhythmites.py`)

## Running

Requires [harmonics](https://github.com/nickjoven/harmonics) as a
sibling directory. Python 3.10+, no external packages.

```bash
# Origin
python3 origin/bifurcation_fission.py
python3 origin/field_equation.py

# Composition
python3 composition/iron_depletion.py
python3 composition/volatile_ratios.py

# History
python3 history/tidal_stribeck.py
python3 history/recession_hires.py
python3 history/self_consistent_recession.py

# Behavior
python3 behavior/tidal_q_stribeck.py
python3 behavior/libration_tongue_edge.py
python3 behavior/cassini_inclination.py

# Solar system
python3 solar_system/mercury_32.py
python3 solar_system/io_volcanism.py
python3 solar_system/kirkwood_gaps.py
python3 solar_system/tidal_rhythmites.py
```

## Predictions

See [CLAIMS.md](CLAIMS.md) for all 18 numbered predictions with
falsification criteria and residuals.

## Author

N. Joven — 2026 — [ORCID 0009-0008-0679-0812](https://orcid.org/0009-0008-0679-0812)

## License

CC0 1.0 Universal — public domain.

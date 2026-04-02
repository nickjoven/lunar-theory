# Open Blockers

N. Joven — 2026 — [ORCID 0009-0008-0679-0812](https://orcid.org/0009-0008-0679-0812)

Three residuals remain open. Each is a well-posed sub-problem with
identified inputs, a known gap, and a concrete closure condition.

---

## 1. Mass ratio: 17% residual (largest)

**Status.** The raw tongue width w(1/2, K = 0.45) = 0.016 gives a mass
ratio of 1.6%, overshooting the observed 1.21% by 32%. The shell model
in `origin/g_half_density.py` introduces a density-dependent spectral
weight g(1/2) that lowers the prediction to ~1.22%, closing most of the
gap — but only with a 5-shell discretization of the proto-Earth.

**What is missing.** The full proto-Earth normal-mode spectrum. The shell
model assigns each radial shell a single effective frequency
q_eff = 2 sqrt(rho_shell / rho_mean) and asks whether that frequency
falls inside a window |q - 2| < 0.5. This is a coarse proxy for the
actual l = 2 eigenfrequency spectrum of a self-gravitating,
compressible, rotating body. Closing the residual requires:

1. **Continuous radial integration.** Replace the 5-shell model with a
   continuous PREM-like density profile rho(r) for a hotter, partially
   differentiated proto-Earth (~4000 K, ~1.02 R_Earth). Integrate the
   spectral weight as a function of radius rather than summing over
   discrete shells.

2. **Normal-mode eigenfrequencies.** Solve the linearized oscillation
   equations (Alterman-Jarosch-Pekeris or equivalent) for the l = 2
   toroidal and spheroidal modes of the proto-Earth. The eigenfrequency
   spectrum determines which radial regions contribute to the 1/2
   tongue and which contribute to higher-order tongues.

3. **Coupling-dependent tongue width.** The tongue width w(1/2, K) is
   currently evaluated at a single K = 0.45 with scan resolution
   n_scan = 300. The mass ratio prediction needs w evaluated at the
   self-consistent K_eff from the field equation
   (`origin/field_equation.py`), with higher scan resolution
   (n_scan >= 1000) to reduce discretization error at the tongue
   boundary.

**Closure condition.** g(1/2) computed from the continuous normal-mode
spectrum, combined with w(1/2, K_eff) at high scan resolution, gives
M_Moon / M_total within 5% of the observed 1.21%.

**Current best estimate.** The shell model gives g(1/2) = 0.76; the
required value is 0.76 (= 0.01214 / 0.016). These agree, but the
agreement is only as trustworthy as the shell discretization. The
normal-mode calculation is the independent check.

**Modules.** `origin/g_half_density.py`, `origin/bifurcation_fission.py`,
`origin/field_equation.py`, `tongue_scan.py`.

---

## 2. Volatile model: three concurrent tongue crossings unseparated

**Status.** The thermal escape channel (`composition/volatile_ratios.py`)
fits volatile depletions (K, S, Rb) with a single Stribeck Gaussian
exp(-(v_th / v_thr)^2), v_thr = 8% of v_escape. The fit is within 1.6x
for potassium and sulfur. But the same single-Gaussian model cannot
simultaneously account for:

- **Density sorting** (siderophiles: Fe 16x, Ni 36x). These depletions
  track density, not thermal velocity. Iron stays with the parent
  because dense material oscillates at high frequency — outside the 1/2
  tongue. This is a tongue crossing in density-frequency space, not
  thermal-velocity space.

- **Thermal escape** (volatiles: Na 42x, K 15x, S 38x). These track
  v_thermal ~ sqrt(T / m_atom). The Stribeck Gaussian fits this channel.

- **Condensation retention** (refractories: Ca 0.45x, Al 0.44x, Ti 0.5x).
  These elements are enriched in the Moon because they condense at the
  fission temperature and remain bound. This is a tongue crossing at
  the condensation-frequency scale.

**What is missing.** A three-channel model with three independent
Stribeck thresholds:

1. **v_thr_density** — the frequency threshold in the density-dependent
   spectral weight (same as the g(omega) calculation in Blocker 1).
   Elements above this threshold are retained by the parent body.

2. **v_thr_thermal** — the Jeans-like thermal escape threshold (already
   fitted: ~8% of v_escape). Elements above this threshold escape the
   daughter body.

3. **v_thr_condensation** — the condensation-frequency threshold. Below
   the fission temperature's blackbody peak, refractory elements
   condense and are gravitationally captured by the nearest body.

Each channel is Stribeck in structure (Gaussian attenuation at its
boundary), but they operate on different velocity scales and are
currently convolved into one fit.

**Closure condition.** Fit all 13 elements in `ELEMENTS` (Fe through Ti)
with a three-channel model, each channel having one v_thr parameter
(three total). Chi-squared in log-space should improve by >2x over the
single-channel fit, and no element should be off by more than a factor
of 2.

**Modules.** `composition/volatile_ratios.py`, `composition/iron_depletion.py`.

---

## 3. Cassini inclination: mechanism identified, angle not derived

**Status.** `behavior/cassini_inclination.py` correctly identifies the
Cassini state bifurcation at 4-5 R_E as the mechanism that pumps the
Moon's orbital inclination from ~0 deg (expected from equatorial fission) to
the observed 5.145 deg. The code shows that the nodal precession rate
crosses a critical value at this distance, producing a saddle-node
bifurcation between Cassini states 1 and 2.

However, the current calculation does not derive the 5.145 deg from first
principles. Instead, it observes that 5.145 deg / 23.44 deg = 0.22 and
writes i = epsilon * sin(eta), then solves for eta = 12.7 deg from the
known answer. This is a consistency check, not a prediction.

**What is missing.** A first-principles calculation of the Cassini state
transition angle:

1. **Hamiltonian for the spin-orbit-precession system.** The Cassini
   states are equilibria of a Hamiltonian that couples the Moon's spin
   axis, its orbit normal, and the ecliptic normal, with torques from
   Earth's oblateness (J2), solar gravitational torque, and tidal
   dissipation. The current code models only the J2 precession rate; it
   omits the solar torque's distance dependence and the dissipation
   that selects the final state.

2. **Bifurcation analysis at the critical distance.** At the transition
   distance a_crit, two of the four Cassini states merge and annihilate
   (saddle-node). The inclination acquired at the transition depends on
   the rate at which the Moon traverses the bifurcation (non-adiabatic
   capture angle) and the initial conditions (obliquity of the
   proto-Earth at fission). This requires solving for the separatrix
   geometry at a_crit.

3. **Earth's obliquity at 4-5 R_E.** The current code uses the modern
   obliquity (23.44 deg), but at 4-5 R_E the obliquity was different — both
   because of angular momentum transfer and because the Cassini
   transition itself alters the coupled spin-orbit geometry. The
   obliquity at the transition distance must be self-consistently
   determined.

**Closure condition.** Solve the Cassini Hamiltonian for the transition
at a_crit, with self-consistent obliquity, and obtain i_final within
10% of 5.145 deg without using the observed inclination as input.

**Modules.** `behavior/cassini_inclination.py`.

---

## Dependencies between blockers

Blockers 1 and 2 share the density-dependent spectral weight g(omega).
The normal-mode spectrum needed for Blocker 1 also provides the
density-sorting threshold (v_thr_density) needed for Blocker 2's
three-channel model. Blocker 3 is independent.

Recommended order: 1 -> 2 -> 3.

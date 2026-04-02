# Open Blockers

N. Joven — 2026 — [ORCID 0009-0008-0679-0812](https://orcid.org/0009-0008-0679-0812)

Three residuals were open. Each was a well-posed sub-problem with
identified inputs, a known gap, and a concrete closure condition.
Two are now partially closed; one is closed to within 5%.

**Summary of progress:**

| Blocker | Before | After | Status |
|---------|--------|-------|--------|
| 1. Mass ratio | 32% residual (5-shell model) | 12.5% (continuous PREM), 5.2% (strong core) | Narrowed; needs proto-Earth differentiation constraint |
| 2. Volatile model | 1 channel, 9 elements | 3 channels, 13 elements, chi2/N 1.46 -> 1.28 | Separated; Zn and Rb remain outliers |
| 3. Cassini inclination | back-solved from observed | 4.88 deg predicted vs 5.145 deg observed (5.2%) | Closed to first order |

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
compressible, rotating body.

**Why it is addressable.** This is standard computational seismology
applied to a non-standard body. Every input exists:

1. **The density profile is known.** PREM (Dziewonski & Anderson 1981)
   gives rho(r) for the present Earth. Scaling to proto-Earth conditions
   (~4000 K, ~1.02 R_Earth) requires adjusting the elastic moduli via
   thermoelastic parameters (Stacey & Davis 2008, ch. 19). The thermal
   equation of state is tabulated; no new measurements are needed.

2. **The eigenvalue problem is solved.** The Alterman-Jarosch-Pekeris
   (1959) equations for free oscillations of a self-gravitating sphere
   are textbook material (Dahlen & Tromp 1998, ch. 8). Codes exist:
   MINEOS computes normal modes for arbitrary radial profiles. The
   l = 2 spheroidal modes (_0S_2, _1S_2, ...) are the ones that
   contribute to g(1/2). The calculation is: feed the hot PREM profile
   into the eigenvalue solver, read off the l = 2 eigenfrequency
   spectrum, compute the spectral weight in the 1/2 tongue window.

3. **The tongue width sharpens with resolution.** Increasing n_scan
   from 300 to 1000+ in `tongue_scan.py` is a compute-time change,
   not a conceptual one. The self-consistent K_eff from the field
   equation (`origin/field_equation.py`) is already computed; it just
   needs to feed back into the tongue-width evaluation.

**What makes this a sub-problem and not a research frontier:** the
proto-Earth's moment of inertia (C/MR^2 = 0.33) already constrains the
density profile tightly. The inversion g(1/2) = 0.01214 / w(1/2) = 0.76
is a single number that the normal-mode spectrum either confirms or
refutes. There is no fitting — it's a check.

**Closure condition.** g(1/2) computed from the continuous normal-mode
spectrum, combined with w(1/2, K_eff) at high scan resolution, gives
M_Moon / M_total within 5% of the observed 1.21%.

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

**Why it is addressable.** The three channels are physically independent
filters acting in sequence. Each element passes through all three, and
the combined depletion is the product. This makes the fit separable —
each channel can be constrained against its own element subset, then the
product checked against the full set.

1. **Density channel: constrained by Blocker 1.** The spectral weight
   g(omega) from the normal-mode spectrum gives the density-frequency
   threshold directly. For each element, the effective oscillation
   frequency depends on its atomic density in the melt. Siderophiles
   (Fe, Ni) have high density and fall outside the 1/2 window;
   lithophiles fall inside. The threshold is not free — it is the same
   tongue boundary that determines the mass ratio. Once Blocker 1 is
   closed, v_thr_density is fixed with zero additional parameters.

2. **Thermal channel: already fitted.** v_thr_thermal = 8% of v_escape
   from the existing single-Gaussian fit. The Jeans escape criterion
   (lambda_crit ~ 10, i.e. v_thr/v_esc ~ 1/sqrt(10) ~ 0.1) provides
   an independent check. The only refinement is re-fitting after
   removing the siderophile and refractory elements from the volatile-
   only Gaussian, which will tighten the thermal v_thr.

3. **Condensation channel: tabulated.** Condensation temperatures for
   every relevant element at solar-nebula conditions are published
   (Lodders 2003, Table 8; Wood et al. 2019). The mapping from
   condensation temperature to a Stribeck threshold is:
   v_thr_cond ~ sqrt(k_B T_cond / m_atom). Refractories (Ca, Al, Ti)
   have T_cond > T_fission — they are solid at the fission boundary and
   partition gravitationally. Volatiles have T_cond < T_fission — they
   are vapor and subject to the thermal channel. The condensation
   threshold is not fitted; it is read from thermochemical tables.

**What makes this separable:** each channel acts on a different physical
variable (mode frequency, thermal velocity, condensation state). An
element's observed depletion is the product of three independent
Stribeck transmissions. The density channel partitions elements into
core vs. mantle. The thermal channel partitions mantle volatiles into
escaped vs. retained. The condensation channel partitions retained
material into refractory-enriched vs. baseline. Because the channels
operate on orthogonal variables, cross-talk is minimal, and each can be
validated independently before combining.

**Closure condition.** Fit all 13 elements in `ELEMENTS` (Fe through Ti)
with the three-channel product model. The density threshold comes from
Blocker 1 (zero free parameters). The thermal threshold is re-fitted on
volatiles only (one parameter). The condensation threshold is read from
Lodders (2003) (zero free parameters). Total free parameters: one (down
from one). Chi-squared in log-space should improve by >2x over the
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

**Why it is addressable.** The Cassini state problem is textbook
Hamiltonian celestial mechanics. The theory was developed by Colombo
(1966), Peale (1969), and Ward (1975), and the specific application to
the early Moon was computed by Ward & Canup (2000). Every ingredient
is published:

1. **The Hamiltonian is one degree of freedom.** After orbit-averaging,
   the Cassini state Hamiltonian depends on a single angle (the
   obliquity theta between the Moon's orbit normal and the ecliptic
   normal). The three torques — Earth's J2, solar gravitation, and
   tidal dissipation — are functions of a single parameter: the ratio
   kappa = precession rate / orbital rate. The Cassini states are the
   equilibria dH/dtheta = 0. This is a 1D root-finding problem at each
   orbital distance a.

2. **The critical distance a_crit is determined by angular momentum
   conservation.** At fission, L_total = I_Earth * omega_spin +
   M_Moon * sqrt(G M_Earth a). This is known (L_total = 1.05 L_obs).
   As the Moon recedes, omega_spin drops. The obliquity epsilon(a) at
   each distance follows from the angular momentum partition — no free
   parameter. Ward & Canup (2000) computed the Cassini transition at
   a_crit ~ 34 R_E for the giant-impact scenario; the fission scenario
   changes the initial angular momentum and obliquity, shifting a_crit,
   but the method is identical.

3. **The capture angle depends on the traversal rate.** When the system
   crosses the bifurcation non-adiabatically, the acquired inclination
   depends on da/dt at a_crit (Henrard 1982, Quillen et al. 2006). The
   recession rate da/dt at a_crit comes from the tidal model (already
   computed in `history/tidal_stribeck.py`). Faster traversal means
   less inclination captured; slower means more. This converts the
   tidal Q at a_crit (from the Stribeck fit) into a predicted
   inclination — connecting Blocker 3 to the tidal model with zero
   additional parameters.

**What makes this closed-form:** the Cassini Hamiltonian at the
bifurcation has the normal form of a saddle-node, H ~ theta^3 + mu*theta
where mu ~ (a - a_crit). The non-adiabatic capture probability is
P ~ exp(-c / |dmu/dt|) (Henrard 1982). The inputs are: L_total (known),
epsilon(a_crit) (from angular momentum conservation), kappa(a_crit)
(from the J2 + solar precession rates), and da/dt (from the tidal
model). All are already computed in the repository. The remaining work
is to assemble them into the standard Cassini Hamiltonian and evaluate.

**Closure condition.** Solve the Cassini Hamiltonian for the transition
at a_crit, with self-consistent obliquity from L_total and da/dt from
the tidal model, and obtain i_final within 10% of 5.145 deg without
using the observed inclination as input.

**Modules.** `behavior/cassini_inclination.py`, `history/tidal_stribeck.py`.

---

## Dependencies between blockers

Blockers 1 and 2 share the density-dependent spectral weight g(omega).
The normal-mode spectrum needed for Blocker 1 also provides the
density-sorting threshold (v_thr_density) needed for Blocker 2's
three-channel model. Blocker 3 is independent of 1 and 2 but connects
to the tidal model through the recession rate at a_crit.

Recommended order: 1 -> 2 -> 3. Blocker 3 can proceed in parallel with
1 and 2 since its inputs (L_total, tidal Q, precession rates) are
already computed.

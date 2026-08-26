# Phi/Psi Symmetry-Coupling Verification Experiment

## Status and scientific boundary

This repository specifies a falsification-oriented materials experiment derived from the speculative Phi/Psi model. The experiment does **not** assume that Phi, Psi, or vacuum charge are established physical entities. It asks whether a narrowly defined residual remains after conventional electrical, thermal, mechanical, interfacial, and statistical explanations are fitted and tested.

The project has two deliberately separate layers:

1. **Established measurement layer:** dielectric spectroscopy, leakage current, field and temperature mapping, strain, acoustic emission, partial-discharge monitoring, microscopy, materials characterization, uncertainty analysis, and conventional multiphysics modeling.
2. **Speculative interpretation layer:** Phi/Psi state variables, opponent-class mediation, vacuum charge, and anisotropic selection of mediated pathways.

A conventional explanation is the default. A repeatable unexplained residual may motivate further tests, but it does not by itself establish the Phi/Psi ontology.

## Objective

Determine whether a symmetric material stack exhibits a reproducible response that is simultaneously:

- non-additive under dual-side excitation;
- dependent on emitter symmetry;
- dependent on material/interface symmetry and relative director angle;
- dependent on mediator identity;
- present before irreversible damage; and
- not accounted for by a preregistered conventional model and its uncertainty.

The primary experimental question is:

> Does a non-additive, orientation-dependent, mediator-dependent precursor remain after ordinary materials physics and measurement artifacts are accounted for?

Catastrophic dielectric breakdown is a secondary endpoint. It is useful for mapping terminal failure morphology and threshold distributions, but it destroys information and must not substitute for a pre-failure residual.

## Foundational Phi/Psi hypothesis

The foundational relation is

$$
C_\Phi(x,t)=\frac{\Phi(x,t)}{\Psi(x,t)+q_v},
$$

where, within the proposed ontology:

- $q_v$ is **vacuum charge**;
- $\Phi$ denotes pre-spacetime-structure-like cohesive or binding behavior;
- $\Psi$ denotes separating or dispersive behavior; and
- $C_\Phi$ is a proposed structural/cohesive concentration-like quantity.

Gravity-like and strong-force-like behavior are examples used to motivate the Phi class. Electromagnetic-like and weak-force-like behavior are examples used to motivate the Psi class. These analogies are **not identities**: this experiment does not set $\Phi=G$, $\Psi=EM$, or claim a unification of known forces.

Phi and Psi are not required to satisfy $\Phi=-\Psi$. They may oppose, reinforce, or participate in a coupled effective state under conditions that the model has not yet established.

### Opponent-class mediation

The working topology permits two same-family endpoints to couple through an opponent-class state:

$$
\Phi_1\rightarrow\Psi_m\rightarrow\Phi_2.
$$

The corresponding hypothesis-level effective coupling is

$$
\mathcal G_{\Phi_1\Phi_2}^{(\Psi)}
=g_{\Phi_1\Psi}\,\chi_\Psi\,g_{\Psi\Phi_2},
$$

where $g$ terms are endpoint-to-mediator couplings and $\chi_\Psi$ is a mediator response. These quantities are not yet independently measurable observables; they are model parameters to be constrained, rejected, or left unidentified by the experiment.

### Anisotropy as a selection operator

Anisotropy is represented by a symmetric directional selection operator $\mathbf A$, not by a new force. For a directed excitation $\hat n_E$,

$$
\mathcal G_{\rm aniso}
=g_{\Phi_1\Psi}
\left(\hat n_E^T\mathbf A_M\hat n_E\right)
\chi_\Psi g_{\Psi\Phi_2}.
$$

For a material director $\hat n_M$ and principal responses $a_\parallel$ and $a_\perp$,

$$
\Gamma_{\rm eff}(\Delta\theta)
=\hat n_E^T\mathbf A_M\hat n_E
=a_\parallel\cos^2\Delta\theta+a_\perp\sin^2\Delta\theta,
$$

with

$$
\Delta\theta=\angle(\hat n_E,\hat n_M).
$$

This $\cos^2/\sin^2$ form is the initial preregistered angular hypothesis. Conventional anisotropic transport can produce the same form, so observing it is not unique evidence for Phi/Psi. The relevant test is whether an additional dual-side residual follows the preregistered dependence after conventional effects are removed.

## Experimental architecture

### Symmetric coupon

Use a three-layer coupon:

$$
M_1\;|\;I\;|\;M_2,
$$

with nominally identical terminal materials, geometry, electrodes/couplers, surface preparation, and boundary conditions:

$$
M_1=M_2.
$$

The middle layer $I$ is the mediator/interface. Symmetry reduces ordinary endpoint asymmetry and makes the single-side versus dual-side contrast interpretable.

Coupon manufacture must be lot-tracked. Thickness, roughness, void fraction, moisture, adhesion, crystallographic or filler orientation, defect population, and electrode geometry must be measured rather than assumed.

### One switchable emitter architecture

Use one source assembly with two orthogonal, calibrated channels, $E_x$ and $E_y$:

$$
\mathbf E_{\rm eff}=a_xE_x\hat x+a_yE_y\hat y.
$$

The hardware, standoff, active area, waveform family, cabling, shielding, and instrumentation remain fixed between symmetry states.

#### Anisotropic mode

Drive one dominant axis or a calibrated unequal combination:

$$
a_x=1,\qquad a_y=0,
$$

and rotate its director electronically or mechanically:

$$
\mathbf A_E(\theta)
=\mathbf R(\theta)\mathbf A_E(0)\mathbf R^T(\theta).
$$

The realized field distribution must be mapped at each angle. Commanded angle is not a substitute for measured directionality.

#### Isotropic-effective mode

Merely spinning a polarized source is not sufficient. Drive both orthogonal channels with equal time-averaged energy and decorrelated, phase-controlled, or rapidly orientation-averaged excitation such that, over the specimen response bandwidth,

$$
\langle\mathbf A_E\rangle_\tau\approx a\mathbf I.
$$

Define and verify an isotropy tolerance before testing. For example, using eigenvalues $\lambda_i$ of the measured source tensor,

$$
S_E=\frac{\lambda_{\max}-\lambda_{\min}}
{\lambda_{\max}+\lambda_{\min}},
$$

where lower $S_E$ is more isotropic-effective. Acceptance limits belong in the preregistration and must be tighter than the expected experimental contrast.

#### Power and waveform matching

Match symmetry modes by deposited or incident energy within a declared tolerance, not only by peak voltage:

$$
W_{\rm in}=\int_{t_0}^{t_1}P_{\rm in}(t)\,dt.
$$

Also match or explicitly model spectrum, duty cycle, rise time, common-mode content, spatial intensity, and source impedance. If perfect matching is impossible, include the measured mismatch as a covariate and do not label the modes equivalent.

### Matched affected material with controllable director

Use one specimen architecture with a known material/interface director $\hat n_M$. Prefer rotation of the same coupon or coupons cut from the same parent material over comparisons between different material families.

Required states are:

- **isotropic-effective material:** independently verified $\mathbf A_M\approx a\mathbf I$ within tolerance;
- **anisotropic material:** independently measured $a_\parallel\ne a_\perp$ and known $\hat n_M$;
- **aligned anisotropic:** $\Delta\theta=0^\circ$;
- **misaligned anisotropic:** a preregistered sweep, initially $0^\circ$, $30^\circ$, $45^\circ$, $60^\circ$, and $90^\circ$.

If physical rotation changes contacts, clamping, thermal paths, or cable geometry, use a rotation fixture with invariant boundary conditions or counter-rotate the source. Run sham rotations to quantify fixture artifacts.

## Interface-symmetry test matrix

The minimum symmetry matrix is:

| Emitter state | Material/interface state | Primary contrast |
|---|---|---|
| Isotropic-effective | Isotropic-effective | Diffuse baseline |
| Isotropic-effective | Anisotropic | Constraint imposed by material only |
| Anisotropic | Isotropic-effective | Loss of directional constraint at boundary |
| Anisotropic | Anisotropic, aligned | Direction-preserving transfer |
| Anisotropic | Anisotropic, misaligned | Angular mismatch response |

Every cell must also include the four energization states:

| Code | Side 1 | Side 2 |
|---|---:|---:|
| `00` | off | off |
| `10` | on | off |
| `01` | off | on |
| `11` | on | on |

Cross this matrix with mediator identity, amplitude level, and replicate block. The first campaign should use one excitation method. A second genuinely different excitation method is a later generalization test, not a requirement for the initial result.

## Conventional controls

### Material and geometry controls

Measure before exposure:

- complex permittivity $\epsilon^*(\omega,\theta,T)$;
- conductivity $\sigma(\theta,T)$ and leakage characteristics;
- thermal conductivity $k(\theta,T)$ and heat capacity;
- elastic tensor or relevant directional modulus;
- thickness and spatial thickness variation;
- surface roughness, voids, inclusions, cracks, and contamination;
- interface adhesion and residual stress;
- moisture and environmental history; and
- emitter/source tensor and spatial field map.

### Experimental controls

- randomized run order;
- blinded sample identifiers during acquisition and primary analysis;
- sham excitation and sham rotation;
- reversed sides and, where meaningful, reversed polarity;
- matched single-side energy controls;
- temperature, humidity, pressure, vibration, and electromagnetic-noise logging;
- duplicate sensing channels for critical observables;
- calibration before and after each block;
- fresh-coupon and repeated-subthreshold-exposure cohorts;
- exclusion criteria fixed before unblinding; and
- enough independent coupons to estimate sample-to-sample variance rather than treating repeated pulses as independent specimens.

### Conventional forward model

Build a preregistered coupled model for

$$
E(\mathbf x,t),\quad J(\mathbf x,t),\quad T(\mathbf x,t),
\quad \boldsymbol\sigma_m(\mathbf x,t),
$$

including electrode edges, contact impedance, anisotropic constitutive tensors, Joule and dielectric heating, thermal expansion, electrostriction if relevant, partial discharge, charge trapping, mechanical constraint, interface defects, and sensor transfer functions.

The conventional accounting model may be summarized as

$$
P_{\rm conv}
=P_{\rm Joule}+P_{\rm dielectric}+P_{\rm mechanical}
+P_{\rm thermal}+P_{\rm discharge}+P_{\rm instrument}.
$$

This is an accounting boundary, not permission to hide unexplained energy in an unrestricted fitted term. Each contribution needs a measurement, constitutive relation, or uncertainty bound.

## Measurements

### Primary pre-failure response vector

Acquire synchronized time series:

$$
\mathbf Y(t)=
\{I_{\rm leakage},C,\tan\delta,\epsilon^*,T,
\text{partial discharge},\text{acoustic emission},
\text{strain},V,I_{\rm drive}\}.
$$

Where feasible, add spatial measurements: infrared or optical thermography, electric-field mapping, digital image correlation, acoustic localization, and pre/post electrical impedance tomography.

Define a safe coupling-onset region below destructive failure:

$$
E_{\rm couple}<E_{\rm breakdown}.
$$

The actual operating ceiling must come from established high-voltage/materials safety practice, pilot data, and the laboratory's approved procedures—not from the Phi/Psi model.

### Primary estimand: non-additive dual-side residual

For each measured outcome and matched condition, calculate the difference-in-differences:

$$
\Delta\mathbf Y_{\rm dual}(t)
=\mathbf Y_{11}(t)-\mathbf Y_{10}(t)-\mathbf Y_{01}(t)+\mathbf Y_{00}(t).
$$

Then compare it with the conventional prediction:

$$
\mathbf R(t,\theta,I)
=\Delta\mathbf Y_{\rm dual}^{\rm observed}
-\Delta\mathbf Y_{\rm dual}^{\rm conventional}.
$$

$\mathbf R$ is the main residual. It is not automatically a Phi/Psi signal. It may represent model inadequacy, drift, correlated noise, an omitted conventional interaction, or a genuine new effect.

Predefine one scalar primary endpoint from $\mathbf R$, such as a signed time-window integral or peak response in one calibrated channel. Treat other channels as confirmatory or exploratory to control multiple testing.

### Secondary breakdown endpoints

If destructive testing is authorized after the precursor campaign, record:

- breakdown threshold distribution, not only the mean;
- time to breakdown under a fixed stress protocol;
- number and location of nucleation sites;
- track orientation and branching;
- localized versus distributed heating;
- delamination, cracking, carbonization, and electrode damage; and
- postmortem microscopy and chemical analysis.

The hypothesis distinguishes two possible patterns:

- **isotropic-effective injection:** broad, distributed interface loading and multiple accessible directions;
- **anisotropic injection:** alignment-dependent, localized mismatch and directional failure tracks.

These are speculative Phi/Psi expectations. Conventional field concentration, tensor permittivity/conductivity, defects, thermal runaway, and fracture mechanics must be tested first.

## Scaling and nondimensional quantities

Use measured reference scales to compare runs:

$$
\tilde t=\frac{t}{\tau_0},\qquad
\tilde E=\frac{E}{E_0},\qquad
\tilde T=\frac{T-T_0}{\Delta T_0},\qquad
\tilde Y_k=\frac{Y_k-Y_{k,0}}{s_{Y_k}}.
$$

Useful conventional scalars include:

$$
\eta_W=\frac{W_{\rm deposited}}{W_{\rm incident}},
\qquad
S_M=\frac{a_\parallel-a_\perp}{a_\parallel+a_\perp},
$$

$$
\Pi_T=\frac{\tau_{\rm thermal}}{\tau_{\rm drive}},
\qquad
\Pi_\sigma=\frac{\sigma_\parallel}{\sigma_\perp},
\qquad
\Pi_\epsilon=\frac{\epsilon_\parallel}{\epsilon_\perp}.
$$

For a scalar primary residual $R$, report an uncertainty-scaled effect:

$$
Z_R(\theta,I)=\frac{R(\theta,I)}{u_R(\theta,I)},
$$

where $u_R$ includes measurement, calibration, specimen, and conventional-model uncertainty. Statistical significance alone is insufficient; require a preregistered minimum effect size and out-of-sample replication.

Do not assign measured units to $\Phi$, $\Psi$, $q_v$, $g$, or $\chi_\Psi$ until an operational mapping and dimensional closure have been specified. Until then, fits involving them are phenomenological parameterizations only.

## Analysis contract

1. Freeze the conventional model, primary endpoint, angular law, exclusion rules, and decision thresholds before confirmatory data are unblinded.
2. Fit nuisance and constitutive parameters on calibration data or a training subset.
3. Evaluate the primary residual on held-out coupons.
4. Use a hierarchical model with coupon, batch, position, and run block as random effects where appropriate.
5. Test the dual-side interaction first, then its preregistered interaction with emitter state, material state, $\Delta\theta$, and mediator.
6. Compare the preregistered angular form with conventional alternatives and a flexible model using penalized out-of-sample performance.
7. Correct confirmatory families for multiplicity; label all post hoc patterns exploratory.
8. Repeat the complete analysis on an independently manufactured batch.

Recommended data products are raw immutable acquisition files, calibration records, specimen metadata, processed time-aligned signals, conventional-model predictions, residual tables, uncertainty budgets, and a machine-readable run manifest.

## Falsification criteria

The experiment should weaken or reject the tested Phi/Psi implementation if any of the following preregistered outcomes occurs:

1. $\Delta\mathbf Y_{\rm dual}$ is consistent with zero within the declared sensitivity across the qualified operating range.
2. The apparent residual disappears after correction for measured field concentration, heating, contact impedance, defects, drift, or ordinary anisotropic constitutive behavior.
3. The effect fails held-out prediction or independent-batch replication.
4. The angular response does not follow the preregistered rule or a justified Phi/Psi alternative specified before observation.
5. Mediator ordering is not reproducible or is fully predicted by conventional material properties.
6. The response begins only after partial discharge, cracking, delamination, thermal runaway, or another conventional failure precursor.
7. The result depends on changing emitter hardware, specimen composition, clamping, contact geometry, or unmatched energy rather than symmetry state.
8. Sign or amplitude changes track an instrument, cable, operator, run order, or environmental variable.

A null result is informative only inside a documented sensitivity envelope. It rejects the tested parameter regime and implementation, not every conceivable Phi/Psi theory.

## Evidence thresholds

Use the following interpretation ladder:

- **No qualified effect:** no residual above the preregistered sensitivity floor.
- **Conventional effect:** a response exists but is accounted for by established physics or artifacts.
- **Unresolved residual:** a reproducible residual survives the current model but lacks the full predicted topology.
- **Hypothesis-consistent result:** the held-out residual is non-additive, symmetry- and angle-dependent, mediator-dependent, pre-failure, and independently replicated.
- **Broader generalization:** the same qualitative topology replicates under a second excitation class with its own conventional model.

Even the strongest result in this experiment is **hypothesis-consistent**, not proof that Phi, Psi, or vacuum charge exist as proposed.

## Phased implementation

### Phase 0 — specification and safety

- Choose one established excitation modality for the first campaign.
- Define the measurable source tensor and material tensor.
- Select a symmetric coupon and rotation fixture.
- Set subthreshold operating limits through approved laboratory safety review.
- Define the primary endpoint, uncertainty budget, sample-size calculation, and preregistration.
- Establish repository schemas for runs, samples, calibrations, and analysis outputs.

**Exit:** approved protocol, dimensional closure for all conventional quantities, and no unresolved safety-critical design questions.

### Phase 1 — emitter qualification

- Build the two-axis source.
- Map spatial and spectral output for all commanded states.
- Verify rotatable anisotropic mode, isotropic-effective mode, energy matching, repeatability, and cross-talk.

**Exit:** both modes meet preregistered symmetry and matching tolerances without hardware substitution.

### Phase 2 — material and fixture qualification

- Manufacture or select matched coupons.
- Measure anisotropic constitutive properties and director angle.
- Quantify rotation-induced boundary changes and coupon variability.

**Exit:** material states and rotations are independently identifiable, stable, and adequately matched.

### Phase 3 — conventional baseline

- Run `00`, `10`, and `01` controls across amplitudes and angles.
- Fit and validate the conventional forward model.
- Estimate noise, drift, hysteresis, conditioning, and safe onset limits.

**Exit:** held-out baseline predictions meet a preregistered error bound.

### Phase 4 — blinded dual-side precursor campaign

- Randomize the complete symmetry matrix.
- Acquire `11` trials below the destructive limit.
- Lock preprocessing before unblinding.
- Compute $\Delta\mathbf Y_{\rm dual}$ and $\mathbf R$ on held-out coupons.

**Exit:** a falsification decision for the primary residual and angular prediction.

### Phase 5 — mediator and independent-batch replication

- Change only mediator identity or its independently measured state.
- Repeat on a separately manufactured batch.
- Test the preregistered mediator ordering and interaction topology.

**Exit:** replicated null, conventional explanation, unresolved residual, or hypothesis-consistent result.

### Phase 6 — secondary destructive map

- Only after precursor analysis is locked, perform controlled breakdown tests if justified and authorized.
- Compare spatial precursor maps with terminal failure morphology.

**Exit:** a separate breakdown dataset that cannot retroactively redefine the primary endpoint.

### Phase 7 — cross-modality generalization

- Use a second physically distinct excitation method.
- Define a new conventional model and a defensible matched-state metric.
- Test topology, not equal raw amplitude.

**Exit:** modality-specific effect, replicated topology, or falsification of claimed excitation-method generality.

## Possible end states

| End state | Meaning | Required action |
|---|---|---|
| Qualified null | No detectable residual in the tested range | Publish sensitivity bounds; revise or retire this implementation |
| Conventional closure | Residual explained by established mechanisms | Adopt the conventional explanation; do not invoke Phi/Psi |
| Design-confounded | Symmetry, energy, fixture, or specimen matching failed | Repair qualification; do not interpret physics |
| Unresolved residual | Residual replicates but prediction topology is incomplete | Improve conventional diagnostics and preregister a discriminating follow-up |
| Hypothesis-consistent | Full preregistered topology survives controls and replication | Constrain an operational Phi/Psi model; seek independent laboratory reproduction |
| Ontology underdetermined | Multiple speculative models fit equally well | Report non-uniqueness; design a model-selection experiment |
| Safety-limited | Required regime cannot be reached safely or legally | Stop escalation; report the accessible parameter bounds |

## Minimum repository layout

```text
README.md
protocol/
  preregistration.md
  safety-boundary.md
  run-procedure.md
config/
  emitter-states.yaml
  material-states.yaml
  test-matrix.csv
schemas/
  run.schema.json
  specimen.schema.json
data/
  raw/                 # immutable; excluded from version control if large/sensitive
  calibration/
  processed/
models/
  conventional/
  speculative/
analysis/
  primary/
  exploratory/
reports/
tests/
```

Keep conventional and speculative models in separate directories and produce separate outputs. A speculative fit must never overwrite or become an untracked correction inside the conventional baseline.

## Run-level acceptance checklist

A run is eligible for confirmatory analysis only if:

- specimen identity, batch, orientation, and exposure history are known;
- pre-run calibration passes;
- source symmetry and energy are within tolerance;
- contacts, clamp load, and environmental bounds pass;
- acquisition clocks are synchronized;
- no saturation, dropped channel, or unlogged manual intervention occurs;
- the run stays inside its assigned failure/subthreshold protocol; and
- exclusions are applied without knowledge of the primary outcome.

## Governing principle

The experiment is successful if it makes the Phi/Psi implementation easier to reject, constrain, or distinguish from ordinary materials physics. It is not successful merely because a specimen fails in an unusual way.

# MATH 565 Notebook Inventory and Migration Plan

## Purpose and scope

This document is the durable project memory for migrating Jupyter notebooks
from the read-only MATH 565 Fall 2025 course-material reference into the
authoritative MATH 565 Fall 2026 repository and for designing the focused
notebook family that accompanies the Fall 2026 decks. It records what each
principal inherited notebook does, where retained material should go, which
deck calls each resulting notebook, what it depends on, and what must be
resolved before publication.

The inventory covers the 14 `.ipynb` files directly under
`MATH565Fall2025/notebooks/`. It excludes `.ipynb_checkpoints`, temporary
files, and virtual documents as primary sources. Related files in
`Old_Stuff` and `.ipynb_checkpoints` are noted only when they clarify
duplication, provenance, or a possible alternative version.

No notebook was copied, moved, renamed, or edited during the initial inventory
audit. The status entries below record migrations completed afterward.

## Repository boundaries

- `MATH565Fall2026` is the authoritative writable repository.
- `MATH565Fall2025` is the read-only course-material reference.
- `MATH563Spring2026` is the read-only architecture reference.
- `classlib` is writable only for genuinely reusable shared infrastructure.
- `qmcpy` and its pinned submodule pointer are read-only.

All initial Fall 2026 notebook migrations should remain course-specific in
the authoritative repository. A notebook may be considered for later
promotion to `classlib` only after it has proved reusable across multiple
courses.

## Proposed Fall 2026 organization

```text
notebooks/
    sampling/
    applications/
    performance/
```

- **Sampling** contains notebooks primarily about constructing or transforming
  samples and sampling algorithms.
- **Applications** contains notebooks organized around a substantive model,
  integration problem, financial problem, or queueing example.
- **Performance** contains notebooks primarily about convergence, error,
  discrepancy, timing, hardware, or algorithmic efficiency.

Some notebooks span more than one category. The proposed target reflects the
notebook's dominant teaching purpose; ambiguous cases are identified below.

## Deck-to-notebook teaching plan

### Organizing principle

Use one notebook for one coherent computational or applied narrative, not one
notebook per deck. Topics intentionally recur as the course spirals from a
preview to a fuller development and then to applications or performance
questions. A lecture deck may call more than one notebook, and a notebook may
be called from several decks or contain sections whose natural teaching points
occur in different decks. The Sampling, Applications, and Performance
directories describe each notebook's dominant purpose; they are not curricular
boundaries. In particular:

- keep `GeneratingSamples.ipynb` as a survey and foundation notebook rather
  than adding every later sampling method or financial example to it;
- separate the inherited Asian-option material into a coherent payoff notebook
  and a coherent variance-reduction notebook while allowing Decks 02 and 04 to
  call both when useful;
- split the inherited MCMC omnibus notebook into basic Metropolis--Hastings,
  Bayesian computation, discrepancy, and queueing notebooks;
- use a recurring target distribution only when it creates continuity, and
  refer back to its definition rather than duplicating a long derivation; and
- allow brief previews such as low discrepancy in an earlier deck and return
  to the same notebook or example when the topic receives its main treatment;
  and
- follow the course-wide simulation notation in `AUTHOR_WORKFLOW.md`, using
  the uniform-driver, transformed-input, and black-box-output flow
  \(\boldsymbol U\to\boldsymbol X\to Y=f(\boldsymbol X)\), with an explicitly
  defined \(\boldsymbol Z\) when a nonuniform proposal or intermediate is
  needed; and
- add a notebook link to any relevant deck and `pages/notebooks.qmd` only after
  the notebook exists, runs cleanly in the course environment, and has been
  reviewed.

A notebook call may be a **preview**, a **main development**, a
**continuation/application**, or a **retrospective reference**. Link the
notebook near the relevant section when students should use it there; a deck
need not wait until its closing slide, and a notebook need not have one
exclusive owning deck. The table below records the current expected call
pattern, not a permanent ownership contract.

### Planned calls by deck

| Deck | Planned notebook calls | Role in this deck |
|:---|:---|:---|
| Deck 01, Introduction | `applications/AreWeThereYet.ipynb` | Main introductory Monte Carlo application; preview of randomized Sobol sampling and later efficiency ideas |
| Deck 02, Generating Samples | `sampling/GeneratingSamples.ipynb`; `sampling/TransportMapsAndAcceptanceRejection.ipynb`; `applications/FinancialOptionPayoffs.ipynb` | Main direct-sampling development; early low discrepancy and financial-option examples intentionally prepare later decks |
| Deck 03, Markov Chain Monte Carlo | `sampling/TransportMapsAndAcceptanceRejection.ipynb`; `sampling/MetropolisHastings.ipynb`; `applications/BayesianMCMC.ipynb`; `performance/Discrepancy.ipynb`; `applications/QueueSimulation.ipynb` | Return to acceptance--rejection as motivation; main MCMC, distribution-comparison, Bayesian, and queueing development |
| Deck 04, Improving Efficiency | `sampling/GeneratingSamples.ipynb`; `sampling/TransportMapsAndAcceptanceRejection.ipynb`; `applications/FinancialOptionPayoffs.ipynb`; `applications/KeisterExample.ipynb`; `sampling/ConditionalMonteCarlo.ipynb`; `performance/AsianOptionVarianceReduction.ipynb`; `performance/Discrepancy.ipynb` | Return to earlier low discrepancy, transport, and option examples; main importance-sampling, variance-reduction, discrepancy, and QMC development |
| Deck 05, Selected Topics | A consolidated gradient/stochastic-gradient notebook and the GPU Monte Carlo notebook, if retained after review; earlier application notebooks when a selected topic extends them | Flexible continuation into selected methods; queueing may recur if it becomes a substantial application, and future MCTS or multilevel notebooks should remain coherent rather than omnibus |

The broad inherited `QMCPy_Introduction.ipynb` has no required deck call. It
should be retained only if it becomes a concise software orientation rather
than a second survey notebook. Likewise, no deck should call a separate
American-option notebook unless optimal stopping is developed computationally.

## Planned notebook specifications

### `sampling/GeneratingSamples.ipynb` — Deck 02, with returns in Deck 04

Keep the existing notebook as the broad executable companion to Deck 02. Its
job is to show direct construction and transformation of IID and low
discrepancy samples, a compact Gaussian-mixture construction, multivariate
Gaussian samples, Brownian motion, geometric Brownian motion, and one
arithmetic-Asian option preview.

Add the Deck 02 Gaussian mixture immediately after the zero-inflated
exponential as a deliberately small section: one explanatory cell for the
component draw and conditional normal draw, followed by one executable cell
with a density-and-sample diagnostic. Match the deck's example:
$p=0.3$, $(\mu_1,\sigma_1)=(-2,0.5)$, and
$(\mu_2,\sigma_2)=(1,1)$. Do not add an extended mixture survey. Instructor
review may trim or clarify other examples. Deck 04 may call the low discrepancy
and option sections again, but this already-full survey notebook should not
absorb transport maps, acceptance--rejection, or MCMC.

### `sampling/TransportMapsAndAcceptanceRejection.ipynb` — Deck 02, with Decks 03–04 returns

**Draft implemented:** Local clean-kernel execution and plots are validated.
The draft includes the inverse-map and density checks, a Beta target
comparison, and quadrature-based marginals and acceptance diagnostics for
the bounded banana. The instructor has approved the notebook; its Colab badge
and Deck 02 links are added. Live-Colab validation and the notebook-page link
remain pending.

Create one focused notebook answering a common question: how can easy proposal
draws become unweighted target samples by moving every draw or by accepting
selected draws? Its preferred sequence is:

1. introduce the recurring \(\operatorname{Beta}(2,1)\) target and
   \(\operatorname{Uniform}(0,1)\) proposal;
2. construct the exact scalar transport \(T(z)=\sqrt z\), verify the
   density--Jacobian identity, and compare transformed samples with the target;
3. develop the triangular flow from Deck 02,
   \(X_1=Z_1\), \(X_2=Z_2+b(Z_1^2-1)\), including its inverse, unit Jacobian
   determinant, density, conditional mean, and sample plot;
4. introduce acceptance--rejection for a possibly unnormalized
   \(\varrho_{\mathrm{tar}}\), using proposal density
   \(\varrho_{\mathrm{prop}}\), acceptance indicator \(W\), and the Bayes'
   theorem derivation from Deck 02;
5. return to the scalar example with \(M=2\), acceptance rule \(U\le Z\),
   acceptance probability \(1/2\), and a direct comparison with transport; and
6. adapt one bounded nonlinear target, its proposal, and its diagnostics from
   the inherited acceptance--rejection notebook; use the existing
   `cl.sampling.accept_reject` implementation rather than copying the
   inherited sampler, then motivate MCMC when no useful map or global envelope
   is available.

For the possibly unnormalized target, define
\(c^{-1}=\int\varrho_{\mathrm{tar}}(x)\,dx\), require
\(\varrho_{\mathrm{tar}}(x)\le
M\varrho_{\mathrm{prop}}(x)\), and accept when
\(U\le\varrho_{\mathrm{tar}}(Z)/
[M\varrho_{\mathrm{prop}}(Z)]\). Then
\(\Prob(W=1)=1/(Mc)\) and the accepted density is
\(c\varrho_{\mathrm{tar}}\); the sampler does not need to know \(c\).

Keep the shared scalar example, one multivariate transport, and one nonlinear
acceptance--rejection example. The triangular-flow target on
\(\mathbb R^2\) and the inherited bounded banana-shaped target are distinct;
name and plot them so students cannot confuse them. Do not teach a catalog of
flow architectures or repeat the full MCMC algorithm. The shared scalar
example already provides the transparent one-dimensional acceptance rule, so
omit the inherited half-normal/exponential example unless instructor review
finds a distinct pedagogical role for it. If the reusable classlib sampler has
a genuine API defect, fix and validate `classlib` through the documented
submodule workflow rather than adding a course-local replacement.

Deck 03 should call back to this notebook rather than repeat the inherited
acceptance--rejection development. Deck 04 may return to the scalar example to
contrast the exact transport with the importance weight \(2z\), while keeping
the full importance-sampling treatment in Deck 04.

### `applications/FinancialOptionPayoffs.ipynb` — Decks 02 and 04

Create a dedicated notebook for discrete risk-neutral geometric-Brownian
paths and payoff definitions. It should contain:

- European call and put payoffs, with Black--Scholes values as benchmarks
  where applicable;
- arithmetic-Asian calls using both right-rectangle and trapezoidal
  approximations to the continuous average;
- lookback call and put payoffs;
- a meaningful pair of discretely monitored barrier options, preferably
  down-and-out and down-and-in calls, together with an in--out parity check
  under the same monitoring convention;
- a small collection of plotted paths annotated by the feature that controls
  each payoff: terminal value, time average, running minimum or maximum, or
  barrier crossing; and
- one final IID-versus-scrambled-Sobol comparison across two or three
  contracts.

Use QMCPy's `FinancialOption` support for European, Asian, lookback, and
barrier contracts so the code matches the Deck 02 notation and conventions.
The notebook should establish reusable path-construction and payoff interfaces
for Deck 04 without teaching all variance-reduction methods here.

Do not include an American put merely as another payoff row. A computational
American option requires an optimal-stopping method, likely Longstaff--Schwartz
regression. If that material is eventually taught, create a separate advanced
`applications/AmericanPutOptimalStopping.ipynb`; otherwise retain only the
conceptual formulation in the slides.

### `sampling/MetropolisHastings.ipynb` — Deck 03

Replace the algorithmic core of the inherited omnibus MCMC notebook with a
transparent NumPy/SciPy implementation. Use one well-defined bimodal or
otherwise challenging target, then examine proposal scale, acceptance rate,
burn-in, trace behavior, autocorrelation, effective sample information, and
multiple chains. Refer back briefly to acceptance--rejection instead of
repeating that notebook.

The purpose is to understand MCMC mechanics, not to survey packages. A common
target may be used later in `BayesianMCMC.ipynb` or `Discrepancy.ipynb` for a
short comparison, provided its definition remains consistent.

### `applications/BayesianMCMC.ipynb` — Deck 03

Use one genuine posterior example to demonstrate a modern sampler and modern
diagnostics. The preferred package choice is PyMC/NUTS with ArviZ if the
dependency and clean-install burden is acceptable. `emcee` is the lighter
fallback, not a second core requirement. Keep the statistical model and
posterior interpretation central; do not make this a package tour.

Langevin MCMC, hand-built Hamiltonian Monte Carlo, and parallel tempering may
be mentioned or developed later if the Deck 03 narrative needs them. They
should not all be accumulated in this notebook. Retain parallel tempering only
as an optional multimodality extension if it contributes more than the chosen
modern sampler.

### `performance/Discrepancy.ipynb` — Decks 03 and 04

Keep discrepancy and maximum mean discrepancy in their own sample-quality
notebook instead of embedding them in the Metropolis notebook. Deck 03 calls
it for comparing empirical and target distributions; Deck 04 may call it for
the integration-error and low-discrepancy interpretations. Preserve that
single teaching purpose even though two decks use it.

### `applications/QueueSimulation.ipynb` — Deck 03, possible Deck 05 return

Modernize the inherited queue quick start as a separate application notebook.
Because the current Deck 03 treats queues as Markov-chain and event-driven
systems, Deck 03 is its current main-development caller. Evaluate SimPy as the
implementation package, possibly through a small course-facing interface, but
do not place queue code in the MCMC notebook. Deck 05 may call and extend the
same queue notebook if queueing becomes a larger selected application during
deck review; that later use does not require moving or renaming it.

### `performance/AsianOptionVarianceReduction.ipynb` — Deck 04, continuing Deck 02

Build this from the variance-reduction portions of the inherited
`AsianOptionExample.ipynb`. Reuse the path and payoff definitions established
for Deck 02, then compare IID and low discrepancy sampling, importance
sampling through drift, a European option as a control variate, and the
combined drift-plus-control method. Keep the performance comparison and its
diagnostics here rather than expanding `GeneratingSamples.ipynb` or
`FinancialOptionPayoffs.ipynb`.

### Deck 05 performance notebooks

Consolidate the inherited gradient and stochastic-gradient variants into one
focused notebook if that material survives Deck 05 review. Keep the GPU Monte
Carlo demonstration separate because hardware, backend, synchronization, and
precision caveats are its principal teaching job. Any future MCTS or
multilevel Monte Carlo notebook should also be independent rather than folded
into either performance notebook.

## Principal Fall 2025 notebooks

### `AcceptanceRejection.ipynb`

- **Status:** The bounded banana target and diagnostics have been adapted into
  the combined transport/acceptance--rejection draft. The new notebook runs
  locally with the `qmcpy` kernel and is instructor-approved. Its Colab badge
  and Deck 02 links are added; live-Colab validation remains pending. The
  inherited sampler and half-normal example were not copied.
- **Source:** `MATH565Fall2025/notebooks/AcceptanceRejection.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/sampling/TransportMapsAndAcceptanceRejection.ipynb`
- **Description:** Supplies the bounded banana-shaped unnormalized target,
  proposal, and diagnostics for the acceptance--rejection half of the combined
  notebook. Use `cl.sampling.accept_reject` rather than copying its inherited
  sampler. The inherited half-normal/exponential example is a reference, not a
  required second scalar development.
- **Dependencies:** NumPy, SciPy, Matplotlib, QMCPy, IPython,
  `classlib.nbviz`, and repository-root path setup. No separate data or image
  input was found.
- **Related versions:** No direct competing version was found in `Old_Stuff`.
  A checkpoint exists only as Jupyter-generated state and is not a migration
  source.
- **Migration concerns:** The Colab badge points to the stale or nonexistent
  `GeneratingRandomVectors.ipynb`. Setup code clones the Fall 2025 repository
  and installs QMCPy from the moving `develop` branch. Replace these
  assumptions and validate every cell from a clean kernel.
- **Classification:** Sampling is unambiguous.

### `AreWeThereYet.ipynb`

- **Status:** Migration and instructor review complete; initialization,
  mathematical content, plots, and clean execution validated in the
  documented course environment. Linked from the course notebook page and
  Introduction slides. The instructor reports successful Colab execution.
- **Source:** `MATH565Fall2025/notebooks/AreWeThereYet.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/applications/AreWeThereYet.ipynb`
- **Description:** Uses a waiting-time model to study Monte Carlo estimation,
  convergence rates, root mean squared error, the central limit theorem,
  unknown variance, confidence intervals, and quantiles.
- **Dependencies:** NumPy, SciPy, Matplotlib, QMCPy, IPython, and
  `classlib.nbviz`. No separate data or image input is required.
- **Related versions:** `Old_Stuff/AreWeThereYet_VerA.ipynb` has the same
  broad structure and cell count but no saved outputs. Treat it as an earlier
  duplicate unless a cell-by-cell review finds a specific correction.
  Several checkpoints have related names but are not primary sources.
- **Migration notes:** Removed stale repository and environment assumptions.
  The notebook follows the current shared initialization pattern
  (`import classlib as cl`, `cl.nbviz.init`, and `cl.nbviz.TOL_BRIGHT`) and
  imports only the packages it uses. The completed example distinguishes
  observed error from RMSE, compares estimates with analytic benchmarks, and
  previews conditional Monte Carlo and randomized Sobol sampling.
- **Classification:** Applications. The waiting-time model is the course's
  introductory illustrative application, even though it also introduces
  convergence and error assessment.

### `AsianOptionExample.ipynb`

- **Status:** Not migrated; split rather than one-for-one migration is now
  recommended.
- **Source:** `MATH565Fall2025/notebooks/AsianOptionExample.ipynb`
- **Proposed targets:** Use its path and basic payoff material when creating
  `MATH565Fall2026/notebooks/applications/FinancialOptionPayoffs.ipynb` for
  Deck 02, and migrate its drift importance sampling and European control
  variate material into
  `MATH565Fall2026/notebooks/performance/AsianOptionVarianceReduction.ipynb`
  for Deck 04.
- **Description:** Prices an arithmetic-mean Asian option and compares
  sampling schemes, importance sampling through drift, and a European option
  as a control variate.
- **Dependencies:** NumPy, SciPy, Matplotlib, QMCPy, IPython,
  `classlib.options.asian`, `classlib.plots`, `classlib.nbviz`, and
  repository-root path setup. No separate data or image input was found.
- **Related versions:** No direct competing notebook was found in
  `Old_Stuff`; the checkpoint is not a migration source.
- **Migration concerns:** The Colab badge incorrectly targets
  `KeisterExample.ipynb`. Confirm the current `classlib` option-pricing API
  and replace stale repository, environment, and nested-path assumptions.
- **Classification:** Split by dominant teaching purpose: Applications for
  payoff construction and Performance for variance reduction.

### `ConditionalMonteCarlo.ipynb`

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/ConditionalMonteCarlo.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/sampling/ConditionalMonteCarlo.ipynb`
- **Description:** Demonstrates conditional Monte Carlo for density
  estimation and compares error measures and sampling schemes.
- **Dependencies:** NumPy, SciPy, Matplotlib, QMCPy, IPython,
  `classlib.distributions`, `classlib.generators`,
  `classlib.options.asian`, `classlib.plots`, `classlib.nbviz`, and
  repository-root path setup.
- **Related versions:** No direct competing version was found. The checkpoint
  is Jupyter-generated state rather than a source candidate.
- **Migration concerns:** The Colab badge incorrectly targets
  `KeisterExample.ipynb`. Review whether the Asian-option helpers and other
  broad imports are used. Confirm current `UniformSumDistribution` and
  `Kronecker` interfaces.
- **Classification:** Conditional Monte Carlo is both a sampling technique
  and a variance-reduction method. Sampling is recommended because the
  conditional sampling construction organizes the notebook.

### `Discrepancy.ipynb`

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/Discrepancy.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/performance/Discrepancy.ipynb`
- **Description:** Compares kernel discrepancy and maximum mean discrepancy
  for several sampling schemes.
- **Dependencies:** NumPy, SciPy, Matplotlib, tqdm, QMCPy,
  `classlib.discrepancy`, `classlib.nbviz`, repository-root discovery, and
  `classlib/classlib/generators/lattice_rules/2exp20_9125dim_new_lattice_rule.txt`.
- **Related versions:** The principal notebook has a checkpoint, but no
  direct competing version was found in `Old_Stuff`.
- **Migration concerns:** The Colab badge points to
  `GeneratingRandomVectors.ipynb`. Verify comments about Kronecker support,
  the lattice-rule path, and current discrepancy and QMCPy APIs. Remove
  fragile repository-root discovery.
- **Classification:** Discrepancy describes sample construction quality and
  could be placed under Sampling. Performance is recommended because the
  notebook uses discrepancy primarily to assess and compare sample quality.

### `GD_SGD_Rosenbrock_Logistic_Timing.ipynb`

- **Status:** Not migrated.
- **Source:**
  `MATH565Fall2025/notebooks/GD_SGD_Rosenbrock_Logistic_Timing.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/performance/GD_SGD_Rosenbrock_Logistic_Timing.ipynb`
- **Description:** Compares gradient descent and stochastic gradient descent
  using Rosenbrock geometry, logistic regression, and large-data timing
  examples.
- **Dependencies:** NumPy and Matplotlib, with optional `classlib.nbviz`
  styling and figure saving. It does not require a separate input dataset.
- **Related versions:** `Old_Stuff` contains
  `GD_SGD_Rosenbrock_Logistic_nbviz.ipynb`,
  `GD_SGD_Rosenbrock_Logistic_Timing_nbviz.ipynb`, and
  `GD_SGD_Rosenbrock_Logistic_Timing_v2_nbviz.ipynb`. These appear to be
  experimental predecessors; the principal notebook is the most complete
  starting point.
- **Migration concerns:** Confirm its role in the final MATH 565 topic
  sequence, make timing comparisons reproducible, and decide whether figures
  saved through `classlib.nbviz` are generated-only or durable assets.
- **Classification:** Performance is recommended. Its optimization content
  is somewhat peripheral to core Monte Carlo sampling, so inclusion in the
  final course remains a curriculum decision.

### `GPU_MonteCarlo_Demo.ipynb`

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/GPU_MonteCarlo_Demo.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/performance/GPU_MonteCarlo_Demo.ipynb`
- **Description:** Compares CPU and GPU Monte Carlo execution, including
  repeated experiments and a batch of many expectations.
- **Dependencies:** NumPy, pandas, Matplotlib, PyTorch, Apple
  `system_profiler`, `pmset`, MPS, and optional CUDA support. Results depend
  materially on available hardware and backend.
- **Related versions:** `Old_Stuff` contains multiple development variants,
  including `GPU_MonteCarlo_Demo Ver B.ipynb`,
  `GPU_MonteCarlo_Demo_Ver A.ipynb`,
  `GPU_MonteCarlo_Demo_with_sync_and_cuda.ipynb`, and several
  many-expectation variants. The principal notebook incorporates much of this
  work, but synchronization logic should be compared before migration.
- **Migration concerns:** Add clear CPU fallbacks and expected-result
  guidance, distinguish algorithmic conclusions from machine-specific
  timings, and test on CPU, MPS, and CUDA where available. Avoid presenting
  one machine's timings as portable results.
- **Classification:** Performance is unambiguous.

### `GeneratingSamples.ipynb`

- **Status:** Migration complete. Modernized initialization and current QMCPy
  APIs, clean execution, and saved outputs have been validated. The notebook
  is linked from the course notebook page and Deck 02. Instructor review is
  still pending. The compact Deck 02 Gaussian-mixture section is now included
  after the zero-inflated exponential. The low discrepancy section compares
  IID and randomized Sobol' mixture samples using maximum CDF error across
  32 independent repetitions. The full notebook executes cleanly
  with the local `qmcpy` kernel. The instructor reports successful Colab
  execution.
- **Source:** `MATH565Fall2025/notebooks/GeneratingSamples.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/sampling/GeneratingSamples.ipynb`
- **Description:** Covers IID binomial samples, a zero-inflated exponential
  model, multivariate normal sampling, Gaussian processes, Brownian motion,
  stock prices, option pricing, and low discrepancy sampling.
- **Dependencies:** NumPy, SciPy, statsmodels, Matplotlib, QMCPy,
  `classlib.distributions`, `classlib.plots`, and `classlib.nbviz`. No
  separate input data or repository-root path setup is required.
- **Related versions:** `Old_Stuff` contains `GeneratingSamples_Ver.ipynb`,
  `GeneratingSamples_Ver_A.ipynb`, and `GeneratingSamples_Ver_B.ipynb`.
  These appear to be predecessors. Use the principal notebook unless a
  focused comparison finds a correction worth carrying forward.
- **Migration notes:** Removed stale Colab, Fall 2025, path-discovery, and
  moving-branch installation code. Current QMCPy `Gaussian`,
  `ZeroInflatedExpUniform`, `BrownianMotion`, `GeometricBrownianMotion`, and
  `FinancialOption` abstractions replace hand-built transformations and the
  duplicate Asian-option payoff. Samples intentionally have no fixed seeds so
  students see different realizations when they rerun the simulation.
- **Classification:** Sampling is unambiguous, although several examples are
  application-oriented.

### `KeisterExample.ipynb`

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/KeisterExample.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/applications/KeisterExample.ipynb`
- **Description:** Introduces the Keister integration problem, variable
  transformations, and accuracy comparisons.
- **Dependencies:** NumPy, SciPy, Matplotlib, QMCPy, IPython,
  `classlib.plots`, `classlib.nbviz`, and repository-root path setup. No
  external data or image input was found.
- **Related versions:** No direct competing version was found; its checkpoint
  is not a migration source.
- **Migration concerns:** Replace Fall 2025 environment and path assumptions,
  verify plotting helpers, and validate transformations and accuracy results
  with the pinned QMCPy revision.
- **Classification:** Applications is recommended because the Keister
  integral is the organizing example. It could also support Performance
  because it compares accuracy.

### `MarkovChainMonteCarlo.ipynb`

- **Status:** Not migrated; split rather than one-for-one migration is now
  recommended.
- **Source:** `MATH565Fall2025/notebooks/MarkovChainMonteCarlo.ipynb`
- **Proposed targets:** Use the Metropolis material in
  `MATH565Fall2026/notebooks/sampling/MetropolisHastings.ipynb`, the Bayesian
  material as a starting point for
  `MATH565Fall2026/notebooks/applications/BayesianMCMC.ipynb`, and the sample
  comparison material only where it supports
  `MATH565Fall2026/notebooks/performance/Discrepancy.ipynb`.
- **Description:** Connects acceptance-rejection sampling, Metropolis
  sampling, maximum mean discrepancy, Bayesian inference, random-walk
  Metropolis, and parallel tempering.
- **Dependencies:** NumPy, Matplotlib, IPython, `classlib.sampling`,
  `classlib.discrepancy`, `classlib.nbviz`, and repository-root path setup.
- **Related versions:** No direct competing principal version was found.
  Checkpoints are not migration sources.
- **Migration concerns:** Colab setup installs QMCPy but does not directly
  install `classlib`, despite relying heavily on it. Confirm sampling and
  discrepancy APIs, then update repository-root and environment logic. Avoid
  repeating the inherited acceptance--rejection development, and treat
  parallel tempering as an optional multimodality extension rather than part
  of the basic Metropolis notebook.
- **Classification:** Split among Sampling, Applications, and Performance by
  the principal teaching purpose of each new notebook.

### `QMCPy_Introduction.ipynb`

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/QMCPy_Introduction.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/sampling/QMCPy_Introduction.ipynb`
- **Description:** Provides a broad hands-on tour of QMCPy discrete
  distributions, low discrepancy projections, true measures, integrands,
  stopping criteria, and financial-option examples.
- **Dependencies:** NumPy, SciPy, pandas, Matplotlib, tqdm, QMCPy, `classlib`,
  IPython, and LaTeX support. It writes a `QMCPy_Intro_figures` directory.
- **Related versions:** A checkpoint named
  `QMCPy_IntroductionOOPs-checkpoint.ipynb` exists, but checkpoints are
  excluded and it should not become a source without a specific reason.
- **Migration concerns:** Colab setup installs QMCPy from `develop` and
  `classlib` from remote `main`. Review current QMCPy APIs, figure and output
  policy, execution time, saved outputs, and reproducibility.
- **Classification:** Sampling is recommended because the notebook primarily
  introduces QMCPy's sampling abstractions, despite also covering
  applications and stopping criteria.

### `SGD_Rosenbrock_nbviz.ipynb`

- **Status:** Not migrated; consolidation decision pending.
- **Source:** `MATH565Fall2025/notebooks/SGD_Rosenbrock_nbviz.ipynb`
- **Proposed target, if retained:**
  `MATH565Fall2026/notebooks/performance/SGD_Rosenbrock_nbviz.ipynb`
- **Description:** Gives a smaller demonstration of gradient descent and
  stochastic coordinate updates on the Rosenbrock function.
- **Dependencies:** NumPy, Matplotlib, and optional `classlib.nbviz`.
- **Related versions:** Its content overlaps substantially with
  `GD_SGD_Rosenbrock_Logistic_Timing.ipynb` and the gradient-descent variants
  under `Old_Stuff`.
- **Migration concerns:** Migrating both principal gradient-descent notebooks
  would likely duplicate material and maintenance effort.
- **Classification:** Performance is appropriate if it remains independent.
- **Recommendation:** Do not migrate it separately by default. During
  migration of `GD_SGD_Rosenbrock_Logistic_Timing.ipynb`, identify any
  uniquely useful explanation or visualization here and merge only that
  material into the broader notebook.

### `TemplateNotebook.ipynb`

- **Status:** Not migrated; retirement or replacement recommended.
- **Source:** `MATH565Fall2025/notebooks/TemplateNotebook.ipynb`
- **Proposed target:** None as student-facing content. If a maintained author
  template is later required, design it separately for Fall 2026 rather than
  treating this file as course material.
- **Description:** A placeholder authoring template with generic headings,
  setup, and imports rather than substantive MATH 565 content.
- **Dependencies:** NumPy, SciPy, Matplotlib, QMCPy, IPython,
  repository-root setup, and an obsolete direct `nbviz` import.
- **Related versions:** A checkpoint exists but is not a migration source.
- **Migration concerns:** It contains Fall 2025 setup and repository
  assumptions and should not appear on the student-facing notebook page.
- **Classification:** None; it is authoring infrastructure, not Sampling,
  Applications, or Performance content.
- **Recommendation:** Retire it in its current form. If an author template is
  needed, create and validate a new Fall 2026 template as a separate task.

### `queuesim_quick_start.ipynb`

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/queuesim_quick_start.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/applications/QueueSimulation.ipynb`
- **Description:** Demonstrates a single-server exponential/uniform queue and
  a drive-through model with downstream blocking.
- **Dependencies:** NumPy, SciPy, Matplotlib, QMCPy, IPython,
  `classlib.queuesim`, `classlib.nbviz`, and repository-root setup.
- **Related versions:** `Old_Stuff/QueueEventSim.ipynb` and
  `Old_Stuff/drive_thru_tandem_blocking.ipynb` are earlier specialized
  examples. Use them only to recover a demonstrated feature or correction
  absent from the principal quick-start notebook. Related checkpoints are not
  primary sources.
- **Migration concerns:** The Colab link misspells the notebook as
  `quesim_quick_start.ipynb`. Confirm the current `classlib.queuesim` API,
  replace the direct `Path.cwd().parent` assumption, and evaluate SimPy as the
  modern implementation package without coupling queue code to the MCMC
  notebook.
- **Classification:** Applications is recommended because queueing systems
  are the organizing models, although the notebook also illustrates
  simulation construction.

## Cross-cutting migration findings

### Nested paths

Several notebooks assume that they live directly under `notebooks/` and use
`Path.cwd().parent` to locate the repository. That will fail under
`notebooks/sampling/`, `notebooks/applications/`, and
`notebooks/performance/`. Establish one tested repository-root discovery
pattern before migrating the first notebook.

### Colab, repository, and dependency links

Many notebooks contain one or more of the following:

- links to the Fall 2025 repository;
- Colab badges targeting another, missing, or misspelled notebook;
- commands that clone the Fall 2025 repository;
- installation of QMCPy from the moving `develop` branch;
- installation of `classlib` from a moving remote branch.

Replace these with Fall 2026 links and the documented course dependency
workflow. Do not publish a Colab badge until its complete setup has been
tested. A Colab setup must clone the current course repository, initialize
only the recorded `classlib` and `qmcpy` submodules through their public HTTPS
URLs, and install those exact checkouts. Do not substitute PyPI releases or a
moving QMCPy `develop` branch: the course may temporarily rely on pinned
QMCPy work or teaching support in `classlib.nbviz` before the corresponding
upstream feature is merged. Keep the setup conditional on Colab and do not
change the notebook's working directory.

### Packages and APIs

The common stack includes NumPy, SciPy, Matplotlib, pandas, statsmodels, tqdm,
IPython, QMCPy, and `classlib`. The GPU notebook additionally requires
PyTorch and platform-specific capabilities. Confirm imported `classlib` and
QMCPy APIs against the pinned submodules rather than relying on moving remote
branches.

### Initialization cells

Modernize each migrated notebook's initialization cell using the current
`classlib` namespace pattern established in `AreWeThereYet.ipynb`. Import the
package once as `cl`, initialize notebook visualization through `cl.nbviz`,
and access other shared modules through the same namespace. A typical minimal
initialization is:

```python
import numpy as np
import matplotlib.pyplot as plt
import classlib as cl

%matplotlib inline

cl.nbviz.init(use_tex=True)
colors = cl.nbviz.TOL_BRIGHT
```

Add SciPy, QMCPy, IPython display helpers, or other packages only when the
notebook actually uses them. Likewise, call `cl.nbviz.configure(...)` only
when the notebook intentionally saves figures. Replace legacy aliases such as
`import classlib.nbviz as nb` and update calls to `cl.nbviz.<name>`; use
namespaced helpers such as `cl.distributions.<name>` where appropriate.
Remove unused imports, constants, duplicated setup, `sys.path` manipulation,
and working-directory-based repository discovery. The repository's documented
editable installation makes `classlib` available without notebook-local path
injection.

### New notebooks created from scratch

The migration guidance above also establishes the baseline for new MATH 565
notebooks, but a new notebook should begin cleanly rather than copying legacy
setup from a migrated file. Place it directly in the appropriate
`notebooks/sampling/`, `notebooks/applications/`, or
`notebooks/performance/` directory and select the course `qmcpy` Jupyter
kernel. Start with a Markdown title and short statement of purpose, followed
by one initialization cell based on this template:

```python
import numpy as np
import matplotlib.pyplot as plt
import classlib as cl

%matplotlib inline

cl.nbviz.init(use_tex=True)
colors = cl.nbviz.TOL_BRIGHT
```

Treat this as a starting template, not a mandatory list of imports. Remove
NumPy or Matplotlib if the notebook does not use them, and add dependencies
only where the notebook needs them. Common additions include:

```python
import scipy.stats as stats
import qmcpy as qp
from IPython.display import display, Markdown
```

For reproducible pseudo-random examples, create an explicit generator with a
documented seed, for example `rng = np.random.default_rng(2026)`, and use that
generator consistently when the relevant APIs support it. If the notebook
deliberately writes figures, add an explicit configuration with a
notebook-specific path:

```python
cl.nbviz.configure(
    figpath="_figures/notebook_name",
    savefigs=True,
    imgfrmt="png",
)
```

For local Jupyter use, do not add unconditional package-install commands,
repository cloning, `sys.path` changes, or working-directory discovery to a
new notebook. Its dependencies come from the documented repository setup. A
notebook intentionally published for Colab may place the tested conditional
setup described above before its import cell; that setup must be a no-op in
the local `qmcpy` environment. Before adding the notebook to
`pages/notebooks.qmd`, restart the kernel, run all cells in order, inspect the
results and runtime, and confirm that any generated files follow the
repository output policy.

### Data, images, and generated files

No principal notebook was found to read a separate course image or tabular
data file. Notable non-notebook resources and generated artifacts are:

- the `classlib` lattice-rule text file used by `Discrepancy.ipynb`;
- figures saved through `classlib.nbviz` by gradient-descent notebooks;
- the `QMCPy_Intro_figures` directory written by
  `QMCPy_Introduction.ipynb`.

Decide the generated-output policy for each notebook before publication.

### Saved outputs and clean execution

Most principal notebooks contain saved outputs. Each migrated notebook should
be restarted and run from a clean kernel, checked for deterministic or
appropriately qualified results, and reviewed for excessive output size,
execution time, warnings, and hidden state.

## Recommended migration and validation order

Proceed by deck so each notebook is shaped by the reviewed lecture narrative,
not by the accidental boundaries of the inherited files.

1. Colab execution of `applications/AreWeThereYet.ipynb` and
   `sampling/GeneratingSamples.ipynb` is confirmed by the instructor.
2. Complete instructor review of the implemented Gaussian-mixture section
   and IID/Sobol' comparison in `sampling/GeneratingSamples.ipynb`.
3. Validate the instructor-approved
   `sampling/TransportMapsAndAcceptanceRejection.ipynb` in clean Colab; its
   local execution and Deck 02 links are already checked.
4. Create and validate `applications/FinancialOptionPayoffs.ipynb`, drawing
   only the basic path and payoff material needed from the inherited Asian
   option notebook.
5. Complete instructor review of the retained Deck 02 companions, add the
   validated notebook calls, and give that stage of the deck--notebook sequence
   its initial polish. Later decks may add further calls or motivate revisions
   without changing notebook identity merely to match a deck boundary.
6. Review Deck 03, then create or migrate `sampling/MetropolisHastings.ipynb`,
   `applications/BayesianMCMC.ipynb`, `performance/Discrepancy.ipynb`, and
   `applications/QueueSimulation.ipynb` in the order established by that
   review.
7. During Deck 04 review, migrate `applications/KeisterExample.ipynb` and
   `sampling/ConditionalMonteCarlo.ipynb`, then create
   `performance/AsianOptionVarianceReduction.ipynb` from the retained
   variance-reduction parts of the inherited Asian notebook.
8. During Deck 05 review, consolidate the gradient/stochastic-gradient
   variants and decide whether to migrate the separate GPU notebook.
9. Reconsider the broad `QMCPy_Introduction.ipynb` only after the focused
   course notebook family exists; omit it if it would duplicate the survey
   role of `GeneratingSamples.ipynb`.

Do not migrate `TemplateNotebook.ipynb` as student-facing content. Before the
Deck 05 gradient notebook is created, review `SGD_Rosenbrock_nbviz.ipynb` for
unique material to merge rather than publishing overlapping versions.

For each migrated notebook:

1. Create or confirm its category directory.
2. Preserve mathematical and pedagogical intent while removing obsolete
   semester-specific material.
3. Replace fragile working-directory and repository-root assumptions.
4. Update Fall 2025, Colab, repository, and dependency links.
5. Modernize the initialization cell according to the convention above and
   confirm all imported `classlib` and QMCPy APIs against pinned submodules.
6. Remove unused imports and duplicated setup.
7. Decide how generated figures and other output files are handled.
8. Restart the kernel and run all cells in order in the documented course
   environment.
9. Review correctness, warnings, runtime, saved outputs, and file size.
10. Verify download and execution from a clean clone.
11. Add the link to `pages/notebooks.qmd` only after validation succeeds.
12. Update the notebook's status here and preserve completed history in
    `STATUS.md`.

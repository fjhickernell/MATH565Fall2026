# MATH 565 Notebook Inventory and Migration Plan

## Purpose and scope

This document is the durable project memory for migrating Jupyter notebooks
from the read-only MATH 565 Fall 2025 course-material reference into the
authoritative MATH 565 Fall 2026 repository. It records what each principal
notebook does, where it should go, what it depends on, and what must be
resolved before publication.

The inventory covers the 14 `.ipynb` files directly under
`MATH565Fall2025/notebooks/`. It excludes `.ipynb_checkpoints`, temporary
files, and virtual documents as primary sources. Related files in
`Old_Stuff` and `.ipynb_checkpoints` are noted only when they clarify
duplication, provenance, or a possible alternative version.

No notebook was copied, moved, renamed, or edited while preparing this
inventory.

## Repository boundaries

- `MATH565Fall2026` is the authoritative writable repository.
- `MATH565Fall2025` is the read-only course-material reference.
- `MATH563Spring2026` is the read-only architecture reference.
- `classlib` is writable only for genuinely reusable shared infrastructure.
- `qmcsoftware` and its pinned submodule pointer are read-only.

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

## Principal Fall 2025 notebooks

### `AcceptanceRejection.ipynb`

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/AcceptanceRejection.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/sampling/AcceptanceRejection.ipynb`
- **Description:** Demonstrates acceptance-rejection sampling, including
  normal sampling with an exponential proposal and a banana-shaped
  unnormalized density.
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

- **Status:** Migrated for instructor review; initialization modernized and
  automated execution validated in the documented course environment.
- **Source:** `MATH565Fall2025/notebooks/AreWeThereYet.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/applications/AreWeThereYet.ipynb`
- **Description:** Uses a waiting-time model to study Monte Carlo estimation,
  convergence rates, root mean squared error, the central limit theorem,
  unknown variance, confidence intervals, and quantiles.
- **Dependencies:** NumPy, SciPy, Matplotlib, QMCPy, IPython,
  `classlib.nbviz`, `classlib.distributions.make_zie`, and repository-root
  path setup. No separate data or image input was found.
- **Related versions:** `Old_Stuff/AreWeThereYet_VerA.ipynb` has the same
  broad structure and cell count but no saved outputs. Treat it as an earlier
  duplicate unless a cell-by-cell review finds a specific correction.
  Several checkpoints have related names but are not primary sources.
- **Migration notes:** Removed the stale Fall 2025 Colab bootstrap and fragile
  repository-path injection. The notebook now follows the current shared
  initialization pattern (`import classlib as cl`, `cl.nbviz.init`, and
  `cl.nbviz.TOL_BRIGHT`) and imports only the packages it uses. The
  zero-inflated exponential example and the notebook's mathematical and
  pedagogical details still require careful instructor review before the
  notebook is linked from the course website.
- **Classification:** Applications. The waiting-time model is the course's
  introductory illustrative application, even though it also introduces
  convergence and error assessment.

### `AsianOptionExample.ipynb`

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/AsianOptionExample.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/applications/AsianOptionExample.ipynb`
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
- **Classification:** Applications is recommended because option pricing is
  the organizing problem, although the notebook also teaches performance
  improvements.

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

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/GeneratingSamples.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/sampling/GeneratingSamples.ipynb`
- **Description:** Covers IID binomial samples, a zero-inflated exponential
  model, multivariate normal sampling, Gaussian processes, Brownian motion,
  stock prices, option pricing, and low-discrepancy sampling.
- **Dependencies:** NumPy, SciPy, statsmodels, Matplotlib, QMCPy, IPython,
  `classlib.distributions`, `classlib.plots`, `classlib.nbviz`, and
  repository-root path setup. No separate input data was found.
- **Related versions:** `Old_Stuff` contains `GeneratingSamples_Ver.ipynb`,
  `GeneratingSamples_Ver_A.ipynb`, and `GeneratingSamples_Ver_B.ipynb`.
  These appear to be predecessors. Use the principal notebook unless a
  focused comparison finds a correction worth carrying forward.
- **Migration concerns:** Colab and setup code refer to Fall 2025 and QMCPy
  `develop`. The notebook is broad and relatively large; migrate it after
  smaller sampling notebooks establish the Fall 2026 conventions.
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

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/MarkovChainMonteCarlo.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/sampling/MarkovChainMonteCarlo.ipynb`
- **Description:** Connects acceptance-rejection sampling, Metropolis
  sampling, maximum mean discrepancy, Bayesian inference, random-walk
  Metropolis, and parallel tempering.
- **Dependencies:** NumPy, Matplotlib, IPython, `classlib.sampling`,
  `classlib.discrepancy`, `classlib.nbviz`, and repository-root path setup.
- **Related versions:** No direct competing principal version was found.
  Checkpoints are not migration sources.
- **Migration concerns:** Colab setup installs QMCPy but does not directly
  install `classlib`, despite relying heavily on it. Confirm sampling and
  discrepancy APIs, then update repository-root and environment logic.
- **Classification:** Sampling is unambiguous.

### `QMCPy_Introduction.ipynb`

- **Status:** Not migrated.
- **Source:** `MATH565Fall2025/notebooks/QMCPy_Introduction.ipynb`
- **Proposed target:**
  `MATH565Fall2026/notebooks/sampling/QMCPy_Introduction.ipynb`
- **Description:** Provides a broad hands-on tour of QMCPy discrete
  distributions, low-discrepancy projections, true measures, integrands,
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
  `MATH565Fall2026/notebooks/applications/queuesim_quick_start.ipynb`
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
  `quesim_quick_start.ipynb`. Confirm the current `classlib.queuesim` API and
  replace the direct `Path.cwd().parent` assumption.
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
tested.

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

Do not add package-install commands, repository cloning, `sys.path` changes,
or working-directory discovery to a new notebook. Its dependencies come from
the documented repository setup. Before adding it to `pages/notebooks.qmd`,
restart the kernel, run all cells in order, inspect the results and runtime,
and confirm that any generated files follow the repository output policy.

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

The sequence begins with focused notebooks having relatively few
platform-specific requirements and progresses toward broader, more tightly
coupled, or hardware-dependent material.

1. `KeisterExample.ipynb`
2. `AcceptanceRejection.ipynb`
3. `AreWeThereYet.ipynb`
4. `ConditionalMonteCarlo.ipynb`
5. `AsianOptionExample.ipynb`
6. `GeneratingSamples.ipynb`
7. `Discrepancy.ipynb`
8. `MarkovChainMonteCarlo.ipynb`
9. `QMCPy_Introduction.ipynb`
10. `queuesim_quick_start.ipynb`
11. `GD_SGD_Rosenbrock_Logistic_Timing.ipynb`
12. `GPU_MonteCarlo_Demo.ipynb`

Before step 11, review `SGD_Rosenbrock_nbviz.ipynb` for unique material to
merge into the broader gradient-descent notebook. Do not migrate
`TemplateNotebook.ipynb` as student-facing content.

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

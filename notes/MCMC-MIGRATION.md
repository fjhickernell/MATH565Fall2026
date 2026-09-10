# MCMC notebook migration

## Scope and source map

All substantive non-queueing material from the read-only 2025
`notebooks/MarkovChainMonteCarlo.ipynb` is retained. Cell indices below are
zero-based. The separate `queuesim_quick_start.ipynb` is now migrated to
`applications/QueueSimulation.ipynb` using SimPy.

| 2025 material | 2026 destination |
|:---|:---|
| Setup and elapsed time | Each notebook’s course bootstrap and final runtime cell |
| Cells 5–8: bounded banana and acceptance--rejection | Existing `sampling/TransportMapsAndAcceptanceRejection.ipynb`; direct comparison with Metropolis in `sampling/MetropolisHastings.ipynb` |
| Cells 9–12: random-walk Metropolis and proposal scales | `sampling/MetropolisHastings.ipynb`, followed by separated-mode experiments |
| Cells 13–21: empirical and off-diagonal MMD | `performance/Discrepancy.ipynb` |
| Cells 22–30: frequentist interval, mixture prior, posterior, and Metropolis | `applications/BayesianMCMC.ipynb` |
| Cells 31–33: parallel tempering and interpretation | Primary development after trapping in `sampling/MetropolisHastings.ipynb`; posterior application in `applications/BayesianMCMC.ipynb` |

Shared course-specific functions live in `notebooks/mcmc_examples.py`.
Acceptance--rejection uses the pinned `qmcpy.AcceptanceRejection` already taught,
with the identical bounded target. Its density integral is computed by
quadrature. Expected proposal cost is distinguished from an observed count,
which that API does not expose. No historical repository was modified.

The scalar Metropolis experiments use 120,000 stored states per run, including
the initial state, with separated-mode distance 10 and 1,500 burn-in states.
The five-replica tempering comparison therefore uses 600,000 target evaluations
for each method. Saved notebook outputs were regenerated end to end at these
settings; the separate bounded-banana comparison retains its existing settings.

## Mathematical corrections and additions

- Correct the Gaussian prior’s missing negative exponent signs.
- Use whole-target tempering consistently in the target definitions, local
  updates, and joint-density swap ratio. Likelihood-only tempering is a
  different construction and must not use the whole-posterior swap ratio.
- Retain repeated states on Metropolis rejection. Compare tempering and a
  plain chain at equal target-evaluation budgets, including initialization.
- Display consecutive-repeat counts, transition denominators, and percentages
  in the Metropolis notebook's banana, mixture, proposal-scale, independence-MH,
  and tempering comparisons. Ordinary MH acceptance and repeats use all `n-1`
  transitions; the tempering comparison counts pairs within retained samples.
  Explain the continuous-proposal identity (repeat rate = 1 - acceptance rate),
  why repeats retain their weights, and why cold-slot swaps require direct counts.
- Derive the exact Gaussian-mixture posterior for a sampling benchmark.
  Preserve confidence-interval versus credible-interval interpretations.
- Correct the inherited MMD summation indices and explain the IID conditions
  for unbiasedness of the off-diagonal formula. Dependent chain samples still
  define a valid empirical MMD, but do not satisfy that unbiasedness argument.
- Add multiple starts, region occupation, limited autocorrelation diagnostics,
  and an empirical RKHS witness; none is a standalone convergence certificate.

## Discrepancy reference and interpretation

Current instructor-selected settings are 1,000 candidate states, 10,000
independent AR reference points, and 1,000 burn-in states. Exact blocked kernel
sums limit memory; cached reference self-sums avoid repeating that work for each
candidate. Dense-versus-blocked numerical checks agree. The reference uses
separate AR draws, never the candidate sample itself. Repeated Metropolis states
retain their weights even though a scatter plot can hide their multiplicities.
Do not infer an optimal proposal scale from one realization. Timing comparisons
are not part of the banana exercise.

## External Bayesian notebook

The course-owned Bayesian notebook links the official
[PyMC API quickstart](https://www.pymc.io/projects/examples/en/latest/introductory/api_quickstart.html)
as an optional modern-software supplement. PyMC is not required for the core
notebook and its external example has not been executed as part of local course
validation. ArviZ is required for diagnostics; Colab installs it explicitly,
and conversion supports both 0.x keyword groups and 1.x nested data groups.
Local validation used ArviZ 1.1.0.

## Validation and publication state

All four Deck 03 companions execute end to end in separate clean local `qmcpy`
kernels without warnings. The queue notebook has saved outputs and four inspected
figures; reruns of the three existing companions were saved only to temporary
validation copies to preserve the instructor’s current outputs. Independent numerical
checks cover the bounded-target integral and mean, rejected-state retention,
joint-density swap algebra and state exchange, kernel identities, and exact
posterior normalization. Instructor content review remains pending. Deck 03 and
the notebook page link all four companions, with sources and helpers included
in the same checkpoint. The instructor accepts the established Colab setup without
separate clean-Colab validation and will address problems when they arise. Keep
both helpers published with the notebooks. The queue companion and its links are
ready for instructor review.

## Queueing companion

`applications/QueueSimulation.ipynb` retains the single-server exponential-arrival,
uniform-service model and two-stage drive-through with blocking after service.
SimPy 4.1.2 supplies event scheduling and FCFS resources; `queue_examples.py`
contains the course-owned customer process and measurement code. No shared
`classlib` or pinned QMCPy code was changed. The existing `classlib.queuesim`
implementation remains available to other consumers, but is not used here.

The notebook explains event-driven simulation versus MCMC, residual service
state, traffic intensity, time averages versus completed-customer averages,
startup and endpoint effects, and the exact finite-run residence-time identity.
It adds an M/G/1 stationary benchmark, independent replications, and a coupled
pickup-capacity comparison. Horizon stops exclude events at the endpoint;
departure stops include the requested departure. Busy time is clipped at the
horizon, and order-window blocking is measured separately from service.

Eight deterministic tests check an independent Lindley recursion, hand-calculated
blocking paths at three capacities, resource conservation, truncated service,
empty runs, both stopping rules, and input checks. Run them with
`python -m unittest discover -s tests -p 'test_queue_examples.py'` in `qmcpy`.
The queue slides now distinguish full interarrival and service draws from
residual times and sample service only when a customer starts service.

Bayesian notebook preparation also includes the instructor-requested explanation
of simulated data, prior information, posterior weights, credible intervals,
frequentist versus Bayesian interpretations, and diffuse-prior behavior. Existing
saved Bayesian outputs were preserved during these explanatory edits.

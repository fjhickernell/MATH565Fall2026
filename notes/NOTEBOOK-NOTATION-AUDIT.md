# Final companion notation audit — September 30, 2026

All nine Decks 02–04 companions were checked against the final Deck 04
refinements: uniform inputs U, proposal/source Z, target X, scalar output
Y=f(X), a general map T with correction w_T, exact transport with w_T=1,
importance contributions g_IS, exact-transport contributions g_ET, cube
integrands h, and lowercase var. Locally defined application symbols and
conditional contributions remain where their meanings are explicit.

| Companion | Final follow-up result |
|:--|:--|
| GeneratingSamples | Uniform, source-normal, target, and payoff roles agree; no further change needed |
| TransportMapsAndAcceptanceRejection | Identify exact-transport g_ET and w_T=1, contrast the Beta importance g_IS, lowercase cov |
| MetropolisHastings | Lowercase var; repair the literal tab in tau_f and the aligned equation break |
| BayesianMCMC | Use observed D consistently in likelihood/posterior formulas and the observation-axis label; document the code's data/ybar names |
| Discrepancy | Target-space nodes and empirical/population distinction agree; no further change needed |
| QueueSimulation | Event states, full durations, and customer times retain their distinct roles; no further change needed |
| AreWeThereYet | Lowercase var; travel time T and conditional g(W_2) are locally defined application quantities |
| KeisterExample | Identify g_a as the scale-indexed importance contribution g_IS,a, distinguish proposal map S_a from exact target transport, retain cube h_a |
| AsianOptionVarianceReduction | Label g_IS, identify the correction and composed cube integrand, and identify the zero-drift exact transport |

Generic g remains valid for controls and conditional expectations. A Python
API parameter named g need not be renamed to h: the surrounding explanation
identifies the function's mathematical role. The Asian-option maturity T is
a scalar time, distinct from a bold vector-valued map.

## Executable stopping examples

Keister owns the method comparison: CubMCCLT, CubQMCRepStudentT, and
CubQMCNetG at absolute tolerance 0.005. The validated seed used 551,911,
8,192, and 2,048 total samples, respectively. An intentionally tight 8,192
sample budget at tolerance 1e-7 reports **not met**. The radial reference is
used only after stopping. Replication intervals are approximate and their
nominal coverage is not guaranteed under adaptive stopping. Walsh bounds
assume the stated function cone; passing necessary checks is not proof of
membership.

The Asian-option example keeps a separately fitted control coefficient
fixed. At price tolerance 0.10, its saved estimate is about 7.66398 with
reported interval radius 0.07261, using 16,384 main samples plus 16,384 pilot
samples. Accuracy concerns simulation of the fixed 13-date payoff, not model
or discretization error. The planned constructions notebook should link these
examples rather than repeat them.

## Validation

- All nine notebooks executed in fresh qmcpy kernels with the recorded
  course qmcpy and classlib checkouts supplied on PYTHONPATH; no error outputs.
- Reviewed the 61 generated figures, including the new stopping comparison
  and revised Bayesian observed-data label. Preserved pre-existing outputs
  for Markdown-only edits and unrelated Bayesian simulation cells.
- Deck 04 and the notebook page render locally. The new continuation fits
  and has both direct notebook-section links. Instructor content review and
  publication remain part of the ordinary Deck 04 review and Checkpoint.

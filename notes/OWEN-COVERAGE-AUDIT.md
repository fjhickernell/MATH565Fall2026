# Owen reading coverage through MCMC

Audited September 10, 2026 against the seven current course notebooks and
Decks 01–03. This is a reading map, not an assignment or a claim that every
section of a cited chapter is taught. Notebook computations and saved outputs
are unchanged.

## Title-slide references

| Deck | Reading shown | Reason for the revision |
|:--|:--|:--|
| 01 Introduction | Owen 1–2 and 8; sampling previews 10, 15, 17 | Conditioning is now developed; the sampling-design slides and travel notebook preview orthogonal arrays and randomized Sobol' sampling |
| 02 Generating Samples | Owen 3–6 and 15–17 | Retain direct sampling and processes; add the low discrepancy, lattice, randomization, and Asian-option connections |
| 03 MCMC | Selected topics from Owen 6, 8, 11, 15; Hickernell–Kirk–Sorokin Section 5 | Include process simulation, common random numbers, MCMC, and discrepancy; give the kernel treatment its own reference |

## Notebook-by-notebook evidence

| Notebook | Relevant Owen reading | Scope and supplements |
|:--|:--|:--|
| `applications/AreWeThereYet.ipynb` | 1–2; 4.1–4.2, 4.9 for input construction; 8.7; 15.1, 15.7; 17.1–17.2, 17.6 | Monte Carlo error, travel-time quantiles, conditional mean/density estimation, and independent randomized-Sobol' replications. Input construction is developed in Deck 02, rather than adding every prerequisite to Deck 01's title |
| `sampling/GeneratingSamples.ipynb` | 3–6; 15–17, especially 17.9 | Binomial, zero-inflated exponential, mixture, multivariate Gaussian, Brownian/GBM, Asian and lookback examples; code explicitly compares IID, Sobol', lattice, and Halton designs |
| `sampling/TransportMapsAndAcceptanceRejection.ipynb` | 4.1, 4.6–4.7; 5.1 | Inversion, transformations, rejection, and a bivariate triangular map. The modern transport/flow framing and QMCPy API are course supplements. Importance sampling is only a later connection, not a reason to add Chapter 9 here |
| `sampling/MetropolisHastings.ipynb` | 11.1–11.6, 11.10–11.13; 4.7 as a callback | Target invariance, random-walk and independence proposals, repeated states, burn-in, dependence and diagnostics; parallel tempering is supplemental |
| `applications/BayesianMCMC.ipynb` | 11.1, 11.4–11.5, 11.10–11.12 | Mixture-prior posterior benchmark, multiple starts, ArviZ and whole-posterior tempering. The inference interpretation, conjugate algebra, and software are supplemental; this is not a Gibbs notebook |
| `performance/Discrepancy.ipynb` | 15.2–15.4 as discrepancy/error background | Empirical kernel MMD, off-diagonal estimates, a witness function, and finite-reference uncertainty. Hickernell–Kirk–Sorokin Section 5 is the direct kernel/error supplement; Owen is not presented as the source of the full two-sample MMD treatment |
| `applications/QueueSimulation.ipynb` | 6.1, 6.8 as process background; 8.6 for common random numbers; 2 for independent replication summaries | M/U/1 and tandem blocking, residual times, finite-run accounting, and capacity comparisons using identical input draws. Owen's process chapter is background, not a source for all these non-exponential-service models; retain the notebook's SimPy and queueing references |

## Boundaries of the reading map

- Chapter 12 is Gibbs sampling. Neither the current MCMC deck nor its
  companions develops Gibbs or slice sampling, so remove the inherited
  blanket 11–12 title reference.
- Owen lists Chapter 13 as in progress, without a downloadable chapter.
  Do not cite it as available tempering reading. The online overview also
  contains inconsistent provisional descriptions of later MCMC chapters;
  use the available chapters rather than inferring contents from placeholders.
- Chapter 10 is a preview reference for Deck 01's orthogonal-array sampling
  display, not a claim that advanced variance reduction is already developed.
- KL, Stein discrepancy, modern transport maps, and the detailed queueing
  models retain their separate references. Do not force these into an Owen
  chapter merely to make the title list comprehensive.
- Chapters 15–17 retain their numbering in Owen's *Practical Quasi-Monte Carlo
  Integration*, linked from his book page. Titles give compact chapter ranges;
  the notebook table above records the actual connections and qualifications.

## Verified sources

- [Owen's book and chapter contents](https://artowen.su.domains/mc/)
- [Owen's current QMC/RQMC chapters](https://artowen.su.domains/mc/practicalqmc.pdf)
- [Hickernell, Kirk, and Sorokin, *Quasi-Monte Carlo Methods: What, Why, and How?*](https://arxiv.org/abs/2502.03644), especially Section 5

The tutorial citation uses the existing pinned shared metadata entry
`papers.hickirsor_2026_qmc_tutorial`. Its 2026 publication year is distinct
from the 2025 arXiv posting date. No shared-library change or pin update is needed.

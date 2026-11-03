# MATH 565 deck accuracy and clarity audit

## November 2, 2026 — all five existing decks

Reviewed the complete current sources for Introduction, Generating Samples,
Markov Chain Monte Carlo, Improving Efficiency, and Selected Topics. Scope
includes mathematical claims and conditions, worked examples, exercise prompts
and presenter answers, embedded Python, notation, proof/teaching dependencies,
and consistency with the pinned software and cited saved notebook evidence.
The slides remain the authoritative exposition; this file records the audit.

### Findings and corrections

| Deck | Corrections |
|---|---|
| 01 — Introduction | State moment and fixed-size IID assumptions; define the CDF on all real arguments; distinguish empirical masses from density estimates; match the empirical generalized-inverse quantile with NumPy's inverted-CDF method; use a density histogram. Reserve n for sample size and align input/map notation. Add missing moment, covariance, shrinkage, quantile and conditioning answer notes; distinguish singular Gaussian laws from the displayed full-dimensional density. |
| 02 — Generating Samples | Distinguish individually uniform randomized inputs from fixed low discrepancy quadrature nodes; remove the claim that arbitrary quantile transforms preserve dependence structure. State distribution parameter ranges, specify the continuous-path Brownian version, and label the finite-grid American-put problem as a grid-restricted approximation. Add missing quantile, mixture and geometric-Brownian answer notes. |
| 03 — Markov Chain Monte Carlo | Make the finite-state Metropolis exercise use independent uniform proposals with replacement, matching its acceptance ratio. Add its answer notes, initialization/ergodicity conditions, and the unbiased-MMD answer explanation. Use the nonnegative Gram quadratic-form definition of positive definite kernels, distinguishing strictness and the characteristic property; state kernel moment and sample-size conditions. Clarify the all-coordinate-subset Sobolev norm and single-server FCFS queue scope; fix a multiline display environment. |
| 04 — Improving Efficiency | Replace the old Keister stopping table with the four rows of the actual saved run and correct its exercise answers: replicated Sobol' and the Walsh bound meet the reported tolerance, while IID CLT and tight-budget Sobol' do not. Qualify Brownian drift and monitoring times, inverse-based conditional-density regularity and atoms, and the Asian payoff's positive strike. Add the missing monotone-antithetic proof. Explain that arbitrary generators need not give low discrepancy and rational Kronecker hand examples eventually repeat. |
| 05 — Selected Topics | Clarify conditional unbiasedness of stochastic gradients at adaptive iterates, without implying unbiased minimizer estimates or descent at every step. Align numerical matrix/coordinate notation and separate variance reduction from the role of structured points in the recap. The existing multilevel allocation, cost/error models, worked counts and UCT scores pass independent verification; the instructor's simplified many-level teaching sequence is preserved. |

The shared slide metadata had a stale CDN MathJax override. It now references
the pinned bundled runtime, matching classlib guidance. The generated HTML
for every deck uses that local path and the runtime exists in the assembled
site. No shared dependency or pin was changed.

Updated the MCMC migration handoff to match the existing placement of KL,
Stein and comparison slides after centered discrepancy under Alternative
comparisons. No lecture dates, coverage, assignments, grades, notebook code,
or saved notebook outputs were changed by this audit.

### Validation and references

- All five decks execute and render with the existing qmcpy kernel; all
  18 embedded Python cells complete. The root website also renders. No
  warnings or errors are found in the complete build logs. Generated deck
  output is assembled locally beneath `_site/slides`.
- 19 focused analytic/numerical checks for Decks 01–02 cover quantiles,
  mixtures, covariance factors, Brownian constructions, shrinkage, transport
  Jacobians and rejection. All 13 Python cells in these decks were also
  checked independently against pinned QMCPy.
- Deck 03 checks include both plotted simulations and rejection counts,
  exact finite-state MH invariance and exercise states/acceptance values,
  whole-target tempering algebra, the negative unbiased-MMD example, and
  all queue exercise event/customer-time results.
- 51 exact/evidence checks for Deck 04 cover IS means/variances and Brownian
  weights, controls and their cost, self-normalized IS, antithetic identities,
  low discrepancy construction arithmetic, RQMC cost powers, and the actual
  saved stopping rows. Pinned QMCPy source confirms the stopping interfaces
  and formulas referenced in the deck.
- 43 exact/numerical checks for Deck 05 cover random and deterministic
  allocations at p=1/2, 1 and 3/2, optimized cost formulas, the IID exercise,
  same-time error powers, covariance, quadratic losses/gradients, and UCT scores.
- All 634 local links/assets emitted by the five decks resolve, including
  destination fragments. Generated IDs are unique and the bundled MathJax
  configuration/path is verified for every deck.
- All previous explicit anchors and exercise markers are preserved. Visible
  prose emphasis/terminal-period checks, Python syntax/execution and
  `git diff --check` pass. All three pinned dependencies and the historical
  reference checkout remain clean and unchanged; MATH 332 is untouched.

Primary-reference checks support the theorem qualifications already in the
slides: [Giles, Multilevel Monte Carlo methods](https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf)
for allocation and complexity assumptions, and
[Kocsis and Szepesvari, Bandit based Monte-Carlo Planning](https://sites.ualberta.ca/~szepesva/papers/ecml06.pdf)
for the UCT setting and evolving rollout returns. The kernel Stein expression
and boundary conditions were checked against
[Liu, Lee and Jordan (2016), Section 2.2 and Theorem 3.6](https://proceedings.mlr.press/v48/liub16.pdf).
The primary abstracts of [Gorham and Mackey (2017)](https://proceedings.mlr.press/v70/gorham17a.html)
and [Liu, Duncan and Gandy (2023)](https://proceedings.mlr.press/v202/liu23i.html)
support the existing kernel-choice/nonconvergence and separated-mode
limitations; those two complete papers were not re-audited.

### Remaining work

The deck source/content review is complete. No further mathematical issue
was identified in this pass. This does not complete the instructor's review
of the later drafts or select the remaining enrichment coverage.

The Keister companion notebook has a separate stale Markdown explanation:
it still names a green band of 0.05 while its executed settings, saved table
and plot use 0.0005. The deck now matches the actual output. This notebook
prose follow-up is recorded in [issue 3](https://github.com/fjhickernell/MATH565Fall2026/issues/3),
assigned to fjhickernell; its code and saved outputs were left intact.

Visual layout, interactive navigation and browser MathJax typesetting remain
unverified under the existing local-file browser restriction; no alternate
route was attempted. Review the changed slides before classroom use,
especially the extra statistical-estimation table row, quantile explanation,
Metropolis prompt, kernel definition and four-row stopping table.

The November 3 Selected Topics continuation and the instructor's simplified
many-level/SGD review plan are unchanged. The source/documentation corrections
are included in the November 2 Checkpoint. Remote CI/deployment and live
verification remain pending.

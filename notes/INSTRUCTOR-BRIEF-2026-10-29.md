# Instructor brief — October 29, 2026

MATH 565 · Thursday, 10:00–11:15 AM America/Chicago · PH 109

Instructor preparation only. This is a proposed plan, not a record of material
taught. The October 22 recording ledger confirms completion through the
IID/RQMC worked cost comparison and tighter-RMSE exercise. October 27 was
assessment-only. Resume Deck 04 at **Big Ideas (continued)**.

## Suggested pacing

- **10:00–10:12 — Big Ideas (continued).** Controls and conditioning exploit
  known structure; antithetics introduce useful dependence; low discrepancy
  designs improve space filling; suitable randomizations support unbiasedness
  and error assessment. LHS remains optional/skipped.
- **10:12–10:25 — How Far We Have Come.** Connect travel time, option pricing,
  Bayesian inference, and queues: formulate the output, generate inputs, choose
  the representation and design, assess error, and compare work.
- **10:25–10:45 — Choose the Method for the Task.** Define the requested output
  first. Equal expectations do not imply equal distributions: a control-adjusted
  contribution's histogram is not the original payoff distribution. For an
  unbiased IID mean, use $C\approx c\,\operatorname{var}(Y)/\varepsilon^2$,
  then account for setup and pilots. Use the control-cost exercise below.
- **10:45–11:10 — Transition to Deck 05.** “We have changed the contribution
  and the points; now we change how computation is organized.” Cover parallel
  computing, CPU/GPU comparisons, timing interpretation, same-time accuracy,
  and shared samples across many expectations.
- **11:10–11:15 — Close.** Recommended stopping point: **Computing many
  expectations together**. Next meeting begins **Two-level Monte Carlo**.
  If discussion runs long, stop after **Faster computation and statistical
  accuracy** instead.

Deck 05's numerical takeaway: 16-fold throughput gives approximately fourfold
smaller IID RMSE, under comparable variance and negligible numerical error.
More simultaneous outputs do not increase samples per output; shared inputs
correlate their estimates. Name the timing baseline and include generation,
evaluation, GPU synchronization, and overhead. Parallelism does not repair bias
or a poor sampling design.

## Existing exercises and answers

Use the control-cost exercise as the main discussion. The others are optional
callbacks to existing Deck 04 exercises, not new assigned work.

### One control: variance and cost

Given $\operatorname{var}(Y)=9$, $\operatorname{var}(\eta)=4$,
$\operatorname{cov}(Y,\eta)=3$, and $\mathbb E(\eta)=0$, use
$Y_{\mathrm{CV}}=Y-\beta\eta$. A controlled contribution costs twice as much.

**Answer:** $\beta_*=3/4$; residual variance is $27/4$. Work factors are
$9c$ versus $13.5c$: direct sampling wins despite variance reduction, ignoring
setup, pilots, and integer rounding. An independent pilot preserves conditional
unbiasedness; charge its cost in practice.

### Compare transport and importance sampling

For $Z\sim\operatorname{Unif}(0,1)$ and target density $2x$ on $(0,1)$,
compare $f(\sqrt Z)$ and $2Zf(Z)$.

**Answer:** For $f(x)=x$, both means are $2/3$; variances are $1/18$ and
$16/45$. For $f(x)=1-x$, both means are $1/3$; variances are $1/18$ and
$1/45$. The integrand changes the ranking. These are equal-contribution-count
comparisons, not established equal-cost comparisons.

### Condition a sum of two uniforms

For independent uniforms and $Y=U_1+U_2$, condition on $U_2=v$.

**Answer:** The conditional CDF is $\min(1,\max(0,y-v))$; a conditional-density
version is $\mathbf1_{\{v<y<v+1\}}$. Averaging gives density $y$ on $(0,1]$,
$2-y$ on $(1,2)$, and zero outside $(0,2)$, with consistent endpoint choices.
The average of conditional densities is unbiased at each fixed $y$ by total
expectation. It estimates density values rather than generating new payoff
samples.

### Tenfold tighter RMSE — already completed October 22

The existing hypothetical comparison has IID contribution variance one,
one-run RQMC variance approximately $16/n^2$ for large $n$, 16 independent
replications, equal point cost, and no setup cost.

**Answer:** At RMSE $0.001$, IID needs 1,000,000 evaluations; RQMC uses
$16\times1024=16,384$. Before rounding, work grows by factors 100 and 10;
the rounded RQMC comparison grows by 8 from the original 2,048 evaluations.
The assumed variance model is not a confidence-coverage guarantee, and a small
pilot does not establish it.

## Unresolved issues

- Decks 04–05 and the GPU companion still need instructor content review.
  Saved M3 execution exists; student-facing GPU notebook links remain deferred.
- The Asian/lookback complete-run cost interpretation and interrupted
  four-method lookback comparison remain unfinished. They are optional
  callbacks, not prerequisites for Deck 05.
- Deck 04's forward preview lists topics in a different order and omits MCTS.
  Follow Deck 05's actual order: parallel, multilevel, SGD, then MCTS.
- Older Keister slide numbers use tolerance $0.05$; the current notebook
  retains $0.0005$. Identify them as different saved settings if revisited.
- Deck 05's overarching reading reference remains undecided; no executable
  MCTS notebook exists.

## Source navigation

- [Deck 04 source: closing synthesis and presenter notes](../slides/04-improving-efficiency.qmd)
- [Deck 05 source: parallel computing and selected topics](../slides/05-selected-topics.qmd)
- [Current handoff](NEXT.md)
- [Recording evidence and continuation ledger](LECTURE-UPDATES.md)
- [Course schedule](../pages/schedule.qmd)

This brief preserves the existing course material and saved outputs. Preparing
and saving it does not establish lecture coverage or grading completion and
does not authorize grade release or student-facing publication.

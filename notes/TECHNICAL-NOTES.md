# Technical Notes

This file records repository architecture, implementation notes, maintenance
knowledge, and technical context useful to future maintainers and agents. Keep
details here when they are durable but too specific for `AGENTS.md`.

## QMCPy acceptance--rejection companion

`notebooks/sampling/TransportMapsAndAcceptanceRejection.ipynb` uses
`qmcpy.AcceptanceRejection` because both targets match its unit-cube interface.
The recorded QMCPy commit `d8fec003` already provides this API; no dependency
update is needed. Keep `classlib` for `nbviz` and leave its more general
acceptance--rejection utility unchanged.

- Use `IIDStdUniform` with dimension equal to target dimension plus one:
  2 for Beta$(2,1)$ and 3 for the bounded banana. A QMC driver would require a
  separately motivated change to the IID narrative.
- Pass ordinary densities, not log densities. The Beta example uses
  `2 * x[:, 0]`, `upper_bound=2`, and `density_integral=1`. The banana uses
  `np.exp(log_banana(x))`, `upper_bound=1`, and the quadrature-computed
  `banana_mass` (approximately `0.12571`). Compute that mass before
  constructing the sampler.
- The mathematical acceptance decision does not require the target's
  normalizing constant. The current QMCPy API nevertheless requires the
  density integral to size its driver batches and report its theoretical
  acceptance rate; do not pass a dummy integral.
- QMCPy generates power-of-two batches and may discard surplus accepted
  points. Returned samples divided by generated driver points therefore
  mixes batching overhead with acceptance probability. Retain fixed-proposal
  experiments that count every accepted proposal for empirical diagnostics,
  and label theoretical proposals per accepted draw as excluding batching
  overhead. Do not expose private `_driver_offset` state for diagnostics.

Local validation executes the ten code cells with the course-recorded
dependency checkouts, inspects the six figures, and checks the sample moments
and acceptance rate against analytic or quadrature benchmarks. A clean Colab
run remains a separate deployment-environment check. Report reusable QMCPy
defects for upstream repair rather than adding course-only workarounds.

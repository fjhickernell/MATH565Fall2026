"""Unit-length, uniformly loaded Euler--Bernoulli beam for the 565 companion.

Independent log stiffnesses are constant on equal material regions. Forward
evaluations use composite midpoint integration; analytic formulas are kept
separate for validation and for exposing the remaining approximation bias.
This classroom model is adapted from the UM-Bridge beam, not its container's
finite-difference implementation or particular load/geometry data.
"""
from functools import lru_cache

import numpy as np
import qmcpy as qp


def _region_count(regions):
    if not np.isscalar(regions) or not np.isfinite(regions) or int(regions) != regions or regions < 1:
        raise ValueError("regions must be a positive integer")
    return int(regions)


def _panel_count(panels, regions=3):
    regions = _region_count(regions)
    if (not np.isscalar(panels) or not np.isfinite(panels) or
            int(panels) != panels or panels < regions or panels % regions):
        raise ValueError("panels must be a positive integer multiple of the region count")
    return int(panels)


@lru_cache(maxsize=32)
def _grid(panels, regions=3):
    panels = _panel_count(panels, regions)
    midpoints = (np.arange(panels) + 0.5) / panels
    indices = np.minimum((regions * midpoints).astype(int), regions-1)
    return midpoints, indices


def _material(log_stiffness):
    m = np.asarray(log_stiffness, dtype=float)
    if m.ndim < 1 or m.shape[-1] < 1 or not np.isfinite(m).all():
        raise ValueError("log_stiffness must have finite values and a nonempty last axis")
    return m


def beam_tip(log_stiffness, panels, load=1.0):
    """Midpoint approximation of tip deflection, with O(panels) work per beam.

    Integrates (1-x) times the curvature load*(1-x)^2/(2*exp(m(x))).
    Arbitrary leading batch axes, including QMC replications, are supported.
    """
    m = _material(log_stiffness)
    panels = _panel_count(panels, m.shape[-1])
    x, indices = _grid(panels, m.shape[-1])
    compliance = np.exp(-m)[..., indices]
    return (compliance * (load * (1 - x)**3 / 2)).sum(axis=-1) / panels


def beam_profile(log_stiffness, panels, load=1.0):
    """Deflections at grid nodes, obtained by two integrations of curvature."""
    m = _material(log_stiffness)
    panels = _panel_count(panels, m.shape[-1])
    x, indices = _grid(panels, m.shape[-1])
    nodes = np.arange(panels + 1) / panels
    curvature = np.exp(-m)[..., indices] * load * (1 - x)**2 / 2
    slope_integrals = np.cumsum(curvature, axis=-1) / panels
    first_moments = np.cumsum(x * curvature, axis=-1) / panels
    displacement = nodes[1:] * slope_integrals - first_moments
    return nodes, np.concatenate([np.zeros(m.shape[:-1] + (1,)), displacement], axis=-1)


def exact_coefficients(load=1.0, regions=3):
    """Coefficients of exp(-m_j) in the exact tip deflection."""
    regions = _region_count(regions)
    edges = np.arange(regions+1) / regions
    return load * ((1 - edges[:-1])**4 - (1 - edges[1:])**4) / 8


def grid_coefficients(panels, load=1.0, regions=3):
    """Finite-grid coefficients, used for validation, not forward evaluation."""
    panels = _panel_count(panels, regions)
    x, indices = _grid(panels, regions)
    return np.bincount(indices, weights=load * (1 - x)**3 / (2 * panels), minlength=regions)


def exact_tip(log_stiffness, load=1.0):
    m = _material(log_stiffness)
    return np.exp(-m) @ exact_coefficients(load, m.shape[-1])


def compliance_moments(lower=1.0, upper=1.05):
    """Mean and variance of exp(-M), M uniform on [lower, upper]."""
    if not np.isfinite([lower, upper]).all() or upper <= lower:
        raise ValueError("finite bounds with lower < upper are required")
    width = upper - lower
    mean = np.exp(-lower) * (-np.expm1(-width)) / width
    second = np.exp(-2 * lower) * (-np.expm1(-2 * width)) / (2 * width)
    return float(mean), float(max(0.0, second - mean**2))


def reference_moments(panels=None, lower=1.0, upper=1.05, load=1.0, regions=3):
    """Exact stochastic mean/variance, either at finite grid or in the limit."""
    coefficients = (exact_coefficients(load, regions) if panels is None
                    else grid_coefficients(panels, load, regions))
    mean_compliance, variance_compliance = compliance_moments(lower, upper)
    return (float(mean_compliance * coefficients.sum()),
            float(variance_compliance * np.dot(coefficients, coefficients)))


def level_moments(course_level, lower=1.0, upper=1.05, load=1.0, regions=3):
    """Exact mean and variance of a same-material coupled contribution."""
    if int(course_level) != course_level or course_level < 1:
        raise ValueError("course_level must be a positive integer")
    regions = _region_count(regions)
    panels = regions * 2**(int(course_level) - 1)
    coefficients = grid_coefficients(panels, load, regions)
    if course_level > 1:
        coefficients = coefficients - grid_coefficients(panels // 2, load, regions)
    mean_compliance, variance_compliance = compliance_moments(lower, upper)
    return (float(mean_compliance * coefficients.sum()),
            float(variance_compliance * np.dot(coefficients, coefficients)))


class BeamMultilevel(qp.AbstractIntegrand):
    """Course beam adapter for QMCPy's native MLMC and MLQMC solvers.

    QMCPy refinement indices are zero-based: level=0 is the notebook's first
    level with one panel per material region. A root with level=None is supplied to the native
    stopping criterion, which spawns the coupled levels it needs. The random
    input dimension equals the material-region count and stays fixed at every mesh.
    """

    def __init__(self, sampler, level=None, lower=1.0, upper=1.05, load=1.0):
        if level is not None and (int(level) != level or level < 0):
            raise ValueError("level must be a nonnegative integer")
        self.regions = _region_count(sampler.d)
        compliance_moments(lower, upper)
        self.sampler = sampler
        self.true_measure = qp.Uniform(sampler, lower_bound=lower, upper_bound=upper)
        self.level = None if level is None else int(level)
        self.lower, self.upper, self.load = float(lower), float(upper), float(load)
        self.panels = self.regions * 2**(self.level or 0)
        self.cost = self.panels + (self.panels // 2 if self.level else 0)
        self.multilevel = level is not None
        self.parameters = ["level", "panels", "cost"]
        shape = (2,) if self.multilevel else ()
        super().__init__(dimension_indv=shape, dimension_comb=shape, parallel=False)

    def g(self, m, **kwargs):
        fine = beam_tip(m, self.panels, self.load)
        if not self.multilevel:
            return fine
        coarse = (beam_tip(m, self.panels // 2, self.load)
                  if self.level else np.zeros_like(fine))
        return np.stack([coarse, fine])

    def dimension_at_level(self, level):
        return self.regions

    def _spawn(self, level, sampler):
        return BeamMultilevel(sampler, level, self.lower, self.upper, self.load)

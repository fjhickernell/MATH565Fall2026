"""Course-specific examples shared by the Deck 03 notebooks.

The scalar MH algorithm stays visible in MetropolisHastings.ipynb. These helpers
keep the bounded target and replica-exchange implementation consistent across
independently executable notebooks. No files or global random state are modified.
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import erf


def log_banana(points, a=2.0, b=60.0):
    """Unnormalized density from TransportMapsAndAcceptanceRejection, on [0,1]^2."""
    points = np.asarray(points, dtype=float)
    single = points.ndim == 1
    points = np.atleast_2d(points)
    if points.shape[1] != 2 or a < 0 or b <= 0:
        raise ValueError("Require two coordinates, a >= 0, and b > 0")
    x1, x2 = points.T
    inside = np.all((points >= 0) & (points <= 1), axis=1)
    values = np.full(len(points), -np.inf)
    values[inside] = -a * (1 - x1[inside])**2 - b * (x2[inside] - x1[inside]**2)**2
    return float(values[0]) if single else values


def banana_mass(a=2.0, b=60.0):
    """Integral of the unnormalized target; also the uniform-envelope AR rate."""
    if a < 0 or b <= 0:
        raise ValueError("Require a >= 0 and b > 0")
    root = np.sqrt(b)
    def marginal(x):
        return (np.exp(-a * (1 - x)**2) * np.sqrt(np.pi) / (2 * root)
                * (erf(root * (1 - x*x)) + erf(root * x*x)))
    return quad(marginal, 0, 1, epsabs=1e-11)[0]


def banana_reference(n):
    """Use exactly the QMCPy IID rejection construction already taught."""
    import qmcpy as qp
    mass = banana_mass()
    sampler = qp.AcceptanceRejection(
        sampler=qp.IIDStdUniform(dimension=3),
        target_density=lambda points: np.exp(log_banana(points)),
        upper_bound=1, density_integral=mass)
    return sampler.gen_samples(n=n), mass


def banana_mean(order=100):
    """Independent tensor Gauss--Legendre integration of the target's mean."""
    nodes, weights = np.polynomial.legendre.leggauss(order)
    nodes, weights = (nodes + 1) / 2, weights / 2
    xx, yy = np.meshgrid(nodes, nodes, indexing='ij')
    points = np.column_stack([xx.ravel(), yy.ravel()])
    masses = np.outer(weights, weights).ravel() * np.exp(log_banana(points))
    return masses @ points / masses.sum()


def random_walk_nd(log_target, x0, n, proposal_sd, rng):
    """Symmetric Gaussian Metropolis; retain repetitions and include x0."""
    x0 = np.atleast_1d(np.asarray(x0, dtype=float))
    if n < 2 or int(n) != n or proposal_sd <= 0 or not np.isfinite(proposal_sd):
        raise ValueError("Require integer n >= 2 and positive finite proposal_sd")
    states = np.empty((n, x0.size))
    states[0] = x0
    current = float(log_target(x0))
    if not np.isfinite(current):
        raise ValueError("Initial state must have finite log target density")
    accepted = 0
    for i in range(1, n):
        candidate = states[i-1] + rng.normal(scale=proposal_sd, size=x0.size)
        proposed = float(log_target(candidate))
        u = rng.random()
        if np.isfinite(proposed) and (u == 0 or np.log(u) <= min(0., proposed-current)):
            states[i] = candidate
            current = proposed
            accepted += 1
        else:
            states[i] = states[i-1]
    return dict(states=states, acceptance=accepted/(n-1), evaluations=n)


def swap_log_ratio(beta_left, beta_right, logp_left, logp_right):
    """Whole-target tempering: log density of swapped pair / current pair."""
    return (beta_left-beta_right)*(logp_right-logp_left)


def parallel_tempering(log_target, x0, betas, n, proposal_sds, rng):
    """Scalar whole-target replica exchange; one update/replica/sweep.

    Alternate disjoint adjacent swap pairs after each local-update sweep.
    Store temperature-slot states, so column 0 always targets beta=1.
    Caches make target evaluations R*n, including initialization.
    """
    betas = np.asarray(betas, dtype=float)
    proposal_sds = np.asarray(proposal_sds, dtype=float)
    x = np.asarray(x0, dtype=float).copy()
    r = len(betas)
    if (r < 2 or betas[0] != 1 or not np.all(np.diff(betas) < 0)
            or not np.all(betas > 0) or not np.all(np.isfinite(betas))):
        raise ValueError("Require 1=beta[0]>beta[1]>...>0")
    if (x.shape != (r,) or proposal_sds.shape != (r,) or n < 2 or int(n) != n
            or not np.all(np.isfinite(proposal_sds)) or not np.all(proposal_sds > 0)):
        raise ValueError("Supply one start and positive scale per replica; integer n >= 2")
    logp = np.array([float(log_target(value)) for value in x])
    if not np.all(np.isfinite(logp)):
        raise ValueError("Starts must have finite log target density")
    traces = np.empty((n, r))
    traces[0] = x
    accepts = np.zeros(r, dtype=int)
    swaps = np.zeros(r-1, dtype=int)
    attempts = np.zeros(r-1, dtype=int)
    for i in range(1, n):
        for j in range(r):
            z = x[j] + rng.normal(scale=proposal_sds[j])
            log_z = float(log_target(z))
            u = rng.random()
            if np.isfinite(log_z) and (u == 0 or np.log(u) <= min(0., betas[j]*(log_z-logp[j]))):
                x[j], logp[j] = z, log_z
                accepts[j] += 1
        for j in range((i-1) % 2, r-1, 2):
            attempts[j] += 1
            delta = swap_log_ratio(betas[j], betas[j+1], logp[j], logp[j+1])
            u = rng.random()
            if u == 0 or np.log(u) <= min(0., delta):
                x[j], x[j+1] = x[j+1], x[j]
                logp[j], logp[j+1] = logp[j+1], logp[j]
                swaps[j] += 1
        traces[i] = x
    return dict(states=traces, acceptance=accepts/(n-1), swaps=swaps,
                swap_attempts=attempts, swap_rate=np.divide(swaps, attempts,
                    out=np.full(r-1, np.nan), where=attempts>0), evaluations=r*n)


def gaussian_kernel(x, y, length_scale=0.2):
    x, y = np.atleast_2d(x), np.atleast_2d(y)
    if length_scale <= 0:
        raise ValueError("length_scale must be positive")
    distances = np.sum((x[:, None, :] - y[None, :, :])**2, axis=2)
    return np.exp(-distances/(2*length_scale**2))


def kernel_sum(x, y, length_scale=0.2, block_size=256):
    """Sum the Gaussian kernel in bounded-memory blocks, without subsampling."""
    total = 0.0
    for i in range(0, len(x), block_size):
        for j in range(0, len(y), block_size):
            total += gaussian_kernel(x[i:i+block_size], y[j:j+block_size], length_scale).sum()
    return float(total)


def mmd_squared(x, y, length_scale=0.2, reference_kernel_sum=None):
    """Empirical MMD^2 and off-diagonal value; optional cached sum K(y,y).

    The cache must belong to exactly this reference sample and length scale.
    Blocking changes memory use, not the empirical measures being compared.
    """
    x, y = np.asarray(x), np.asarray(y)
    n, m = len(x), len(y)
    if n < 2 or m < 2:
        raise ValueError("Each sample must contain at least two points")
    sxx = kernel_sum(x, x, length_scale)
    syy = (kernel_sum(y, y, length_scale) if reference_kernel_sum is None
           else reference_kernel_sum)
    sxy = kernel_sum(x, y, length_scale)
    biased = sxx/n**2 + syy/m**2 - 2*sxy/(n*m)
    # Gaussian kernel diagonal entries are exactly one.
    off_diagonal = ((sxx-n)/(n*(n-1)) + (syy-m)/(m*(m-1)) - 2*sxy/(n*m))
    return float(biased), float(off_diagonal)

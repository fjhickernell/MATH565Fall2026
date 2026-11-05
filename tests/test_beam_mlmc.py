"""Physics, bias, and package-interface checks for the beam companion."""
import sys
import unittest
from pathlib import Path

import numpy as np
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'qmcpy'), str(ROOT / 'notebooks')]
import qmcpy as qp
from beam_mlmc import (BeamMultilevel, beam_tip, beam_profile, exact_tip,
                       reference_moments, level_moments, compliance_moments)


class BeamChecks(unittest.TestCase):
    def test_constant_material_against_closed_form(self):
        exact = np.exp(-1.025) / 8
        for regions in (1, 3, 16):
            m = np.full((2, regions), 1.025)
            np.testing.assert_allclose(exact_tip(m), exact, rtol=1e-14)
            for panels in (regions, 2*regions, 8*regions):
                midpoint = np.exp(-1.025) * (1/8 - 1/(16 * panels**2))
                np.testing.assert_allclose(beam_tip(m, panels), midpoint, rtol=1e-14)

    def test_material_interfaces_against_independent_quadrature(self):
        m = np.array([1.0, 1.03, 1.05])
        reference = sum(quad(lambda x: (1-x)**3 / (2*np.exp(m[j])),
                             j/3, (j+1)/3, epsabs=1e-14)[0] for j in range(3))
        self.assertAlmostEqual(float(exact_tip(m)), reference, places=14)
        errors = [reference-float(beam_tip(m, panels)) for panels in (3, 6, 12)]
        np.testing.assert_allclose(np.array(errors[:-1])/errors[1:], 4, rtol=1e-11)

    def test_profile_boundary_and_tip_consistency(self):
        nodes, u = beam_profile([[1.0, 1.03, 1.05]], 48)
        self.assertEqual(u[0, 0], 0)
        np.testing.assert_allclose(u[..., -1], beam_tip([[1.0, 1.03, 1.05]], 48))
        # Two midpoint integrations converge to the clamped uniform-material curve.
        nodes, u = beam_profile([[1.025]*3], 192)
        analytical = np.exp(-1.025)*nodes**2*(6-4*nodes+nodes**2)/24
        self.assertLess(np.max(abs(u[0]-analytical)), 7e-7)

    def test_exact_mean_and_bias_independent_of_sampling(self):
        for regions, lower, upper in [(3, 1., 1.05), (16, 0., 2.)]:
            mean_compliance, _ = compliance_moments(lower, upper)
            mu, _ = reference_moments(lower=lower, upper=upper, regions=regions)
            for panels in (regions, 4*regions, 16*regions):
                finite, _ = reference_moments(panels, lower, upper, regions=regions)
                self.assertAlmostEqual(mu-finite, mean_compliance/(16*panels**2), places=14)
            # Independent one-dimensional stochastic integration; the expected
            # compliance is the same at every physical position.
            expected = quad(lambda m: np.exp(-m), lower, upper)[0]/(upper-lower)/8
            self.assertAlmostEqual(mu, expected, places=14)

    def test_coupling_telescope_and_replication_axes(self):
        for regions, lower, upper in [(3, 1., 1.05), (16, 0., 2.)]:
            sampler = qp.IIDStdUniform(regions, seed=565)
            m = qp.Uniform(sampler, lower_bound=lower, upper_bound=upper)(16)
            total = beam_tip(m, regions)
            for panels in (2*regions, 4*regions, 8*regions, 16*regions):
                total += beam_tip(m, panels)-beam_tip(m, panels//2)
            np.testing.assert_allclose(total, beam_tip(m, 16*regions), rtol=1e-14)
            adapted = BeamMultilevel(qp.DigitalNetB2(regions, replications=4, seed=565),
                                      level=2, lower=lower, upper=upper)
            values = adapted(16)
            self.assertEqual(values.shape, (2, 4, 16))
            children = adapted.spawn([0, 3])
            self.assertEqual([c.panels for c in children], [regions, 8*regions])
            self.assertEqual([c.cost for c in children], [regions, 12*regions])
            self.assertTrue(all(c.d == regions for c in children))

    def test_coupled_correction_variance_decay(self):
        for level in (2, 3, 4):
            _, var = level_moments(level)
            _, finer_var = level_moments(level+1)
            self.assertAlmostEqual(var/finer_var, 16, places=8)
            panels = 3*2**(level-1)
            independent = reference_moments(panels)[1]+reference_moments(panels//2)[1]
            self.assertLess(var, independent/100)

    def test_reference_variances_against_tensor_quadrature(self):
        # Independent integration of the actual beam responses over the three
        # material parameters, rather than reusing the moment formula.
        nodes, weights = np.polynomial.legendre.leggauss(10)
        for regions, lower, upper in [(3, 1., 1.05), (4, 0., 2.)]:
            coordinates = (lower+upper)/2 + (upper-lower)*nodes/2
            m = np.stack(np.meshgrid(*([coordinates]*regions), indexing='ij'), axis=-1).reshape(-1, regions)
            w = np.prod(np.stack(np.meshgrid(*([weights/2]*regions), indexing='ij'), axis=-1), axis=-1).ravel()
            for panels in (regions, 4*regions, None):
                y = exact_tip(m) if panels is None else beam_tip(m, panels)
                mean = np.dot(w, y)
                variance = np.dot(w, (y-mean)**2)
                expected_mean, expected_variance = reference_moments(panels, lower, upper, regions=regions)
                self.assertAlmostEqual(mean, expected_mean, places=13)
                np.testing.assert_allclose(variance, expected_variance, rtol=3e-9)

    def test_invalid_inputs(self):
        for panels in (0, 2, 4, 4.5):
            with self.assertRaises(ValueError):
                beam_tip([1, 1, 1], panels)
        with self.assertRaises(ValueError):
            beam_tip([1, 1], 3)
        with self.assertRaises(ValueError):
            compliance_moments(1.05, 1)
        with self.assertRaises(ValueError):
            BeamMultilevel(qp.IIDStdUniform(3), level=-1)
        for regions in (0, 1.5):
            with self.assertRaises(ValueError):
                reference_moments(regions=regions)


if __name__ == '__main__':
    unittest.main()

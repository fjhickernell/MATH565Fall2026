"""Independent pathwise checks for the course's SimPy queue models.

Run: python -m unittest discover -s tests -p 'test_queue_examples.py'
"""
import sys
import unittest
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'notebooks'))
from queue_examples import simulate_queue


class QueueChecks(unittest.TestCase):
    def check_accounting(self, run):
        m = run.summary()
        t, n = run.trajectory()
        self.assertAlmostEqual(np.sum(np.diff(t) * n[:-1]) / run.time, m['avg_N'])
        self.assertAlmostEqual(m['avg_N'], m['completed_residence_per_time'] +
                               m['unfinished_residence_per_time'])
        self.assertEqual(m['arrivals'], m['departures'] + m['remaining'])
        self.assertTrue(np.all(n >= 0))
        self.assertLessEqual(m['busy_1'] + m.get('blocked_1', 0), 1 + 1e-12)
        for c in run.customers:
            self.assertLessEqual(c['arrival'], c.get('start_1', np.inf))
        if run.tandem:
            self.assertLessEqual(m['busy_2'], 1 + 1e-12)
            events = []
            for c in run.customers:
                if 'transfer' in c:
                    events.append((c['transfer'], 1))
                if 'departure' in c:
                    events.append((c['departure'], -1))
            # Departures release capacity before same-time new admissions.
            occupancy = np.cumsum([v for _, v in sorted(events)])
            self.assertTrue(np.all((0 <= occupancy) & (occupancy <= run.capacity)))

    def test_single_server_matches_lindley_recursion(self):
        rng = np.random.default_rng(651)
        a = np.cumsum(rng.exponential(1.25, 500))
        v = rng.uniform(.8, 1.2, len(a))
        start, departure = [], 0
        for arrival, service in zip(a, v):
            start.append(max(arrival, departure))
            departure = start[-1] + service
        run = simulate_queue(a, v, n_complete=len(a))
        np.testing.assert_allclose([c['start_1'] for c in run.customers], start)
        np.testing.assert_allclose([c['departure'] for c in run.customers], np.array(start) + v)
        self.check_accounting(run)

    def test_horizon_clips_incomplete_service(self):
        run = simulate_queue([1, 2, 8], [10, 1, 1], t_end=4)
        m = run.summary()
        self.assertEqual(m['departures'], 0)
        self.assertEqual(m['arrivals'], 2)
        self.assertAlmostEqual(m['busy_1'], .75)
        self.assertAlmostEqual(m['avg_N'], 1.25)
        self.assertTrue(np.isnan(m['avg_W']))
        self.check_accounting(run)

    def test_events_at_horizon_excluded(self):
        run = simulate_queue([1, 2], [1, 1], t_end=2)
        self.assertEqual(run.summary()['arrivals'], 1)
        self.assertEqual(run.summary()['departures'], 0)
        self.check_accounting(run)

    def test_earlier_of_two_stops(self):
        run = simulate_queue([0, .1, .2], [1, 1, 1], t_end=10, n_complete=2)
        self.assertEqual(run.time, 2)
        self.assertEqual(run.summary()['departures'], 2)
        self.check_accounting(run)
        run = simulate_queue([0, .1, .2], [1, 1, 1], t_end=.5, n_complete=2)
        self.assertEqual(run.time, .5)
        self.assertEqual(run.summary()['departures'], 0)
        self.check_accounting(run)

    def test_drive_through_hand_calculated_path(self):
        for k, transfers, blocked in [(1, [1, 4, 7], .4), (2, [1, 2, 4], .1), (3, [1, 2, 3], 0)]:
            run = simulate_queue([0, .1, .2], [1, 1, 1], [3, 3, 3], capacity=k, n_complete=3)
            np.testing.assert_allclose([c['transfer'] for c in run.customers], transfers)
            np.testing.assert_allclose([c['departure'] for c in run.customers], [4, 7, 10])
            self.assertAlmostEqual(run.summary()['blocked_1'], blocked)
            self.assertAlmostEqual(run.summary()['busy_1'], .3)
            self.assertAlmostEqual(run.summary()['busy_2'], .9)
            self.check_accounting(run)

    def test_stop_while_blocked(self):
        run = simulate_queue([0, .1, .2], [1, 1, 1], [3, 3, 3], capacity=1, t_end=3)
        self.assertAlmostEqual(run.summary()['blocked_1'], 1 / 3)
        self.assertAlmostEqual(run.summary()['busy_1'], 2 / 3)
        self.check_accounting(run)

    def test_empty_observation_window(self):
        run = simulate_queue([10], [1], t_end=5)
        self.assertEqual(run.summary()['arrivals'], 0)
        self.assertEqual(run.summary()['avg_N'], 0)
        self.check_accounting(run)

    def test_invalid_inputs(self):
        for kwargs in [{'t_end': -1}, {'n_complete': 3}, {'n_complete': 1.5}, {}]:
            with self.assertRaises(ValueError):
                simulate_queue([0, 1], [1, 1], **kwargs)
        with self.assertRaises(ValueError):
            simulate_queue([1, 0], [1, 1], t_end=5)
        with self.assertRaises(ValueError):
            simulate_queue([0, 1], [1, 1], [1, 1], capacity=0, t_end=5)


if __name__ == '__main__':
    unittest.main()

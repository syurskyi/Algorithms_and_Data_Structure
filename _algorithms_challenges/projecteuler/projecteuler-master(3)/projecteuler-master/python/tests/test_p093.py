import unittest

from p093 import calc_consecutive


class TestProblem093(unittest.TestCase):

    def test_calc_consecutive(self):
        self.assertEqual(calc_consecutive(set(range(2, 10))), 0)
        self.assertEqual(calc_consecutive(set(range(1, 10))), 9)
        self.assertEqual(calc_consecutive({1, 2, 3, 4, 6, 7, 8, 9}), 4)

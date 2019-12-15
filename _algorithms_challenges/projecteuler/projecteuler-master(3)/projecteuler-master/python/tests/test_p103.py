import unittest

from p103 import is_special_sum_set


class TestProblem103(unittest.TestCase):

    def test_is_special_sum_set(self):
        self.assertTrue(is_special_sum_set([1]))
        self.assertTrue(is_special_sum_set([1, 2]))
        self.assertTrue(is_special_sum_set([2, 3, 4]))
        self.assertTrue(is_special_sum_set([3, 5, 6, 7]))
        self.assertTrue(is_special_sum_set([6, 9, 11, 12, 13]))
        self.assertTrue(is_special_sum_set([11, 18, 19, 20, 22, 25]))
        self.assertTrue(is_special_sum_set([157, 150, 164, 119, 79, 159, 161,
                                            139, 158]))
        self.assertFalse(is_special_sum_set([81, 88, 75, 42, 87, 84, 86, 65]))

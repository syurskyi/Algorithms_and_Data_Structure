import unittest

from p041 import is_pandigital


class TestProblem041(unittest.TestCase):

    def test_is_pandigital(self):
        self.assertTrue(is_pandigital(123456789, 9))
        self.assertTrue(is_pandigital(122333444455556789, 9))
        self.assertTrue(is_pandigital(1234, 4))
        self.assertFalse(is_pandigital(1023456789, 9))
        self.assertFalse(is_pandigital(12345, 4))
        self.assertFalse(is_pandigital(1234, 5))

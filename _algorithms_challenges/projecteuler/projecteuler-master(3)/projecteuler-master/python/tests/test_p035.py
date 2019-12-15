import unittest

from p035 import rotations


class TestProblem035(unittest.TestCase):

    def test_rotations(self):
        self.assertEqual(list(rotations(197)), [719, 971, 197])

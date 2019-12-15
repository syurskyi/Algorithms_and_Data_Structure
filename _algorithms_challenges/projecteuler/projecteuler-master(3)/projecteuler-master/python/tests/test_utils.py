"""
This module contains tests for utils.

To run the tests execute:
$ nosetests -v tests/test_utils.py
or
$ python -m unittest -v tests/test_utils.py
"""

import unittest
from itertools import islice

from utils import (  # isort:skip
    arithmetic_series,
    exp_by_squaring,
    hexagonal_numbers,
    is_palindrome,
    is_pandigital,
    is_pentagonal,
    is_prime,
    is_square,
    is_triangular_number,
    isqrt,
    nth_pentagonal,
    nth_triangle,
    num_of_divisors,
    pentagonal_numbers,
    sum_digits,
    triangular_numbers,
)


class TestUtils(unittest.TestCase):
    def test_arithmetic_series(self):
        self.assertEqual(arithmetic_series(1, 100, 100), 5050)
        self.assertEqual(arithmetic_series(2, 100, 50), 2550)

    def test_is_pentagonal(self):
        self.assertTrue(is_pentagonal(1))
        self.assertFalse(is_pentagonal(2))
        self.assertTrue(is_pentagonal(5))
        self.assertFalse(is_pentagonal(15))

        n = 10**15
        p = nth_pentagonal(n)
        self.assertTrue(is_pentagonal(p))
        self.assertFalse(is_pentagonal(p + 2))

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(15485863))

    def test_is_square(self):
        self.assertTrue(is_square(4))
        self.assertFalse(is_square(8))
        x = 12345678987654321234567 ** 2
        self.assertTrue(is_square(x))
        self.assertFalse(is_square(x + 2))

    def test_triangular_numbers(self):
        self.assertEqual(list(islice(triangular_numbers(), 20)),
                         [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105,
                          120, 136, 153, 171, 190, 210])

    def test_pentagonal_numbers(self):
        self.assertEqual(list(islice(pentagonal_numbers(), 20)),
                         [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210,
                          247, 287, 330, 376, 425, 477, 532, 590])

    def test_hexagonal_numbers(self):
        self.assertEqual(list(islice(hexagonal_numbers(), 20)),
                         [1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276,
                          325, 378, 435, 496, 561, 630, 703, 780])

    def test_is_triangular_number(self):
        self.assertTrue(is_triangular_number(1))
        self.assertFalse(is_triangular_number(2))
        n = 10**15
        t = nth_triangle(n)
        self.assertTrue(is_triangular_number(t))
        self.assertFalse(is_triangular_number(t + 2))

    def test_is_pandigital(self):
        self.assertTrue(is_pandigital(923456781))
        self.assertFalse(is_pandigital(12345678))
        self.assertFalse(is_pandigital(102345678))
        self.assertFalse(is_pandigital(1023456789))

    def test_exp_by_squaring(self):
        for num, p in ((2, 3), (10, 10), (1234, 5678)):
            self.assertEqual(exp_by_squaring(num, p), pow(num, p))

    def test_isqrt(self):
        data = (
            (1, 1), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
            (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3),
            (16, 4), (17, 4), (18, 4), (19, 4), (20, 4), (21, 4), (22, 4),
            (23, 4), (24, 4), (25, 5), (26, 5), (27, 5), (28, 5), (29, 5),
            (30, 5), (31, 5), (32, 5), (33, 5), (34, 5), (35, 5), (36, 6),
            (37, 6), (38, 6), (39, 6), (40, 6), (99, 9), (100, 10), (101, 10),
            (289, 17), (65535, 255), (65536, 256), (65537, 256),
            (1073741823, 32767), (1073741824, 32768), (1073741825, 32768),
            (2147483648, 46340), (4294967295, 65535))

        for num, root in data:
            self.assertEqual(isqrt(num), root, f"isqrt({num}) != {root}")

    def test_sum_digits(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(1), 1)
        self.assertEqual(sum_digits(1000), 1)
        self.assertEqual(sum_digits(1234567890), 45)

    def test_num_of_divisors(self):
        self.assertEquals([num_of_divisors(x) for x in range(1, 17)],
                          [1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5])

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(1))
        self.assertFalse(is_palindrome(10))
        self.assertTrue(is_palindrome(101))
        self.assertFalse(is_palindrome(int("10", base=2), base=2))
        self.assertTrue(is_palindrome(int("101", base=2), base=2))
        self.assertFalse(is_palindrome(int("123", base=4), base=4))
        self.assertTrue(is_palindrome(int("12321", base=4), base=4))

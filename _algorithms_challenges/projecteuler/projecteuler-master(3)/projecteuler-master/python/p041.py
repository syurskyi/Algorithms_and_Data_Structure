#!/usr/bin/env python

"""Problem 41: Pandigital prime"""

from itertools import permutations

from utils import is_prime


def is_pandigital(n, digits):
    """
    Check if a number is '1' to 'digits' pandigital.
    The function doesn't check for redundant digits.
    """
    flags = 0

    while n:
        flags |= (1 << n % 10)
        n //= 10

    return flags == ((1 << digits) - 1) << 1


def main():
    digits = "987654321"

    # only 7- or 4-digit numbers need to be considered
    # in other cases the sum is divisible by 3
    for ndigits in (7, 4):
        for p in permutations(digits[-ndigits:], ndigits):
            n = int("".join(p))

            if is_pandigital(n, ndigits) and is_prime(n):
                return n

if __name__ == "__main__":
    print(main())

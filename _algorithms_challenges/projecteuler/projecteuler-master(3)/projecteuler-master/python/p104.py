#!/usr/bin/env python

"""Problem 104: Pandigital Fibonacci ends"""

from math import log10, sqrt

from utils import is_pandigital


def main():
    a, b, cnt = 1, 1, 2
    # https://en.wikipedia.org/wiki/Fibonacci_number#Relation_to_the_golden_ratio
    φ = (1 + sqrt(5)) / 2

    while True:
        # keep only the last 9 digits of the fibonacci numbers
        a, b = b, (a + b) % 10**9
        cnt += 1

        if is_pandigital(b):
            # use some logarithm rules
            num_digits = cnt*log10(φ) - log10(sqrt(5))
            if is_pandigital(int(10 ** (num_digits % 1 + 8))):
                return cnt

if __name__ == "__main__":
    print(main())

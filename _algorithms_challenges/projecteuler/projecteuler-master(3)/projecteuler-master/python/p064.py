#!/usr/bin/env python

"""Problem 64: Odd period square roots"""

from math import sqrt

from utils import sqrt_fraction_expansion as sfe


def main():
    lim = 10000
    squares = {x*x for x in range(2, int(sqrt(lim)) + 1)}

    return sum([1 for n in range(2, lim+1) if not (n in squares or len(sfe(n)) & 1)])

if __name__ == "__main__":
    print(main())

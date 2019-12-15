#!/usr/bin/env python

"""Problem 33: Digit cancelling fractions"""

from functools import reduce
from math import gcd


def main():
    fractions = []

    for a in range(10, 99):
        for b in range(a+1, 100):
            if not a % 10 or not b % 10:
                continue

            # the numbers need to be of the form AX/XB (e.g. 49/98)
            if a % 10 == b // 10 and a*(b % 10) == b*(a // 10): # a/b = c/d === a*d = b*c
                fractions.append((a, b))

    f = reduce(lambda x, y: (x[0]*y[0], x[1]*y[1]), fractions)

    return f[1]//gcd(*f)

if __name__ == "__main__":
    print(main())

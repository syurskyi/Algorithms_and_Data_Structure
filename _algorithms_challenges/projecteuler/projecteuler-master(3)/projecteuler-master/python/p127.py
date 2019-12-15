#!/usr/bin/env python

"""Problem 127: abc-hits"""

from math import gcd


def main():
    lim = 120000

    rads = [1]*lim

    for i in range(2, lim):
        if rads[i] == 1:
            for j in range(i, lim, i):
                rads[j] *= i

    numbers = sorted(range(1, lim), key=rads.__getitem__)

    s = 0

    for c in range(3, lim):
        for a in numbers:
            if a >= c // 2:  # ensure b > a
                continue

            if rads[a]*rads[c] >= c:
                break

            b = c - a

            # gcd(a, b) == 1 implies gcd(a, c) == gcd(b, c) == 1
            if rads[a]*rads[b]*rads[c] < c and gcd(a, b) == 1:
                s += c
    return s


if __name__ == "__main__":
    print(main())

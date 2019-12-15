#!/usr/bin/env python

"""Problem 129: Repunit divisibility"""

from itertools import count
from math import ceil, log10


def main():
    lim = 1_000_000

    for n in count(lim if lim & 1 else lim + 1, 2):  # A(n) <= n
        if n % 5:
            k = ceil(log10(n*3))
            r = (10**k-1)//9

            while r:
                r = (r*10 + 1) % n
                k += 1

            if k > lim:
                return n

if __name__ == "__main__":
    print(main())

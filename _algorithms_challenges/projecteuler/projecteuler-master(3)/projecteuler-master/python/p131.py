#!/usr/bin/env python

"""Problem 131: Prime cube partnership"""

from itertools import count

from utils import is_prime


def main():
    lim = 1_000_000
    res = 0

    for x in count(1):
        n = (x+1)**3 - x**3
        if n > lim:
            break
        if is_prime(n):
            res += 1
    return res


if __name__ == "__main__":
    print(main())

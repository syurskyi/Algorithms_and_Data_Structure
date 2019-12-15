#!/usr/bin/env python

"""Problem 35: Circular primes"""

from itertools import repeat

from utils import prime_sieve


def rotations(n):
    """
    Generate rotations of a number (including the number itself).
    May produce duplicates.
    """

    # this is faster than using math.log10()
    k = 5 if n > 100000 else \
        4 if n > 10000 else \
        3 if n > 1000 else \
        2 if n > 100 else \
        1 if n > 10 else \
        0

    for _ in repeat(None, k+1):
        n = 10**k * (n % 10) + n // 10
        yield n


def main():
    primes = prime_sieve(1000000)
    primes_set = set(primes)

    cnt = 0

    for p in primes:
        for r in rotations(p):
            if r not in primes_set:
                break
        else:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 134: Prime pair connection"""

from itertools import tee
from math import ceil, log10

from utils import prime_sieve_lazy


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    lim = 1_000_000
    primes = prime_sieve_lazy()
    next(primes)
    next(primes)
    res = 0

    # p1 + d * k == 0 (mod p2).
    for p1, p2 in pairwise(primes):
        if p1 > lim:
            break
        d = 10**(ceil(log10(p1)))
        dinv = pow(d, p2 - 2, p2)
        k = ((p2 - p1) * dinv) % p2
        res += p1 + d * k

    return res


if __name__ == "__main__":
    print(main())

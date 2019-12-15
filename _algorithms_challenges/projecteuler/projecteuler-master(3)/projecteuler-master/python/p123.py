#!/usr/bin/env python

"""Problem 123: Prime square remainders"""

from itertools import islice

from utils import prime_sieve_lazy


def main():
    for n, p in islice(enumerate(prime_sieve_lazy(), 1), 0, None, 2):
        if 2*p*n > 10**10:
            return n


if __name__ == "__main__":
    print(main())

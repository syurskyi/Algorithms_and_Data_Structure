#!/usr/bin/env python

"""Problem 10: Summation of primes"""

from utils import prime_sieve


def main():
    lim = 2000000
    return sum(prime_sieve(lim))


if __name__ == "__main__":
    print(main())

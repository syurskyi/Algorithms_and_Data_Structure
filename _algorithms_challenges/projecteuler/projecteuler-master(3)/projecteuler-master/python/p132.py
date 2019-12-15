#!/usr/bin/env python

"""Problem 132: Large repunit factors"""

from utils import prime_sieve_lazy


def main():
    factors = []

    for prime in prime_sieve_lazy():
        if pow(10, 10**9, 9*prime) == 1:  # R(k) = (10**k - 1) // 9
            factors.append(prime)
            if len(factors) == 40:
                return sum(factors)


if __name__ == "__main__":
    print(main())

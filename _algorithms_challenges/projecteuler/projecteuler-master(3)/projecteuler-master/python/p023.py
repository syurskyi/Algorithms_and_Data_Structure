#!/usr/bin/env python

"""Problem 23: Non-abundant sums"""

from math import sqrt

from utils import prime_sieve, sum_of_proper_divisors


def main():
    LIMIT = 28123
    primes = prime_sieve(int(sqrt(LIMIT)))
    a_numbers = [i for i in range(12, LIMIT+1) if sum_of_proper_divisors(i, primes) > i]
    a_numbers_set = frozenset(a_numbers)

    def not_sum(n):
        lim = n//2

        for a in a_numbers:
            if a > lim:
                break

            if n - a in a_numbers_set:
                return False

        return True

    return sum(filter(not_sum, range(LIMIT, 0, -1)))

if __name__ == "__main__":
    print(main())

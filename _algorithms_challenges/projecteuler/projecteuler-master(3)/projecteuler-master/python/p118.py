#!/usr/bin/env python

"""Problem 118: Pandigital prime sets"""

from functools import lru_cache
from itertools import permutations

from utils import prime_sieve


def main():
    primes = prime_sieve(100_000)

    @lru_cache(maxsize=None)
    def is_prime(n, primes=primes, primes_set=frozenset(primes)):
        if n < 100_000:
            return n in primes_set

        for p in primes:
            if not n % p:
                return False
            if p*p > n:
                return True

    def count_sets(cnt, prev, digits):
        if not digits:
            return cnt + 1

        for i in range(1, len(digits)+1):
            for p in permutations(digits, i):
                if i == 1:
                    if p[0] not in "2357":
                        continue
                elif p[-1] not in "1379":
                    continue

                x = int("".join(p))

                if x > prev and is_prime(x):
                    cnt = count_sets(cnt, x, digits.difference(p))
        return cnt

    return count_sets(0, 0, frozenset("123456789"))


if __name__ == "__main__":
    print(main())

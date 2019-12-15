#!/usr/bin/env python

"""Problem 60: Prime pair sets"""

from functools import lru_cache

from utils import is_prime, prime_sieve


def main():
    primes = prime_sieve(8500)

    @lru_cache(maxsize=None)
    def check(p1, p2):
        return is_prime(int(f'{p1}{p2}')) and is_prime(int(f'{p2}{p1}'))

    def candidates(p):
        for i in range(p[-1]+1, len(primes)):
            if all(check(primes[i], primes[j]) for j in p):
                if len(p) == 4:
                    yield (*p, i)
                else:
                    yield from candidates((*p, i))

    for i in range(len(primes)):
        try:
            quint = next(candidates((i,)))
            return sum(primes[x] for x in quint)
        except StopIteration:
            pass


if __name__ == "__main__":
    print(main())

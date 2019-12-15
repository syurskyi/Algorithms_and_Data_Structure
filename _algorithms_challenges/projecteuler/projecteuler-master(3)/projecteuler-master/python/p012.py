#!/usr/bin/env python

"""Problem 12: Highly divisible triangular number"""

from functools import lru_cache, partial
from itertools import count

from utils import num_of_divisors, prime_sieve

num_of_divisors = lru_cache(maxsize=None)(partial(num_of_divisors,
                                                  primes=prime_sieve(1000)))

def main():
    for n in count(1):
        divisors = (num_of_divisors((n+1)//2) * num_of_divisors(n) if n & 1
                    else num_of_divisors(n//2) * num_of_divisors(n+1))

        if divisors >= 500:
            return n*(n + 1)//2


if __name__ == "__main__":
    print(main())

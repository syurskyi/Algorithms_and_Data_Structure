#!/usr/bin/env python

"""Problem 70: Totient permutation"""

from bisect import bisect_left
from heapq import heappop, heappush

from utils import is_permutation, prime_sieve


def main():
    # n cannot be prime^k (k = [1, 2, ...]) because prime^k and phi(prime^k)
    # cannot be a permutation of each other

    lim = 10**7
    primes = prime_sieve(4000)
    last_idx = len(primes)-1
    # the max prime <= sqrt(10**7) is 3137
    middle_idx = bisect_left(primes, 3137)

    def candidate_primes(low_idx):
        for high_idx in range(last_idx, low_idx, -1):
            if primes[low_idx]*primes[high_idx] <= lim:
                yield high_idx

    class Number(object):
        """Number which is the product of two primes"""

        def __init__(self, low_idx, gen):
            self.low_idx = low_idx
            self.gen = gen
            low = primes[low_idx]
            high = primes[next(gen)]
            self.number = low*high
            self.phi = (low-1)*(high-1)

        def __lt__(self, other):
            return self.number*other.phi < other.number*self.phi

    queue = []

    for low_idx in range(middle_idx, -1, -1):
        heappush(queue, Number(low_idx, candidate_primes(low_idx)))

    while queue:
        number = heappop(queue)

        if is_permutation(number.number, number.phi):
            return number.number

        try:
            heappush(queue, Number(number.low_idx, number.gen))
        except StopIteration:
            pass

if __name__ == "__main__":
    print(main())

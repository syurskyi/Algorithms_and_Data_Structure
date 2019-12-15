#!/usr/bin/env python

"""Problem 49: Prime permutations"""

from utils import prime_sieve


def main():
    primes = [p for p in prime_sieve(10000)
              if p > 1000 and p not in {1487, 4817, 8147}]
    primes_set = frozenset(primes)

    def anagram_hash(num, primes=primes):
        """
        Calculate a unique signature or perfect hash by multiplying prime
        numbers corresponding to each digit in a number.
        """
        sig = 1
        while num:
            sig *= primes[num % 10]
            num //= 10
        return sig

    for p1 in primes:
        p2 = p1 + 3330
        p3 = p1 + 6660
        if (p2 in primes_set and p3 in primes_set and
                anagram_hash(p1) == anagram_hash(p2) == anagram_hash(p3)):
            return f"{p1}{p2}{p3}"


if __name__ == "__main__":
    print(main())

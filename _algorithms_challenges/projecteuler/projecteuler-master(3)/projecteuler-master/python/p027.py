#!/usr/bin/env python

"""Problem 27: Quadratic primes"""

from utils import prime_sieve


def main():
    primes = prime_sieve(20000)
    primes_set = frozenset(primes)

    t = product = 0

    for b in primes: # b has to be prime (0^2+0*a+b=b)
        if b > 1000:
            break

        for a in (p - b - 1 for p in primes): # n=1, a+b+1 has to be prime
            if a > 1000:
                break

            n = 0
            while n*n + a*n + b in primes_set:
                if n > t:
                    t, product = n, a*b
                n += 1

    return product

if __name__ == "__main__":
    print(main())

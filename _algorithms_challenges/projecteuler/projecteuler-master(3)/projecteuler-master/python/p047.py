#!/usr/bin/env python

"""Problem 47: Distinct primes factors"""

from math import sqrt


def main():
    lim = 1000000
    sieve = [0]*lim

    for i in range(2, int(sqrt(lim))+1):
        if not sieve[i]: # prime
            for k in range(i+i, lim, i):
                sieve[k] += 1
    l = [4]*4
    for i in range(2, len(sieve)-4):
        if sieve[i:i+4] == l:
            return i

if __name__ == "__main__":
    print(main())

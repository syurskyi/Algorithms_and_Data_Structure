#!/usr/bin/env python

"""Problem 50: Consecutive prime sum"""

from utils import prime_sieve


def main():
    lim = 1000000
    primes = prime_sieve(lim)
    primes_set = frozenset(primes)

    cnt, res = 21, 953

    for i in range(len(primes)-21):
        s = primes[i]

        for k in range(i+1, len(primes)):
            s += primes[k]

            if s > lim: break

            if s in primes_set and k - i > cnt:
                cnt = k - i
                res = s

    return res

if __name__ == "__main__":
    print(main())

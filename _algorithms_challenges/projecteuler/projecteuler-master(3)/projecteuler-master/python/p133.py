#!/usr/bin/env python

"""Problem 133: Repunit nonfactors"""


from utils import prime_sieve


def main():
    primes = prime_sieve(100_000)
    res = 0

    for prime in primes:
        if prime < 7:
            res += prime
            continue
        f1, f2 = prime - 1, 1
        while f1 % 2 == 0:
            f1 //= 2
            f2 *= 2
        while f1 % 5 == 0:
            f1 //= 5
            f2 *= 5
        if f1 == 1 or pow(10, f2, prime) == 1:
            continue
        res += prime

    return res


if __name__ == "__main__":
    print(main())

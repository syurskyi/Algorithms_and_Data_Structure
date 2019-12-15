#!/usr/bin/env python

"""Problem 37: Truncatable primes"""

from math import log10

from utils import is_prime, prime_sieve_lazy


def is_truncatable(p):  # check if the prime is right-/left-truncatable
    if p < 10:
        return False
    t = p // 10

    while t > 0:
        if not is_prime(t):
            return False
        t //= 10

    k = int(log10(p))
    t = p % 10**k

    while t > 0:
        if not is_prime(t):
            return False
        k -= 1
        t %= 10**k

    return True


def main():
    res = cnt = 0

    for p in prime_sieve_lazy():
        if is_truncatable(p):
            res += p
            cnt += 1

            if cnt == 11:
                return res


if __name__ == "__main__":
    print(main())

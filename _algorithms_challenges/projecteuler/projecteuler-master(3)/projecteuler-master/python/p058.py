#!/usr/bin/env python

"""Problem 58: Spiral primes"""

from math import sqrt

from utils import prime_sieve

primes = prime_sieve(20000)
primes_set = set(primes)


def is_prime(n, primes=primes, primes_set=primes_set):

    if n in primes_set:
        return True

    max_divisor = int(sqrt(n))

    for prime in primes:
        if not n % prime:
            return False

        if prime > max_divisor:
            return True

    # all primes are of the form c#k + i for i < c# and i coprime to c#
    # let c = 6, c# = 2*3*5 = 30

    divisor = 19980

    while divisor <= max_divisor:
        if not (n % (divisor + 1) and n % (divisor + 7) and n % (divisor + 11) and
                n % (divisor + 13) and n % (divisor + 17) and n % (divisor + 19) and
                n % (divisor + 23) and n % (divisor + 29)):
            return False
        divisor += 30

    return True


def main():
    number = 1
    cnt = 0
    step = 2
    primes_cnt = 0

    while True:
        cnt += 1
        number += step

        if cnt & 3:  # only the first 3 diagonals contain primes
            primes_cnt += is_prime(number)
        else:
            # layer done
            if primes_cnt/(2*step+1) < 0.1:  # ratio below 10%
                return 1+step
            step += 2

if __name__ == "__main__":
    print(main())

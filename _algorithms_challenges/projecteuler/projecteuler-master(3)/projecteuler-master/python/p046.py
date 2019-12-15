#!/usr/bin/env python

"""Problem 46: Goldbach's other conjecture"""

from utils import is_prime


def main():
    primes = {2}
    n = 3

    while True:
        if is_prime(n):
            primes.add(n)
        else:
            i = 1
            while 2*i*i < n:
                if n - 2*i*i in primes:
                    break
                i += 1
            else:
                return n
        n += 2

if __name__ == "__main__":
    print(main())

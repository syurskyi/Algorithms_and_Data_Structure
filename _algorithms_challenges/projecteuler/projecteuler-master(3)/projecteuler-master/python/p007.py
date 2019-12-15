#!/usr/bin/env python

"""Problem 7: 10001st prime"""

from utils import prime_sieve_lazy


def main():
    for count, prime in enumerate(prime_sieve_lazy(), 1):
        if count == 10001:
            return prime

if __name__ == "__main__":
    print(main())

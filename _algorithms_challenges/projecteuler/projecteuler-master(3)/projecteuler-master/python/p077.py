#!/usr/bin/env python

"""Problem 77: Prime summations"""

from itertools import count

from utils import prime_sieve_lazy


def main():
    nways = 5000

    for num in count(10):
        ways = [0]*(num+1)
        ways[0] = 1

        for p in prime_sieve_lazy():
            if p > num:
                break

            for i in range(p, num+1):
                ways[i] += ways[i-p]

        if ways[num] > nways:
            return num


if __name__ == "__main__":
    print(main())

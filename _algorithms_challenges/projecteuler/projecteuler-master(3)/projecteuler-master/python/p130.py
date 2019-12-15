#!/usr/bin/env python

"""Problem 130: Composites with prime repunit property"""

from itertools import count

from utils import is_prime


def main():
    composites = []

    for n in count(9, 2):
        # A(n) divides n-1 iff 10^(n-1)=1 (mod 9*n)
        if n % 5 and not is_prime(n) and pow(10, n - 1, 9*n) == 1:
            composites.append(n)
            if len(composites) == 25:
                return sum(composites)


if __name__ == "__main__":
    print(main())

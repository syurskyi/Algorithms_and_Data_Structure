#!/usr/bin/env python

"""Problem 9: Special Pythagorean triplet"""

from utils import pythagorean_triplets


def main():
    # There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    a, b, c = next(pythagorean_triplets(1000))
    return a*b*c

if __name__ == "__main__":
    print(main())

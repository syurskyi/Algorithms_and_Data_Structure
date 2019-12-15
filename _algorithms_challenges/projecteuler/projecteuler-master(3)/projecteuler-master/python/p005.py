#!/usr/bin/env python

"""Problem 5: Smallest multiple"""

from math import gcd


def main():
    multiple = 1
    for i in range(2, 21):
        multiple *= i // gcd(i, multiple)
    return multiple

if __name__ == "__main__":
    print(main())

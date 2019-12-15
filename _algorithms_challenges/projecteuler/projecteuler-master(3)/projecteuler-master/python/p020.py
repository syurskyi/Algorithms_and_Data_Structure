#!/usr/bin/env python

"""Problem 20: Factorial digit sum"""

from math import factorial


def main():
    return sum(int(d) for d in str(factorial(100)))

if __name__ == "__main__":
    print(main())

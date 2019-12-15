#!/usr/bin/env python

"""Problem 97: Large non-Mersenne prime"""


def main():
    return (28433 * pow(2, 7830457, 10**10) + 1) % 10**10

if __name__ == "__main__":
    print(main())

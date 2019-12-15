#!/usr/bin/env python

"""Problem 24: Lexicographic permutations"""

from math import factorial


def main():
    def nth_perm(s, n):
        if len(s) < 2:
            return s
        quot, n = divmod(n, factorial(len(s)-1))
        return s[quot] + nth_perm(s[:quot] + s[quot+1:], n)

    return nth_perm('0123456789', 999999)


if __name__ == '__main__':
    print(main())

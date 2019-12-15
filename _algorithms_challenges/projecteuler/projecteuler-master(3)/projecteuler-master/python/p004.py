#!/usr/bin/env python

"""Problem 4: Largest palindrome product"""

from utils import is_palindrome


def main():
    n = 0

    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            k = x*y
            if k <= n:
                break
            if is_palindrome(k):
                n = k
    return n

if __name__ == "__main__":
    print(main())

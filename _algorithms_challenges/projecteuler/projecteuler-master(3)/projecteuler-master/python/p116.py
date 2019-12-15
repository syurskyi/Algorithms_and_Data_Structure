#!/usr/bin/env python

"""Problem 116: Red, green or blue tiles"""

from itertools import repeat


def main():
    row_len = 50
    cnt = 0

    # red, f(n) = f(n-1) + f(n-2)
    a, b = 1, 2
    for _ in repeat(None, row_len-2):
        a, b = b, b + a

    cnt += b

    # green, f(n) = f(n-1) + f(n-3)
    a, b, c = 1, 1, 2
    for _ in repeat(None, row_len-3):
        a, b, c = b, c, c + a

    cnt += c

    # blue, f(n) = f(n-1) + f(n-4)
    a, b, c, d = 1, 1, 1, 2
    for _ in repeat(None, row_len-4):
        a, b, c, d = b, c, d, d + a

    cnt += d

    return cnt - 3


if __name__ == "__main__":
    print(main())

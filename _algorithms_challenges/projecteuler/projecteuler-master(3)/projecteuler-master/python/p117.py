#!/usr/bin/env python

"""Problem 117: Red, green, and blue tiles"""

from itertools import repeat


def main():
    row_len = 50
    a, b, c, d = 1, 2, 4, 8

    for _ in repeat(None, row_len - 4):
        a, b, c, d = b, c, d, a + b + c + d

    return d  # this is also the 54th tetranacci number


if __name__ == "__main__":
    print(main())

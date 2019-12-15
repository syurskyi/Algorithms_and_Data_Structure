#!/usr/bin/env python

"""Problem 45: Triangular, pentagonal, and hexagonal"""

from utils import hexagonal_numbers, is_pentagonal


def main():
    cnt = 0

    for num in hexagonal_numbers():
        if is_pentagonal(num):  # Every hexagonal number is a triangular number
            cnt += 1
            if cnt == 3:
                return num


if __name__ == "__main__":
    print(main())

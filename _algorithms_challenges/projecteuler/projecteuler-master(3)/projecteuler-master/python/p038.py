#!/usr/bin/env python

"""Problem 38: Pandigital multiples"""

from itertools import permutations

from utils import is_pandigital


def main():
    # The number to beat is 918273645.
    # The starting number can't be in the form 9X or 9XX, as that would
    # produce too few or too many digits. Thus, it must be in the form 9XXX.

    for digits in permutations("987654321", 4):
        start = "".join(digits)
        prod = start + str(int(start)*2)

        if is_pandigital(int(prod)):
            return prod

if __name__ == "__main__":
    print(main())

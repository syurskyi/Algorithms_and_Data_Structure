#!/usr/bin/env python

"""Problem 30: Digit fifth powers"""

from itertools import combinations_with_replacement


def main():
    digits = "0123456789"
    powers = {d: i**5 for i, d in enumerate(digits)}

    psums = {1}

    # max possible number is 6*9^5, which has 6 digits
    for i in range(2, 7):
        for d in combinations_with_replacement(digits, i):
            p = sum([powers[x] for x in d])

            if p == sum([powers[x] for x in str(p)]):
                psums.add(p)
    return sum(psums) - 1

if __name__ == "__main__":
    print(main())

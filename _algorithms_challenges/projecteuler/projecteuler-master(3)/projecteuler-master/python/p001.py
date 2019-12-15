#!/usr/bin/env python

"""Problem 1: Multiples of 3 and 5"""

from utils import arithmetic_series


def main():
    lim = 999
    return (arithmetic_series(3, lim//3*3, lim//3) +
            arithmetic_series(5, lim//5*5, lim//5) -
            arithmetic_series(15, lim//15*15, lim//15))

if __name__ == "__main__":
    print(main())

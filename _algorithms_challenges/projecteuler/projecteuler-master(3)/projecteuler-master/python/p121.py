#!/usr/bin/env python

"""Problem 121: Disc game prize fund"""

from functools import reduce
from itertools import chain, combinations
from math import factorial
from operator import mul


def main():
    turns = 15
    prob = sum(reduce(mul, reds, 1) for reds in chain.from_iterable(
        combinations(range(1, turns+1), n) for n in range((turns+1)//2)))
    return factorial(turns+1) // prob


if __name__ == "__main__":
    print(main())

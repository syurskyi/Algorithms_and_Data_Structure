#!/usr/bin/env python

"""Problem 39: Integer right triangles"""

from utils import pythagorean_triplets


def main():
    s = p = 0

    for perimeter in range(12, 1001, 4): # the perimeter is always divisible by 4
        solutions = len(list(pythagorean_triplets(perimeter)))
        if solutions > s:
            s = solutions
            p = perimeter
    return p

if __name__ == "__main__":
    print(main())

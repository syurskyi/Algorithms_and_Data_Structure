#!/usr/bin/env python

"""Problem 91: Right triangles with integer coordinates"""

from math import gcd


def main():
    N = 50
    triangles = 0

    for x in range(1, N+1):  # run
        for y in range(1, N+1):  # rise
            gcf = gcd(x, y)

            Δx = y//gcf
            Δy = x//gcf

            triangles += min(y//Δy, (N-x)//Δx)

    triangles *= 2  # account for the symmetry
    triangles += N*N*3  # count triangles on the axes

    return triangles

if __name__ == "__main__":
    print(main())

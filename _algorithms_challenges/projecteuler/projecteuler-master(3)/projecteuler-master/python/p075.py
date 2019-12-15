#!/usr/bin/env python

"""Problem 75: Singular integer right triangles"""

from math import gcd, sqrt


def main():
    limit = 1500000
    perimeters = [0]*(limit + 1)

    for m in range(2, int(sqrt(limit>>1))):
        for n in range(2 if m&1 else 1, m, 2):
            if gcd(m, n) == 1:

                p = 2*m*(m+n)  # a + b + c

                if p <= limit:
                    for i in range(p, limit, p):
                        perimeters[i] += 1

    return perimeters.count(1)


if __name__ == "__main__":
    print(main())

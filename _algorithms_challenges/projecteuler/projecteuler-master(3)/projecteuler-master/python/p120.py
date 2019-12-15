#!/usr/bin/env python

"""Problem 120: Square remainders"""


def main():
    # r == 2*a*n % (a*a) for n odd, and 2 for n even.
    # For a ≥ 3, 2 < 2*1*a < a*a, so the maximal remainder is obtained for
    # some odd exponent n. To maximize r, 2*n must be the largest
    # even number less than a.
    return sum(2*a*a - a - 1 for a in range(3, 1001, 2))


if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 44: Pentagon numbers"""

from itertools import count

from utils import is_pentagonal


def main():
    # P(n+k)-P(n) = 3kn + P(k), P(n+k)-P(n) = P(m)
    pm = 1
    for m in count(1):
        if not pm & 1:  # both numbers must be even
            pk = 1
            for k in range(1, m):
                if not (pm - pk) % (3*k):
                    n = (pm - pk) // (3*k)
                    if is_pentagonal(pm + n*(3*n - 1)):
                        return pm
                pk += 3*k + 1
        pm += 3*m + 1

if __name__ == "__main__":
    print(main())

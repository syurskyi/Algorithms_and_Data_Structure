#!/usr/bin/env python

"""Problem 90: Cube digit pairs"""

from itertools import combinations


def main():
    cnt = 0

    # "10 choose 6" == 210 combinations
    cubes = tuple(combinations(range(10), 6))

    for first in cubes:
        for second in cubes:
            if second >= first:
                break

            if ((0 in first and 1 in second or 0 in second and 1 in first)
                and
                (0 in first and 4 in second or 0 in second and 4 in first)
                and
                (0 in first and (9 in second or 6 in second) or 0 in second and (9 in first or 6 in first))
                and
                (1 in first and (6 in second or 9 in second) or 1 in second and (6 in first or 9 in first))
                and
                (2 in first and 5 in second or 2 in second and 5 in first)
                and
                (3 in first and (6 in second or 9 in second) or 3 in second and (6 in first or 9 in first))
                and
                # this check works for both 49 & 64
                (4 in first and (9 in second or 6 in second) or 4 in second and (9 in first or 6 in first))
                and
                (8 in first and 1 in second or 8 in second and 1 in first)):

                cnt += 1
    return cnt

if __name__ == "__main__":
    print(main())

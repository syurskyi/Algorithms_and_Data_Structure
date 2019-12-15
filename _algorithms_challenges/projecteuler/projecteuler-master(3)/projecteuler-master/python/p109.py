#!/usr/bin/env python

"""Problem 109: Darts"""

from itertools import combinations_with_replacement


def main():
    scores = [0, 25, 50] + [j*i for i in range(1, 21) for j in range(1, 4)]
    doubles = list(range(2, 41, 2)) + [50]

    cnt = 0
    for c in combinations_with_replacement(scores, 2):
        for d in doubles:
            if c[0] + c[1] + d >= 100:
                break
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 81: Path sum: two ways"""

from itertools import repeat

from utils import get_path


def main():
    with get_path("data", "matrix.txt").open() as data_file:
        matrix = [[int(x) for x in line.split(",")] for line in data_file]

    sums = [[0]*80 for _ in repeat(None, 80)]
    sums[0][0] = matrix[0][0]

    for i in range(1, 80):
        sums[0][i] = sums[0][i-1] + matrix[0][i]
        sums[i][0] = sums[i-1][0] + matrix[i][0]

    for i in range(1, 80):
        for j in range(1, 80):
            sums[i][j] = matrix[i][j] + min(sums[i-1][j], sums[i][j-1])

    return sums[-1][-1]

if __name__ == "__main__":
    print(main())

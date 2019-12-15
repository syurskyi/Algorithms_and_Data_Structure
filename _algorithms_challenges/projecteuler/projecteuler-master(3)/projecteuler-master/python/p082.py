#!/usr/bin/env python

"""Problem 82: Path sum: three ways"""

from utils import get_path


def main():
    with get_path("data", "matrix.txt").open() as data_file:
        matrix = [[int(x) for x in line.split(",")] for line in data_file]

    size = len(matrix)
    best = [row[0] for row in matrix]  # first column

    for col in range(1, size):
        column = [matrix[row][col] + best[row] for row in range(size)]

        for row in range(1, size):
            if column[row-1] + matrix[row][col] < column[row]:
                column[row] = column[row-1] + matrix[row][col]

        for row in range(size-2, -1, -1):
            if column[row+1] + matrix[row][col] < column[row]:
                column[row] = column[row+1] + matrix[row][col]
        best = column

    return min(best)


if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 83: Path sum: four ways"""

from heapq import heappop, heappush
from itertools import repeat

from utils import get_path


def main():
    with get_path("data", "matrix.txt").open() as data_file:
        matrix = [[int(x) for x in line.split(",")] for line in data_file]

    size = 80
    last = size - 1
    distances = [[float("inf")]*size for _ in repeat(None, size)]
    heap = [(matrix[0][0], 0, 0)]

    # Dijkstra's algorithm, simplified
    while heap:
        distance, row, col = heappop(heap)

        # try to go up, right, down and left, if possible
        for r, c in ((row-1, col), (row, col+1), (row+1, col), (row, col-1)):
            if 0 <= r <= last >= c >= 0:
                new_distance = distance + matrix[r][c]
                if new_distance < distances[r][c]:
                    heappush(heap, (new_distance, r, c))
                    distances[r][c] = new_distance

    return distances[last][last]


if __name__ == "__main__":
    print(main())

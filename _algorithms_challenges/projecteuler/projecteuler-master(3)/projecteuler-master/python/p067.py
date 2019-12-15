#!/usr/bin/env python

"""Problem 67: Maximum path sum II"""

# This is a more difficult version of Problem 18.
import p018
from utils import get_path


def main():
    with get_path("data", "triangle.txt").open() as data_file:
        triangle = [[int(d) for d in line.split()] for line in data_file]

    return p018.main(triangle)


if __name__ == "__main__":
    print(main())

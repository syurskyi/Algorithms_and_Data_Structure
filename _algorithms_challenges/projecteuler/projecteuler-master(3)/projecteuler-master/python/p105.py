#!/usr/bin/env python

"""Problem 105: Special subset sums: testing"""

from p103 import is_special_sum_set
from utils import get_path


def main():
    with get_path("data", "sets.txt").open() as data_file:
        sets = [[int(x) for x in line.split(",")] for line in data_file]
        return sum([sum(s) for s in sets if is_special_sum_set(s)])


if __name__ == "__main__":
    print(main())

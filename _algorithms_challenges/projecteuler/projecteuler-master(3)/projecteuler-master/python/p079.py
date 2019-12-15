#!/usr/bin/env python

"""Problem 79: Passcode derivation"""

from utils import get_path


def main():
    with get_path("data", "keylog.txt").open() as data_file:
        keys = [line.rstrip() for line in data_file]

    # dict storing numbers that appear before a given number
    preceding = {c: set() for c in set().union(*keys)}

    for key in keys:
        preceding[key[1]].add(key[0])
        preceding[key[2]].add(key[1])
        preceding[key[2]].add(key[0])

    return "".join(sorted(preceding, key=preceding.get))


if __name__ == "__main__":
    print(main())

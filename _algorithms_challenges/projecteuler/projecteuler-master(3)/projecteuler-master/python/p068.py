#!/usr/bin/env python

"""Problem 68: Magic 5-gon ring"""

from operator import itemgetter


def main():
    numbers = frozenset(range(1, 11))
    sides = [0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 1]
    rotations = [itemgetter(*sides[i:], *sides[:i]) for i in range(0, len(sides), 3)]
    solutions = []
    search = [[10]]

    while search:
        ring = search.pop()
        left = numbers.difference(ring)

        if not left:
            solutions.append(min(r(ring) for r in rotations))
            continue

        for c in left:
            node = len(ring)

            if (node == 4 and ring[0] + ring[1] != ring[3] + c or
                node == 6 and ring[2] + ring[3] != ring[5] + c or
                node == 8 and ring[4] + ring[5] != ring[7] + c or
                node == 9 and ring[6] + ring[7] != ring[1] + c):
                continue
            search.append([*ring, c])

    return "".join(map(str, max(solutions)))


if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 122: Efficient exponentiation"""

from collections import deque


def main():
    lim = 200

    cache = {}
    queue = deque([[1]])

    # generate star addition chains
    while queue:
        chain = queue.popleft()

        for x in chain:
            y = chain[-1] + x
            if y > lim:
                break

            if cache.get(y, lim) >= len(chain):
                cache[y] = len(chain)
                queue.append([*chain, y])
    return sum(cache.values())


if __name__ == "__main__":
    print(main())

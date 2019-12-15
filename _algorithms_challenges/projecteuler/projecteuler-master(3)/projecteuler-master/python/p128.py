#!/usr/bin/env python

"""Problem 128: Hexagonal tile differences"""

from functools import lru_cache
from itertools import count

import utils


def main():
    target = 2000
    cnt = 2  # n == 1 in layer 0 and n == 2 in layer 1 satisfy PD(n) = 3
    is_prime = lru_cache(maxsize=None)(utils.is_prime)

    for layer in count(2):
        if (is_prime(layer * 6 - 1) and is_prime(layer * 6 + 1) and
                is_prime(layer * 12 + 5)):
            cnt += 1
            if cnt == target:
                return layer * (layer - 1) * 3 + 2
        if (is_prime(layer * 6 - 1) and is_prime(layer * 6 + 5) and
                is_prime(layer * 12 - 7)):
            cnt += 1
            if cnt == target:
                return layer * (layer + 1) * 3 + 1


if __name__ == "__main__":
    print(main())

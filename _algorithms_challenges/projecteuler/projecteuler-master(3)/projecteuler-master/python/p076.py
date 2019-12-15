#!/usr/bin/env python

"""Problem 76: Counting summations"""

from functools import lru_cache


def main():

    @lru_cache(maxsize=None)
    def count(k, n):
        """Returns the number of summations of n using numbers >= k"""
        if k == n:
            return 1
        if k > n:
            return 0
        return count(k, n-k) + count(k+1, n)

    return count(1, 100) - 1

if __name__ == "__main__":
    print(main())

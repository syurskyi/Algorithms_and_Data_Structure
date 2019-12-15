#!/usr/bin/env python

"""Problem 40: Champernowne's constant"""

def main():
    index = 0
    n = 1
    res = 1
    indexes = frozenset(10**x for x in range(7))

    while index <= 1000000:
        for c in str(n):
            index += 1
            if index in indexes:
                res *= int(c)
        n += 1

    return res

if __name__ == "__main__":
    print(main())

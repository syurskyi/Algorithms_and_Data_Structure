#!/usr/bin/env python

"""Problem 112: Bouncy numbers"""

from itertools import count


def main():

    bouncy = 0
    total = 100

    def is_bouncy(n):
        is_increasing = is_decreasing = False

        p = n % 10
        n //= 10

        while n:
            d = n % 10
            n //= 10

            if d > p:
                if is_increasing:
                    return True
                is_decreasing = True
            elif d < p:
                if is_decreasing:
                    return True
                is_increasing = True
            p = d

        return False

    for n in count(101):
        if is_bouncy(n):
            bouncy += 1
        total += 1

        if bouncy / total >= 0.99:
            return n

if __name__ == "__main__":
    print(main())

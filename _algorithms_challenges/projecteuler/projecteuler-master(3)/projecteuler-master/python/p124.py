#!/usr/bin/env python

"""Problem 124: Ordered radicals"""


def main():
    lim = 100_000

    rads = [1]*(lim+1)

    for i in range(2, lim+1):
        if rads[i] == 1:
            for j in range(i, lim+1, i):
                rads[j] *= i

    return sorted(range(lim+1), key=rads.__getitem__)[10000]


if __name__ == "__main__":
    print(main())

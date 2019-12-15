#!/usr/bin/env python

"""Problem 72: Counting fractions"""


# http://en.wikipedia.org/wiki/Farey_sequence
def main():
    lim = 1_000_000

    phis = list(range(lim+1))

    for i in range(2, lim+1):
        if phis[i] == i:  # i is a prime
            for j in range(i, lim+1, i):
                phis[j] -= phis[j]//i

    return sum(phis) - 1


if __name__ == "__main__":
    print(main())

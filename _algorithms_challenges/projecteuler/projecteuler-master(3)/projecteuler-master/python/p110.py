#!/usr/bin/env python

"""Problem 110: Diophantine reciprocals II"""

# This is a more difficult version of Problem 108

import p108


def main():
    lim = 4000000

    # the number of primes to be considered is ceil(log3(lim*2))
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    return p108.main(lim, primes)


if __name__ == "__main__":
    print(main())

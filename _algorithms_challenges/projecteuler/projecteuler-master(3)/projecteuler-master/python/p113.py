#!/usr/bin/env python

"""Problem 113: Non-bouncy numbers"""

from utils import n_choose_k


def main():
    ndigits = 100
    # numbers of combinations w/ replacement = (n + k - 1)! / k!(n - 1)!
    return sum([n_choose_k(9+k, k) + n_choose_k(8+k, k)
                for k in range(1, ndigits+1)]) - 10*ndigits

if __name__ == "__main__":
    print(main())

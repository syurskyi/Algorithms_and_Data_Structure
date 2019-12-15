#!/usr/bin/env python

"""Problem 15: Lattice paths"""

from utils import n_choose_k


def main():
    size = 20
    return n_choose_k(size+size, size)

if __name__ == "__main__":
    print(main())

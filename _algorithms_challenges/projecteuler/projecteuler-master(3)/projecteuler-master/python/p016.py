#!/usr/bin/env python

"""Problem 16: Power digit sum"""


def main():
    return sum(map(int, str(2**1000)))


if __name__ == "__main__":
    print(main())

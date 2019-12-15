#!/usr/bin/env python

"""Problem 71: Ordered fractions"""

def main():
    # http://en.wikipedia.org/wiki/Farey_sequence
    a, b, c, d = 0, 1000000, 3, 7

    while True:
        a = (b*c-1)//d
        if b*c - a*d == 1:
            return a
        b -= 1


if __name__ == "__main__":
    print(main())

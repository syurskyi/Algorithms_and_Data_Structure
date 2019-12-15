#!/usr/bin/env python

"""Problem 92: Square digit chains"""

from functools import lru_cache


def main():

    @lru_cache(maxsize=None)
    def sum_squares(num):
        """Sums the squares of the digits in a number"""
        if num == 89 or num == 1:
            return num

        a, b, c = num // 100, (num % 100) // 10, num % 10
        return sum_squares(a*a + b*b + c*c)

    # http://www.shaunspiller.com/happynumbers/
    squares = [i*i for i in range(10)]
    frequencies = [0]*(9**2 + 1)  # frequencies for 1-digit numbers

    for square in squares:
        frequencies[square] += 1

    for d in range(2, 8):  # compute frequences for 2..7-digit numbers iteratively
        tmp = [0]*(9**2*d + 1)

        for i, v in enumerate(frequencies):
            for square in squares:
                tmp[i + square] += v

        frequencies = tmp

    return sum([v for i, v in enumerate(frequencies[1:], 1) if sum_squares(i) == 89])


if __name__ == "__main__":
    print(main())

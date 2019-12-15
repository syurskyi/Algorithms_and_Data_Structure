#!/usr/bin/env python

"""Problem 61: Cyclical figurate numbers"""

from operator import itemgetter

from utils import (nth_heptagonal, nth_hexagonal, nth_octagonal,
                   nth_pentagonal, nth_square, nth_triangle)


def is_cyclic(m, n):
    return m % 100 == n // 100


def main():
    numbers = [  # the ranges can be figured out using the respective formulas
        [nth_triangle(i) for i in range(45, 141)],  # 4-digit triangle numbers
        [nth_square(i) for i in range(31, 100)],  # 4-digit square numbers
        [nth_pentagonal(i) for i in range(25, 82)],
        [nth_hexagonal(i) for i in range(22, 71)],
        [nth_heptagonal(i) for i in range(20, 64)],
        [nth_octagonal(i) for i in range(18, 59)]
    ]

    def get_number(n):
        return numbers[n[0]][n[1]]

    types = set(range(6))
    typegetter = itemgetter(0)

    def search(n):
        if len(n) == 6:
            if is_cyclic(*map(get_number, (n[-1], n[0]))):
                return n
            return

        unused_types = types - set(map(typegetter, n))
        this_num = get_number(n[-1])

        for u in unused_types:
            for k in range(len(numbers[u])):
                if is_cyclic(this_num, numbers[u][k]):
                    s = search(n+[(u, k)])
                    if s:
                        return s

    for i in range(len(numbers[5])):  # start from the octagonal numbers
        s = search([(5, i)])
        if s:
            return sum(map(get_number, s))


if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 93: Arithmetic expressions"""

from functools import reduce
from itertools import combinations, permutations, product
from operator import add, mul, sub, truediv


def calc_consecutive(targets):
    """Return the number of consecutive integers 1 to n in a set"""
    i = 0
    while i+1 in targets:
        i += 1
    return i


def main():
    max_consecutive = 0
    operations = (add, sub, mul, truediv)

    for digits in combinations(range(1, 10), 4):
        targets = set()
        for a, b, c, d in permutations(digits, 4):
            for first_op, second_op, third_op in product(operations, repeat=3):
                # each expression can be parenthesized in 5 different ways:
                # ((ab)c)d, (ab)(cd), (a(bc))d, a((bc)d), a(b(cd))

                targets.add(third_op(second_op(first_op(a, b), c), d))
                targets.add(second_op(first_op(a, b), third_op(c, d)))
                targets.add(third_op(first_op(a, second_op(b, c)), d))

                # these two can raise ZeroDivisionError
                try:
                    targets.add(first_op(a, third_op(second_op(b, c), d)))
                except ZeroDivisionError:
                    pass

                try:
                    targets.add(first_op(a, second_op(b, third_op(c, d))))
                except ZeroDivisionError:
                    pass

        cons = calc_consecutive(targets)
        if cons > max_consecutive:
            max_consecutive = cons
            answer = digits

    return reduce(lambda x, y: x*10 + y, answer)


if __name__ == "__main__":
    print(main())

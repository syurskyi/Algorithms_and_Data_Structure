#!/usr/bin/env python

"""Problem 111: Primes with runs"""

from functools import reduce
from itertools import combinations, product

from utils import is_prime


def main():
    D = 10
    digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    total = 0

    for d in digits:
        for n in range(D-1, 0, -1):
            if d == 0 and n == D-1:
                continue
            S = 0
            for indexes in combinations(range(D), n):
                repeating = [d if i in indexes else None for i in range(D)]

                for others in product(digits[:d] + digits[d+1:], repeat=D-n):
                    others = iter(others)
                    num = [next(others) if x is None else x for x in repeating]

                    if num[0] and num[-1] in {1, 3, 7, 9} and sum(num) % 3:
                        x = reduce(lambda x, y: x*10 + y, num)
                        if is_prime(x):
                            S += x
            if S:
                total += S
                break
    return total


if __name__ == "__main__":
    print(main())

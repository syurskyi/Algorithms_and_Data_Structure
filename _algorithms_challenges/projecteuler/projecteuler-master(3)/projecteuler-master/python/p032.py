#!/usr/bin/env python

"""Problem 32: Pandigital products"""

from itertools import permutations

from utils import is_pandigital


def main():
    products = set()
    digits = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    # The factors must either be 1, 4 or 2, 3 digits.

    # skip 1 (1 x N == N)
    for a in digits[1:]:
        for b in permutations([d for d in digits if d != a], 4):
            b = b[0]*1000 + b[1]*100 + b[2]*10 + b[3]
            prod = a*b
            if prod > 9876:
                break
            if is_pandigital(a*10**8 + b*10**4 + prod):
                products.add(prod)

    for perm in permutations(digits, 2):
        a = perm[0]*10 + perm[1]
        for b in permutations([d for d in digits if d not in perm], 3):
            b = b[0]*100 + b[1]*10 + b[2]
            prod = a*b
            if prod > 9876:
                break
            if is_pandigital(a*10**7 + b*10**4 + prod):
                products.add(prod)

    return sum(products)

if __name__ == "__main__":
    print(main())

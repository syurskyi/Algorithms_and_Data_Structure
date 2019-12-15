#!/usr/bin/env python

"""Problem 108: Diophantine reciprocals I"""

from functools import reduce


def num_of_divisors(f):
    """Get the number of divisors of n^2 from prime factors of n"""
    return reduce(lambda x, y: x*(2*y[1]+1), f, 1)


def num(f):
    """Get the number from its prime factors"""
    return reduce(lambda x, y: x*(y[0]**y[1]), f, 1)


def main(lim=1000,
         # the number of primes to be considered is ceil(log3(lim*2))
         primes=(2, 3, 5, 7, 11, 13, 17)):

    min_n = float("inf")
    lim = lim*2 - 1

    factors = [[[x, 1] for x in primes[:i]] for i in range(1, len(primes)+1)]
    solutions = 1 << len(primes)+1

    while factors:
        f = factors.pop()
        # if a bigger number of distinct primes produced no solutions, then
        # we're done.
        if not solutions & (1 << len(f)+1):
            break

        if num_of_divisors(f) > lim and num(f) < min_n:
            min_n = num(f)
            solutions |= 1 << len(f)

        new = f

        for i in range(len(f)):
            new = [x[:] for x in new]
            new[i][1] += 1
            if num(new) >= min_n:
                break
            factors.append(new)
    return min_n


if __name__ == "__main__":
    print(main())

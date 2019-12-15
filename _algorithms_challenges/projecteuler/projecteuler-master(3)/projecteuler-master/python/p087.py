#!/usr/bin/env python

"""Problem 87: Prime power triples"""

from utils import prime_sieve


def main():
    lim = 50*10**6
    lim_square = int((lim - 2**3 - 2**4) ** (1/2))
    lim_cube = int((lim - 2**2 - 2**4) ** (1/3))
    lim_fourth = int((lim - 2**2 - 2**3) ** (1/4))

    primes = prime_sieve(lim_square)

    squares = [p**2 for p in primes]
    cubes = [p**3 for p in primes if p <= lim_cube]
    fourths = [p**4 for p in primes if p <= lim_fourth]

    numbers = set([
        square + cube + fourth
            for fourth in fourths
            for cube in cubes if fourth + cube < lim
            for square in squares if fourth + cube + square < lim
    ])

    return len(numbers)

if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 74: Digit factorial chains"""

from itertools import combinations_with_replacement


def main():
    factorials = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
    cache = {0: 2, 1: 1, 145: 1, 169: 3, 871: 2, 872: 2, 69: 5, 78: 4, 540: 2}

    def get_chain_len(n, factorials=factorials, cache=cache):
        """Return chain length for a given number"""
        if n in cache:
            return cache[n]
        chain = [n]

        while True:
            fsum = 0

            while n:
                fsum += factorials[n % 10]
                n //= 10

            if fsum in cache:
                length = cache[fsum] + len(chain)
                for i, v in enumerate(chain):
                    cache[v] = length - i
                return length

            if fsum in chain:
                for i, v in enumerate(chain):
                    if v == fsum and i > 0:
                        break
                    cache[v] = len(chain) - i
                return len(chain)

            chain.append(fsum)
            n = fsum

    chains = 0

    # TODO: this solution is not complete (e.g. combinations with trailing
    # zeroes are not considered, as well as repeating permutations containing "1"s)
    for digits in combinations_with_replacement(range(10), 6):
        number = 0
        for d in digits:
            number = number*10 + d

        if get_chain_len(number) == 60:
            digits = [d for d in digits if d]  # skip leading zeroes
            ndigits = len(digits)

            # calculate the number of distinguishable permutations
            counts = [0]*10
            for digit in digits:
                counts[digit] += 1

            perms = factorials[ndigits]
            for count in counts:
                if count > 1:
                    perms //= factorials[count]
            chains += perms

            # 1 and 0 are interchangable except in the leftmost part of the number
            if counts[1]:
                chains += factorials[ndigits] - counts[1]*factorials[ndigits-1]

    return chains

if __name__ == "__main__":
    print(main())

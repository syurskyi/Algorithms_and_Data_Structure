#!/usr/bin/env python

"""Problem 14: Longest Collatz sequence"""


def main():

    lim = 1_000_000

    cache = [False]*lim
    cache[2] = 2

    def get_chain_len(n, cache=cache):
        """
        Return chain length for a number, cache final and intermediate results.
        """
        if n < lim:
            if cache[n]:
                return cache[n]
            chain_len = cache[n] = (2 + get_chain_len((3*n + 1) >> 1) if n & 1
                                    else 1 + get_chain_len(n >> 1))
        else:
            chain_len = (2 + get_chain_len((3*n + 1) >> 1) if n & 1
                         else 1 + get_chain_len(n >> 1))
        return chain_len

    longest = num = 0

    # Look only at the second half of the numbers in the range
    # Every number n ≤ lim//2 has a reverse map n*2**k in the upper half.
    for i in range(lim//2, lim):
        length = get_chain_len(i)

        if length > longest:
            longest = length
            num = i

    return num

if __name__ == "__main__":
    print(main())

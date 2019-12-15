#!/usr/bin/env python

"""Problem 95: Amicable chains"""

from utils import pdsums_sieve


def main():
    limit = 1000000
    dsums = pdsums_sieve(limit)
    max_len = min_elem = 0

    for i in range(1, limit):
        chain = [i]

        while True:
            s = dsums[i]
            dsums[i] = False

            # we always hit a chain from the lowest member
            if not s or s > limit or s < chain[0]:
                break

            if s in chain:
                start = chain.index(s)

                if len(chain)-start > max_len:
                    max_len = len(chain)-start
                    min_elem = s
                break
            chain.append(s)
            i = s
    return min_elem

if __name__ == "__main__":
    print(main())

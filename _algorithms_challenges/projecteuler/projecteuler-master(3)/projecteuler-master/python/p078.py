#!/usr/bin/env python

"""Problem 78: Coin partitions"""

from itertools import count
from math import ceil, floor, sqrt


# http://mathworld.wolfram.com/PartitionFunctionP.html
def main():
    # The first few values of the partition function (starting with p(0)=1)
    partitions = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]

    for n in count(len(partitions)):
        lower_bound = ceil(-(sqrt(24*n+1)+1)/6)
        upper_bound = floor((sqrt(24*n+1)-1)/6)

        sum_ = 0

        sign = -1 if lower_bound & 1 else 1

        for k in range(lower_bound, upper_bound+1):
            if k:
                sum_ -= sign * partitions[n - (k*(3*k+1) >> 1)]
            sign = -sign

        if not sum_ % 1000000:
            return n

        partitions.append(sum_)

if __name__ == "__main__":
    print(main())

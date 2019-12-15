#!/usr/bin/env python

"""Problem 114: Counting block combinations I"""


def main():
    row_len, tile_len = 50, 3

    ways = [0]*row_len
    ways[:tile_len+1] = [1, 1, 2, 4]

    # use the recurrent relation: f(n) = f(n-1) + f(n-4) + f(n-5) +..+ f(1) + 2
    for i in range(4, row_len):
        count = ways[i-1] + 2
        for j in range(i-tile_len):
            count += ways[j]
        ways[i] = count

    return ways[-1]


if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 115: Counting block combinations II"""


def main():
    tile_len = 50
    ways = [1]*(tile_len-1) + [2, 4]

    i = tile_len + 1
    while True:
        count = ways[i-1] + 2
        for j in range(i-tile_len):
            count += ways[j]

        if count > 1_000_000:
            return i + 1

        ways.append(count)
        i += 1


if __name__ == '__main__':
    print(main())

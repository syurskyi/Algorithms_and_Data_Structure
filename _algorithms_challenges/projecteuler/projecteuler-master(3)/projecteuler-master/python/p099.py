#!/usr/bin/env python

"""Problem 99: Largest exponential"""

from math import log2

from utils import get_path


def main():
    with get_path("data", "base_exp.txt").open() as data_file:
        line = max_val = 0

        for line_num, data in enumerate(data_file):
            base, exp = data.split(",")

            # if log(x) > log(y), than x > y; log(a^b) = b*log(a)
            val = float(exp) * log2(float(base))
            if val > max_val:
                line, max_val = line_num, val

    return line + 1


if __name__ == "__main__":
    print(main())

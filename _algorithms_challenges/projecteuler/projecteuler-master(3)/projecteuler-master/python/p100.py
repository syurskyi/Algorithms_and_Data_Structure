#!/usr/bin/env python

"""Problem 100: Arranged probability"""


def main():
    # taking n as the number of disks and k as number of blue disks, we derive
    # (2n-1)^2 - 2(2k-1)^2 = -1, or x^2 - 2y^2 = -1 (Pell Equation)
    # The fundamental solution is (1,1), and subsequent solutions are given
    # by the recurrence below.

    x = y = 1

    while x <= 2 * 10**12 - 1:
        x, y = 3*x + 4*y, 2*x + 3*y

    return (y + 1) // 2

if __name__ == "__main__":
    print(main())

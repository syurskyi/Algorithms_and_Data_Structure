#!/usr/bin/env python

"""Problem 94: Almost equilateral triangles"""


def main():
    max_perimeter = 10**9
    psum = 0
    # By writing x = (3*a +- 1)/2 and y = h, we get the Pell equation:
    # x^2 - 3*y^2 = 1.

    # fundamental solution
    x1, y1 = 2, 1

    # the first solution
    x, y = 7, 4

    sign = 1

    while 2*x <= max_perimeter:
        a = (2*x + sign*1)//3
        psum += 3*a + sign*1
        x, y, sign = x1*x + 3*y1*y, x1*y + y1*x, -sign

    return psum

if __name__ == "__main__":
    print(main())

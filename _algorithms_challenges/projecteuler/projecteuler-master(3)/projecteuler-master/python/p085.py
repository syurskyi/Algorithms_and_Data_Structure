#!/usr/bin/env python

"""Problem 85: Counting rectangles"""

def main():

    # A rectangle on a grid is bounded by two vertical grid lines and two
    # horizontal grid lines. In an a x b grid the number of rectangles is
    # C(a+1,2)*C(b+1,2) = a*(a+1)*b*(b+1)/4

    N = 2000000
    diff = N-1
    area = 0
    a = 1

    while True:
        b = 0
        nrectangles = 0
        while nrectangles < N:
            b += 1
            nrectangles = a*(a+1)*b*(b+1) >> 2

        if nrectangles - N < diff:
            diff = nrectangles - N
            area = a*b

        if N - nrectangles*(b-1)//(b+1) < diff:
            diff = N - nrectangles*(b-1)//(b+1)
            area = a*(b-1)

        if a >= b:
            break
        a += 1

    return area


if __name__ == "__main__":
    print(main())

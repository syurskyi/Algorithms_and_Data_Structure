#!/usr/bin/env python

"""Problem 101: Optimum polynomial"""


# http://en.wikipedia.org/wiki/Lagrange_polynomial
def main():
    terms = [sum([(-x)**k for k in range(11)]) for x in range(1, 11)]
    fits_sum = 1

    for n in range(2, 11):
        for i in range(1, n+1):
            t1 = t2 = 1
            for j in range(1, n+1):
                if i == j:
                    continue
                t1 *= (n+1)-j
                t2 *= i-j
            fits_sum += terms[i-1] * t1 // t2

    return fits_sum

if __name__ == "__main__":
    print(main())

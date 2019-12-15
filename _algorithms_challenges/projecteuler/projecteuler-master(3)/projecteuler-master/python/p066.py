#!/usr/bin/env python

"""Problem 66: Diophantine equation"""

# http://mathworld.wolfram.com/PellEquation.html
# http://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions
# http://en.wikipedia.org/wiki/Continued_fraction#Pell.27s_equation

from math import sqrt

from utils import convergent_fractions, sqrt_fraction_expansion


def quotients(n):
    f = sqrt_fraction_expansion(n)
    yield f.pop(0)

    while True:
        for i in f:
            yield i

def main():
    lim = 1000
    res = max_x = 0
    squares = {x*x for x in range(2, int(sqrt(lim)) + 1)}

    for d in range(2, lim+1):
        if d in squares:
            continue

        for num, den in convergent_fractions(quotients(d)):
            if num*num - d*den*den == 1:
                if num > max_x:
                    max_x, res = num, d

                break
    return res

if __name__ == "__main__":
    print(main())

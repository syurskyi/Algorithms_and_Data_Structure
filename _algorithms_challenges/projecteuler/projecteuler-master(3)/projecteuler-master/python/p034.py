#!/usr/bin/env python

"""Problem 34: Digit factorials"""

def main():
    factorials = [
        1,
        1,
        2,
        6,
        24,
        120,
        720,
        5040,
        40320,
        362880,
    ]
    res = 0

    for n in range(3, 40586): # For the proper upper bound see http://en.wikipedia.org/wiki/Factorion#Upper_bound
        s = 0
        k = n
        while k > 0:
            s += factorials[k % 10]
            k //= 10

        if n == s:
            res += n
    return res

if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 125: Palindromic sums"""

from utils import is_palindrome


def main():
    lim = 10**8
    squares = [x*x for x in range(1, 7072)]  # 7071^2 + 7072^2 > 10^8
    seen = set()

    for i in range(len(squares)-1):
        s = squares[i]
        for j in range(i+1, len(squares)):
            s += squares[j]

            if s >= lim:
                break

            if s not in seen and is_palindrome(s):
                seen.add(s)
    return sum(seen)


if __name__ == "__main__":
    print(main())

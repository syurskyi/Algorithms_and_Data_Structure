#!/usr/bin/env python

"""Problem 2: Even Fibonacci numbers"""


def main():
    limit = 4_000_000
    a, b, c, Σ = 1, 1, 2, 0

    # every third Fibonacci number is even
    while c <= limit:
        Σ += c
        a = b + c
        b = c + a
        c = a + b

    return Σ

if __name__ == "__main__":
    print(main())

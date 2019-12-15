#!/usr/bin/env python

"""Problem 25: 1000-digit Fibonacci number"""

def main():
    a, b, cnt = 1, 2, 3

    while b < 10**999:
        a, b, cnt = b, a+b, cnt+1

    return cnt

if __name__ == "__main__":
    print(main())

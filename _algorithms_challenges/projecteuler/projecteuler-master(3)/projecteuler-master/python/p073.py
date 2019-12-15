#!/usr/bin/env python

"""Problem 73: Counting fractions in a range"""


def main():
    limit = 12000
    count = 0
    top = 0
    stack = [0]*(limit//2+1)
    left = 3
    right = 2

    while True:
        med = left + right
        if med > limit:
            if top > 0:
                left = right
                top -= 1
                right = stack[top]
            else:
                break
        else:
            count += 1
            stack[top] = right
            top += 1
            right = med

    return count


if __name__ == "__main__":
    print(main())

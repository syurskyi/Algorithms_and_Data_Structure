#!/usr/bin/env python

"""Problem 63: Powerful digit counts"""

def main():
    cnt = 0

    # if num >= 10, num^n has more than n digits for each n
    for num in range(1, 10):
        power = 1

        # if num^n has less than n digits, then num^k has less than k digits for each k > n
        while len(str(num**power)) == power:
            cnt += 1
            power += 1

    return cnt


if __name__ == "__main__":
    print(main())

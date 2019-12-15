#!/usr/bin/env python

"""Problem 43: Sub-string divisibility"""


def main():
    def sum_pandigitals(digits, num):
        if (len(digits) == 7 and num % 17 or
            len(digits) == 6 and (num//10) % 13 or
            len(digits) == 5 and (num//100) % 11 or
            len(digits) == 4 and (num//1000) % 7 or
            len(digits) == 3 and (num//10000) % 5 or
            len(digits) == 2 and (num//100000) % 3 or
            len(digits) == 1 and (num//1000000) % 2):
            return 0

        if len(digits) == 0:
            return num

        s = 0
        for i, d in enumerate(digits):
            t = digits[0:i]+digits[i+1:]
            s += sum_pandigitals(t, (10**(10-len(t)-1))*d+num)
        return s

    return sum_pandigitals((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 0)


if __name__ == "__main__":
    print(main())

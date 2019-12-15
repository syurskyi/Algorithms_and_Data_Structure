#!/usr/bin/env python

"""Problem 17: Number letter counts"""


def main():
    # precalculated letter counts for some numbers
    counts = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
              11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
              10: 3, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

    def count_letters(num):
        """Return the number of letters used by a number 0 < n < 1000"""
        count = 0

        if num >= 100:
            count += counts[num//100] + 7  # "hundred"
            num %= 100
            if num:
                count += 3  # "and"

        if num > 19:
            count += counts[num//10*10]
            num %= 10

        if num >= 1:
            count += counts[num]

        return count

    return sum([count_letters(i) for i in range(1, 1000)], len("onethousand"))

if __name__ == "__main__":
    print(main())

#!/usr/bin/env python

"""Problem 19: Counting Sundays"""


def is_leap_year(year):
    """Determine whether a year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    numdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    year, month, wday = 1901, 0, 2  # Tue, 1 Jan 1901
    is_leap = False
    sundays = 0

    while year < 2001:
        if wday == 0:
            sundays += 1

        days = 29 if is_leap and month == 1 else numdays[month]
        wday = (wday + days) % 7

        if month < 11:
            month += 1
        else:
            month = 0
            year += 1
            is_leap = is_leap_year(year)

    return sundays

if __name__ == "__main__":
    print(main())

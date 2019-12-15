"""Complete weekday_of_birth_date which takes a date object of a birthday and returns the corresponding weekday string.

For example Bob and Julian's birthdays return Saturday and Monday (that's why Bob is meant to relax and Julian to do all the work chuckle).

For this Bite you want to look at the datetime and calendar modules. Have fun!
"""

import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    # calendar is nice, but you can also use: date.strftime('%A')
    weekday = date.weekday()
    return calendar.day_name[weekday]
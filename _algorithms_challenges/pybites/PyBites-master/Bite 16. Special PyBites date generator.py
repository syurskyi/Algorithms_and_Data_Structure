"""Write a generator that returns special dates for PyBites:

Every year mark counting from PYBITES_BORN date
Every 100 days mark counting from PYBITES_BORN
See the tests for more details how your code will be tested: as this is a beginner's challenge we only calculate a few years ahead, leaving the next leap year (2020) out of this challenge.

We will revisit this in an intermediate challenge. Have fun!"""

from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)
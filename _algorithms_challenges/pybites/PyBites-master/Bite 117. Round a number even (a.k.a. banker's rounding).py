"""Bankers Rounding is an algorithm for rounding quantities to integers, in which numbers which are equidistant from the two nearest integers are rounded to the nearest even integer. Thus, 0.5 rounds down to 0; 1.5 rounds up to 2. - source
Complete the function below that takes an int, returning it rounded even. You probably want to look at the decimal module."""

from decimal import Decimal


def round_even(number):
    """Takes a number and returns it rounded even"""
    # decimal.getcontext() -> ROUND_HALF_EVEN is default
    return Decimal(number).quantize(0)
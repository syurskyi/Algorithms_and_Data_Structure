"""
go back  metrics icon  Level: Intro (img: IN / score: 1) level Bite 110. Type conversion and exception handling
In this Bite you complete the divide_numbers function that takes a numerator and a denominator (the number above and below the line respectively when doing a division).

First you try to convert them to ints, if that raises a ValueError you will re-raise it (using raise).

To keep things simple we can expect this function to be called with int/float/str types only (read the tests why ...)

Getting passed that exception (no early bail out, we're still in business) you try to divide numerator by denominator returning its result.

If denominator is 0 though, Python throws another exception. Figure out which one that is and catch it. In that case return 0. """


def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        numerator = int(numerator)
        denominator = int(denominator)
    except ValueError:
        raise
    try:
        func = numerator / denominator
        return func
    except ZeroDivisionError:
        return 0

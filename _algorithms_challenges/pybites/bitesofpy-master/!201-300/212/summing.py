from contextlib import suppress


def sum_numbers(numbers):
    """This generator divides each nummber by its consecutive number.
       So if it gets passed in [4, 2, 1] it yields 4/2 and 2/1.
       It ignores ZeroDivisionError and TypeError exceptions (latter happens
       when a string or other non-numeric data type is in numbers)

       Task: use contextlib's suppress twice to make the code below more concise.
    """
    for i, j in zip(numbers, numbers[1:]):
        # replace the block below
        with suppress(TypeError):
            with suppress(ZeroDivisionError):
                yield i/j

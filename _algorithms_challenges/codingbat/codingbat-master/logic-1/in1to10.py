''' Given a number n, return True if n is in the range 1..10, inclusive.
Unless outside_mode is True, in which case return True if the number is less
or equal to 1, or greater or equal to 10. '''


def in1to10(n, outside_mode):
    match = False
    if n in range(1, 11) and not outside_mode:
        match = True
    elif n not in range(2, 10) and outside_mode:
        match = True
    return match

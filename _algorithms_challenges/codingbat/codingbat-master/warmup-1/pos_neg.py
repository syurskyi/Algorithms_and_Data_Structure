''' Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both are
negative. '''


def pos_neg(a, b, negative):
    match = False
    if negative:
        if a < 0 and b < 0:
            match = True
    else:
        if a < 0 < b:
            match = True
        elif b < 0 < a:
            match = True
    return match

''' Given 3 int values, a b c, return their sum. However, if one of the values
is the same as another of the values, it does not count towards the sum. '''


def lone_sum(a, b, c):
    ints_sum = 0
    if a not in [b, c]:
        ints_sum += a
    if b not in [a, c]:
        ints_sum += b
    if c not in [a, b]:
        ints_sum += c
    return ints_sum

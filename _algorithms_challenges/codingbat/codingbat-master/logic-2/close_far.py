''' Given three ints, a b c, return True if one of b or c is "close"
(differing from a by at most 1), while the other is "far", differing from both
other values by 2 or more. Note: abs(num) computes the absolute value of a
number. '''


def close_far(a, b, c):
    close_far_match = False
    if abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2:
        close_far_match = True
    if abs(a - c) <= 1 and abs(a - b) >= 2 and abs(c - b) >= 2:
        close_far_match = True
    return close_far_match

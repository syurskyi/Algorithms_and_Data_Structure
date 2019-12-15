''' Given a non-negative number "num", return True if num is within 2 of a
multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5)
is 2. See also: Introduction to Mod. '''


def near_ten(num):
    is_near = False
    if num % 10 in [0, 1, 2, 8, 9]:
        is_near = True
    return is_near

''' The number 6 is a truly great number. Given two int values, a and b, return
True if either one is 6. Or if their sum or difference is 6. Note: the function
abs(num) computes the absolute value of a number. '''


def love6(a, b):
    is_6 = False
    if 6 in [a, b, a + b, abs(a - b)]:
        is_6 = True
    return is_6

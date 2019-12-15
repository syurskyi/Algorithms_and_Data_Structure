''' Given an int n, return True if it is within 10 of 100 or 200. Note:
abs(num) computes the absolute value of a number. '''


def near_hundred(n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return True
    return False

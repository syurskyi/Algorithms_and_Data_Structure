def limit_number(num, range_low, range_high):
    if num < range_low:
        return range_low
    elif num > range_high:
        return range_high
    else:
        return num

def test():
    print("test has started")
    if limit_number(5, 1, 10) != 5:
        print("error1")
    if limit_number(-3, 1, 10) != 1:
        print("error2")
    if limit_number(14, 1, 10) != 10:
        print("error3")

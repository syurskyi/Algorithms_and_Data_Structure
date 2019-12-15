def find_digit_amount(num):
    return len(str(num))

#BUGFIX
def test():
    print("test has started")
    if find_digit_amount(22224) != 5:
        print("error1")
    if find_digit_amount(2441139) != 7:
        print("error2")

def is_plural(word):
    if word[-1] == "s":
        return True
    else:
        return False


def test():
    print("test has started")
    if is_plural("dudes") != True:
        print("error1")
    if is_plural("doubles") != True:
        print("error2")
    if is_plural("mood") != False:
        print("error3")

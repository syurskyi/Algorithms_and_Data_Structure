def equal_slices(total, people, each):
    if people == 0:
        return True
    if people * each <= total:
        return True
    else:
        return False


def test():
    print("test has started")
    if equal_slices(100, 0, 50) != False:
        print("error1")
    if equal_slices(100 , 50, 2) != True:
        print("error2")
    if equal_slices(30, 15 ,3) != False:
        print("error3")

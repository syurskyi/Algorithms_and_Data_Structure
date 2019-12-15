def hurdle_jump(hurdles, jump_height):
    if hurdles == []:
        return True
    hurdles.sort()
    if hurdles[-1] <= jump_height:
        return True
    else:
        return False


def test():
    print("test has started")
    if hurdle_jump([1,2,1], 1) != False:
        print("error1")
    if hurdle_jump([1, 2, 3, 4, 5], 5) != True:
        print("error2")
    if hurdle_jump([], 4) != True:
        print("error3")

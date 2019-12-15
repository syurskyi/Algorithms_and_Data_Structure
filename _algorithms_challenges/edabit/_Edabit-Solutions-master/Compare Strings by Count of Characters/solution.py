def comp(txt1, txt2):
    if len(txt1) == len(txt2):
        return True
    else:
        return False


def test_comp():
    print("test has started")
    if comp("test","food") != True:
        print("error")
    if comp ("too", "good") != False:
        print("error2")
    else:
        print("success")

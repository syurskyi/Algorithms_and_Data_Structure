def is_empty(s):
    if s == "":
        return True
    else:
        return False

def test_empty():
    print("test has started")
    if is_empty("") != True:
        print("error1")
    if is_empty(10) != False:
        print("error2")
    if is_empty("tom") != False:
        print("error3")

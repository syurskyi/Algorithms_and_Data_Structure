def has_spaces(txt):
    if txt.find(" ") == -1:
        return False
    else:
        return True


def test():
    print("test has started")
    if has_spaces("FOO") != False:
        print("error1")
    if has_spaces("FOO BAR") != True:
        print('error2')
    if has_spaces("Foo ") != True:
        print("error3")
    if has_spaces("") != False:
        print("error4")

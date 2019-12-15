def get_word(left, right):
    return left.capitalize() + right



def test():
    print("test has started")
    if get_word("reli", "able") != "Reliable":
        print("error1")
    if get_word("maga", "zine") != "Magazine":
        print("error2")
    if get_word("offi", "cial") != "Official":
        print("error3")

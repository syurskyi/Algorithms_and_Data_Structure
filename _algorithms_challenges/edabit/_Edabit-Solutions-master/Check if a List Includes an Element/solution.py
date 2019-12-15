def check(lst, el):
    if lst.count(el) > 0:
        return True
    else:
        return False


def test():
    print("test has started")
    a_list = [4.6,4,7]
    if check(a_list,4) != True:
        print("error")
    if check(a_list,2) != False:
        print("erro2")


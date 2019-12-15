def find_index(lst, txt):
    return lst.index(txt)



def test():
    print("test has started")
    a_list = ["Google", "facebook", "Sony"]
    if find_index(a_list, "Sony") != 2:
        print("error1")

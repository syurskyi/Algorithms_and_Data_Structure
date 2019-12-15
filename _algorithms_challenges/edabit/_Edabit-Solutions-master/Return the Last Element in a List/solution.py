def getLastItem(lst):
    return lst[-1]



def test():
    print("test has started")
    a_list = [2,4,6]
    if getLastItem(a_list) != 6:
        print("error1")
    a_list = ["cat", "dog", "cow"]
    if getLastItem(a_list) != "cow":
        print("error2")

def first_last(lst):
    return [lst[0], lst[-1]]



def test():
    print("test has started")
    a_list = [2,1,3,4]
    if first_last(a_list) != [2,4]:
        print("error1")
    b_list = ["tom","rat", "jerry"]
    if first_last(b_list) != ["tom","jerry"]:
        print("error2")

def is_empty(dictionary):
    if len(dictionary) == 0:
        return True
    else:
        return False


def test():
    print("Test has started")
    dict = {"Name": "Eleven"}
    if is_empty(dict) != False:
        print("error1")
    b_dict = {}
    if is_empty(b_dict) != True:
        print("error2")

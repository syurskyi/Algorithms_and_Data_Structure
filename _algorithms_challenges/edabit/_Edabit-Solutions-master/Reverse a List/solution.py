def reverse(lst):
    return lst[::-1]


def test():
    print("test has started")
    if reverse([1, 2, 3, 4]) != [4, 3, 2, 1]:
        print("error1")
    if reverse([5, 6, 7]) != [7, 6, 5]:
        print("error2")


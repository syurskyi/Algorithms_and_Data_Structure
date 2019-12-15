def programmers(one, two, three):
    a_list = [one, two, three]
    a_list.sort()
    return a_list[-1] - a_list[0]


def test_programmers():
    print("test has started")
    if programmers(5, 10, 3) != 7:
        print("error1")
    if programmers(20, 5, 15) != 15:
        print("error2")

num_list _ [1, 2, 3, 4, 5, 6, 7]
num_list2 _ [5, 6, 7, 8, 9]


___ rondomFunction(num_list
    total _ 0

    ___ num1 __ num_list2:
        ___ num2 __ num_list:
            print(num1, num2)
            total +_ 1

    r_ total


print(rondomFunction(num_list))
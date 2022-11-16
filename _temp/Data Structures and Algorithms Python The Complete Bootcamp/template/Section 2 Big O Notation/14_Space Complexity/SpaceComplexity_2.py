___ all_cubes(items
    result _    # list

    ___ item __ items:
        result.a..(pow(item,3)) #O(n)

    print(result)

items _ [2,3,4,5,6,7]
all_cubes(items)
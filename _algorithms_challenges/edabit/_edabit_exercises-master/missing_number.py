def missing_nums(lst):
    example_list = [i for i in range(1, 11)]
    print(example_list)
    result = list(set(example_list) - set(lst))
    return result[0]



print(missing_nums([1, 7, 2, 4, 8, 10, 5, 6, 9]))
print(missing_nums([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(missing_nums([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missing_nums([7, 2, 3, 9, 4, 5, 6, 8, 10]))

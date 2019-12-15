def sum_of_evens(lst):
    output = 0
    for i in lst:
        for x in i:
            if x % 2 == 0:
                output += x
    return output

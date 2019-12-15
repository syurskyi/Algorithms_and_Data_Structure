def find_even_nums(num):
    if num < 2:
        return []
    index = 2
    output = []
    while index <= num:
        if index % 2 == 0:
            output.append(index)
        index = index + 1

    return output

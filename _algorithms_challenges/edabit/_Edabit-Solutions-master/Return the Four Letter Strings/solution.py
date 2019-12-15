def is_four_letters(lst):
    index = 0
    output_list =[]
    while index < len(lst):
        if len(lst[index]) == 4:
            output_list.append(lst[index])
        index = index + 1
    return output_list

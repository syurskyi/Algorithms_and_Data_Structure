def dictionary(intial,lst):
    last_index = len(lst) - 1
    index = 0
    a_list = []
    while index <= last_index:
        word = lst[index]
        if word.startswith(intial):
            a_list.append(word)
        index = index + 1
    return a_list

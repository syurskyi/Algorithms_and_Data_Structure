def first_non_repeated_character(txt):
    list_txt = list(txt)
    nonrepeated_list = []
    for char in list_txt:
        if list_txt.count(char) == 1:
            nonrepeated_list.append(char)
    if not nonrepeated_list:
        return False
    else:
        return nonrepeated_list[0]


print((first_non_repeated_character("the quick brown fox jumps then quickly blows air")))
print((first_non_repeated_character("the misty examination pleases into the drab county")))

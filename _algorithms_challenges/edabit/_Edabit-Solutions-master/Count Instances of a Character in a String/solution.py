def char_count(txt1, txt2):
    index = 0
    total_count = 0
    while index <= len(txt2) -1:
        if txt1 == txt2[index]:
            total_count = total_count + 1
        index = index + 1
    return total_count

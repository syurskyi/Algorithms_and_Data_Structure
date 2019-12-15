def accum(s):
    final_string = ''
    counter = 0
    for char in list(s):
        cur_str = char * (counter + 1)
        final_string += str(cur_str).capitalize() + '-'
        counter += 1
    return final_string[:-1]


print(accum('ZpglnRxqenU'))

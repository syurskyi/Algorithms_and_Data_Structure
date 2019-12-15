def filter_list(l):
    index = 0
    output = []
    while index < len(l):
        if(type(l[index])) == int:
           output.append(l[index])
        index = index + 1
    return output

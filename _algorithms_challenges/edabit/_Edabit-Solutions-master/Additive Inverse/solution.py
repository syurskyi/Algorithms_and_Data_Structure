def additive_inverse(lst):
    index = 0
    output = []
    while index < len(lst):
        s= lst[index] * -1
        output.append(s)
        index += 1
    return output

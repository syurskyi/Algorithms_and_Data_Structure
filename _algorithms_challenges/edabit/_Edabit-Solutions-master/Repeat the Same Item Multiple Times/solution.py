def repeat(item, times):
    if times == 0:
        return []
    index = 1
    output = []
    while index <= times:
        output.append(item)
        index += 1
    return output

def countdown(start):
    index = 1
    output = [start]
    while index <= start:
        s = start - index
        output.append(s)
        index += 1
    return output

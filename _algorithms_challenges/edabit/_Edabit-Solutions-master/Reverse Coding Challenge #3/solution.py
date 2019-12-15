def mystery_func(lst, n):
    output = []
    for i in lst:
        s = i % n
        output.append(s)
    return output

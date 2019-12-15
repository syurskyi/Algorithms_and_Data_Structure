def even_odd_transform(lst, n):
    output = []
    s = 0
    for i in lst:
        if i % 2 == 0:
            s = i - 2* n
            output.append(s)
        else:
            s = i + 2* n
            output.append(s)

    return output

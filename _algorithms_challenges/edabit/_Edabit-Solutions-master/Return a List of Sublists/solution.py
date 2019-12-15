def matrix(x, y, z):
    lst = []
    for i in range(x):
        lst.append([])
    for q in lst:
        for a in range(y):
            q.append(z)
    return lst



def intersection_union(lst1, lst2):
    inter = []
    uni = []
    output = [inter, uni]
    for i in lst1:
        if i in lst2:
            inter.append(i)
    for x in inter:
        if inter.count(x) > 1:
            inter.remove(x)
    for z in lst1:
        if z in uni:
            continue
        uni.append(z)
    for c in lst2:
        if c not in uni:
             uni.append(c)
    inter.sort()
    uni.sort()
    return output

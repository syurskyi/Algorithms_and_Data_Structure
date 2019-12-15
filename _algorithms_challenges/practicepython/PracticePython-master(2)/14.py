# List Remove Duplicates - ???

# Remove Dupes -- using for loop (works)


def removedupes1(li):
    new_li = []
    for i in li:
        if i not in new_li:
            new_li.append(i)
    return (new_li)

# Remove Dupes -- using set (works)


def removedupes2(li):
    return list(set(li))


# Given
li = [1, 5, 3, 6, 7, 1, 2, 6, 7, 2]
print removedupes1(li)
print removedupes2(li)

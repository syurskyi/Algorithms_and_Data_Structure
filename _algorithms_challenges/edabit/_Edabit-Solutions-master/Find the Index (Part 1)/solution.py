def search(lst, item):
    if lst.count(item) == 0:
        return -1
    else:
        return lst.index(item)

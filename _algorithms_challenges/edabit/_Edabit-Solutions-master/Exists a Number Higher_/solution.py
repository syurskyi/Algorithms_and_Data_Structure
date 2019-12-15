def exists_higher(lst, n):
    for i in lst:
        if i >= n:
            return True
    else:
        return False

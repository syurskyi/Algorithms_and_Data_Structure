def subset(lst1, lst2):
    Aset = set(lst1)
    Bset = set(lst2)
    if Aset.issubset(Bset):
        return True
    else:
        return False

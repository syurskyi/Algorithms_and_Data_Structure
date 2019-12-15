def is_omnipresent(lst, val):
    for i in lst:
        if val in i:
            return True
        else:
            return False

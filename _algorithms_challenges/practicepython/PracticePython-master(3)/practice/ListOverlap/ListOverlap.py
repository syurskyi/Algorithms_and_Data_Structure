
def ListOverlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    kesisti=kesisim(a,b)
    print(kesisti)
    return kesisti

def kesisim(a,b):
    sa= set(a)
    sb= set(b)
    inter=sa.intersection(sb)
    return list(inter)
    
    
    
    

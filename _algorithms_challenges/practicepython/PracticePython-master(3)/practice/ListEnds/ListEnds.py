
def ListEnds():
    a= [1,2,3,4,5]
    carp= lambda l : l*5
    a=list(map(carp,a))# input-girdi
    sonuc=[a[0], a[len(a)-1]]
    print(sonuc)
    return sonuc

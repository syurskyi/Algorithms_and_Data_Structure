import random
def LessThanTen():
    girdi= [random.randint(0,101) for _ in range(20)] 
    OndanAz= [az for az in girdi if az<10]
    print(OndanAz)
    return OndanAz 
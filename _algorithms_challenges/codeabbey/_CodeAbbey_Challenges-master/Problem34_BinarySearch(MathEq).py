import math
infile = open("prob34.txt")
infile.readline()
data = infile.readlines()
infile.close()


def func(x):
    global A,B,C,D
    eq = (A*x) + (B*math.sqrt(x**3)) - (C*math.exp(-x/50)) - D
    return eq

for line in data:
    A,B,C,D = list(map(float,line.strip().split(" ")))
    top = 100
    bot = 0
    eq = -1
    while math.isclose(eq , 0 ,abs_tol = 1e-7) == False:
        mid = (top+bot)/2
        eq = func(mid)
        if eq > 0:
            top = mid-1
        elif eq < 0:
            bot = mid+1
    print(mid,end=" ")
    
    
    
    

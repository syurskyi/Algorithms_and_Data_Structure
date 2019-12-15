infile = open("prob104.txt")
infile.readline()
data=infile.readlines()
infile.close()

for line in data:
    line = line.strip().split(" ")
    x1,y1,x2,y2,x3,y3 = list(map(int,line))

    #FACTOR PRODUCT
    A = 0.5*abs((x1*y2)+(x2*y3)+(x3*y1)-(y1*x2)-(y2*x3)-(y3*x1))
    print(A,end=" ")

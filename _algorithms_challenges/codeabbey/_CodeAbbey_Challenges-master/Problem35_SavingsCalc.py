infile = open("prob35.txt")
infile.readline()
data = infile.readlines()

for line in data:
    s,p,r = line.strip().split(" ")
    s = float(s)
    count= 0
    while int(s)<int(p):
        count+= 1
        s*=(1+(int(r)/100))
##        print(count,"{:0.2f}".format(s))
    print(count ,end=" ")


infile.close()

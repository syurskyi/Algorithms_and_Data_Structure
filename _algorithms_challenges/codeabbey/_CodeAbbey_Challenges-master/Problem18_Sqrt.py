infile = open("prob18.txt")
infile.readline()
data = infile.readlines()


for line in data:
    r = 1
    x,n = line.strip().split(" ")
    d = int(x)/r
##    while abs(r-d) > 1:
##        r = (r+d)/2
##        d = int(x)/r
##    r = (r+d)/2
    for i in range(int(n)):
        r = (r+d)/2
        d = int(x)/r
    print(r,end=" ")
        








infile.close()

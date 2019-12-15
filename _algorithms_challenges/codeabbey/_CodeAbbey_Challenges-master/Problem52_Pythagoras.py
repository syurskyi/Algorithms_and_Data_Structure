infile = open("prob52.txt")
infile.readline()
data = infile.readlines()
for line in data:
    a,b,c = line.strip().split(" ")
    sums = int(a)**2 + int(b)**2
    if sums == int(c)**2:
        print("R",end=" ")
    elif sums < int(c)**2:
        print("O",end=" ")
    elif sums > int(c)**2:
        print("A",end=" ")

infile.close()

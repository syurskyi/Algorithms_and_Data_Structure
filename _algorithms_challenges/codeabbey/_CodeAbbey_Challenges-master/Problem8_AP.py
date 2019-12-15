infile = open("prob8.txt")
infile.readline()
data = infile.readlines()
for line in data:
    line = line.strip()
    a,b,n = line.split(" ")
    total = 0
    for i in range(int(n)):
        total += int(a)+i*int(b)
    print(total,end=" ")
   


infile.close()

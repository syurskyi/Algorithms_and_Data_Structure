infile = open("prob94.txt")
infile.readline()
data = infile.readlines()
infile.close()

for line in data:
    total = 0
    line = line.strip().split(" ")
    for each in line:
        total += int(each)**2
    print(total,end=" ")

infile = open("prob44.txt")
infile.readline()
data = infile.readlines()

for line in data:
    line = line.strip().split(" ")
    summ = 0
    for random in line:
        summ += (int(random)%6)+1
    print(summ,end=" ")

infile.close()

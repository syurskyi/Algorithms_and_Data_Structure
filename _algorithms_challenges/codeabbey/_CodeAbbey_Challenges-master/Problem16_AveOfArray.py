
infile = open("prob16.txt")
infile.readline()
data = infile.readlines()


def avg(num):
    total = sum(num)
    ave = total/len(num)
    print(round(ave),end=" ")
    


for line in data:
    line = line.strip().split(" ")
    line = line[:-1]
    line = [int(i) for i in line]
    avg(line)
infile.close()

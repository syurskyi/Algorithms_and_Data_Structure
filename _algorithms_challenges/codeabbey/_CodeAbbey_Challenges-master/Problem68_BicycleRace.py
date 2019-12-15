infile = open("prob68.txt")
infile.readline()
data = infile.readlines()
for line in data:
    dist,s1,s2 = line.strip().split(" ")
    time = int(dist)/(int(s1)+int(s2))
    print(float(time)*int(s1),end=" ")



infile.close()

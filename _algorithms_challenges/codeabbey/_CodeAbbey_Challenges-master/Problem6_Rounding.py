infile = open("prob6.txt")
infile.readline()
data = infile.readlines()
for line in data:
    num,denom = line.strip("\n").split(" ")
    ans = int(num)/int(denom)
    print(round(ans),end=" ")



infile.close()

infile = open("prob29.txt")
infile.readline()
data = infile.read().strip().split(" ")
data = [(int(data[i]),i+1) for i in range(len(data))]
for j in range(len(data)):
    for k in range(len(data)):
        if data[j][0]<data[k][0]:
            data[j],data[k] = data[k],data[j]

for i in data:
    print(i[1],end=" ")
infile.close()

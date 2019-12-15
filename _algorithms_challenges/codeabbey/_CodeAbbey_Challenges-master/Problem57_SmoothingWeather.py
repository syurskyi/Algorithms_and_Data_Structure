infile = open("prob57.txt")
n = infile.readline()
data = infile.read().strip().split(" ")
print(data[0],end=" ")
for i in range(int(n)):
    temp = data
    if i == 0 or i ==int(n)-1:
        pass
    else:
        ave = eval("+".join(temp[i-1:i+2]))/3
        print(ave,end=" ")
print(data[int(n)-1])
infile.close()

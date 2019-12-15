infile = open("prob23.txt")
data = infile.read().strip().split(" ")
infile.close()
data = data[:-1]
data = [int(i) for i in data]
i = 0
swaps = 0
while i <len(data)-1:
    if data[i]>data[i+1]:
        swaps+=1
        data[i],data[i+1]=data[i+1],data[i]
    i+=1


## CHECKSUM PROB17
total = 0
for digit in data:
    total += int(digit)
    total *= 113
    total = total%10000007

print(swaps,total)



infile = open("prob27.txt")
infile.readline()
data = infile.read().strip().split(" ")
data = [int(i) for i in data]

passes = 0
swaps = 0
i=len(data)
flag = True
while i>2 and flag:
    passes+=1
    j=0
    flag =False
    while j<i-1:
        if data[j]>data[j+1]:
            swaps +=1
            flag = True
            data[j],data[j+1]= data[j+1],data[j]
        j+=1
    i-=1
    
print(data)
print(passes,swaps,end=" ")

infile.close()

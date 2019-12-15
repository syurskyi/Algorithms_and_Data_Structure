infile = open("prob120.txt")
n = infile.readline()
array = infile.readline()
infile.close()

array = array.split(" ")
array = list(map(int,array))
for i in range(int(n)-1):
    highest = 0
    index = 0
    for j in range(len(array)-i):
        if array[j]>highest:
            highest = array[j]
            index=j
    array[index],array[int(n)-i-1]=array[int(n)-i-1],array[index]
    print(index,end=" ")
           

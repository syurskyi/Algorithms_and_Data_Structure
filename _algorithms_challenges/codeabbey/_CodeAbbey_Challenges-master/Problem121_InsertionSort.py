infile = open("prob121.txt")
infile.readline()
data = infile.read()
infile.close()

array = [int(i) for i in data.strip().split(" ")]
i = 0
while i < len(array)-1:
    count = 0
    if array[i]>array[i+1]:
        temp = array[i+1]
        j = i
        while j>=0 and array[j]>temp:
            count+=1
            array[j+1] = array[j]
            j-=1
        array[j+1] = temp
    print(count,end=" ")
    i+=1


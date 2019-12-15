infile = open("prob55.txt")
data =infile.read()
infile.close()

data = data.strip().split(" ")

i=0
latins = dict()
while data[i] != "end":
    latins[data[i]]= latins.get(data[i],0)+1
    i+=1

code = list(latins.items())

# INSERTION SORT
i = 0
while i<len(code)-1:
    if code[i]>code[i+1]:
        temp= code[i+1]
        j=i
        while j>0 and code[j]>temp:
            code[j],code[j+1]=code[j+1],code[j]
            j-=1
        code[j+1] = temp
    i+=1

for i in code:
    if i[1]>=2:
        print(i[0],end=" ")
        


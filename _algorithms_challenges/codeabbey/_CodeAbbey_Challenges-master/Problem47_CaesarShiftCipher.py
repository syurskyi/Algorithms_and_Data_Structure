infile = open("prob47.txt")
n,k=infile.readline().strip().split(" ")
data = infile.readlines()
infile.close()

## Gen Alphabets
alpha = []
for i in range(26):
    char = chr(65+i)
    alpha.append(char)


#Decrypt
    
for line in data:
    output = ""
    line = line.strip()
    for char in line:
        if char.isalpha():
            i = alpha.index(char)-int(k)
            output += alpha[i]
        else:
            output+=char
    print(output,end=" ")

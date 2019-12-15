infile = open("prob81.txt")
infile.readline()
data=infile.readline()
data = data.strip().split(" ")
max_32 = 4294967296 

for i in range(len(data)): # flipping negative to positive
    if int(data[i]) <0:
        data[i] = str(max_32 + int(data[i]))

##for numbers in data:
##    conv_bin = bin(int(numbers))
##    conv_bin = conv_bin[2:]
##    summ = sum([int(i) for i in conv_bin])
##    print(summ,end=" ")

# ALT OF COUNTING BITS USING BITWISE
for numbers in data:
    c=0
    numbers = int(numbers)
    for i in range(32):
       c+=(int(numbers) & 1) # check last bit with 1
       numbers>>=1  # truncate last bit
    print(c)



infile.close()

infile = open("prob69.txt")
infile.readline()
data = infile.readline()
infile.close()

#### GEN FIBONACCI
##fib = [0,1]
##n= 10000
##for i in range(n):
##    fib.append(fib[i]+fib[i+1])
##
##for index in data.strip().split(" "):
##    i = 1
##    while fib[i]%int(index) != 0:
##        i+=1
##    print(i,end=" ")


## ALTERNATIVE
for m in data.strip().split(" "):
    a,b = 0,1
    i=1
    while b%int(m) != 0:
        a,b=b,(a+b)
        i+=1
    print(i,end=" ")

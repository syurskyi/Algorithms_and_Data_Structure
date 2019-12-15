

fib = [0,1]
for i in range(1000):       # FIB GEN
    fib.append(fib[i]+fib[i+1])
infile = open("prob67.txt")
infile.readline()
data = infile.readlines()
for fib_no in data:
    print(fib.index(int(fib_no)),end=" ")



infile.close()

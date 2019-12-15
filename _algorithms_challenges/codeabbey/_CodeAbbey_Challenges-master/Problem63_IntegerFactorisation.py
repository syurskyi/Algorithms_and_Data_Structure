infile = open("prob63.txt")
infile.readline()
data = infile.readlines()
infile.close()

#check for prime
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
        return True

for num in data:
    num = int(num.strip())
    output = []
    if isPrime(num):
        output.append(num)
    else:
        i=2
        while num != 1:
            while isPrime(i) and num%i == 0:
               output.append(i)
               num = num//i
            i+=1
    print("*".join([str(x) for x in output]),end=" ")
        

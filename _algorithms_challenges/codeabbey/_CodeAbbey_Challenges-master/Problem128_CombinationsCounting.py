import math
infile = open("prob128.txt")
infile.readline()
data =infile.readlines()
infile.close()

for line in data:
    N,K = line.strip().split(" ")
    numerator = math.factorial(int(N))
    denominator = (math.factorial(int(K))*math.factorial(int(N)-int(K)))
    total = numerator/denominator
    print(int(total),end = " ")
    

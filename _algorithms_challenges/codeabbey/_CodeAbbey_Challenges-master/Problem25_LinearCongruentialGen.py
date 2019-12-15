infile = open("prob25.txt")
infile.readline()
data = infile.readlines()
infile.close()

for line in data:
    a,c,m,x,n = line.strip().split(" ")
    random = []
    for i in range(int(n)):
        x = (int(a)*int(x)+int(c))%int(m)
        random.append(x)
    print(random[-1],end=" ")

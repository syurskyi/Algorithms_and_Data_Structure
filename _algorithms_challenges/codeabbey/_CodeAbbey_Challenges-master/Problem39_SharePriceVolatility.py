infile = open("prob39.txt")
infile.readline()
data = infile.readlines()
infile.close()


for line in data:
    line = line.strip().split(" ")
    name = line[0]
    share_p = [int(i) for i in line[1:]]
    mean = sum(share_p)/len(share_p)
    var = [(price-mean)**2 for price in share_p]
    dev = (sum(var)/len(var))**0.5
    if dev >= 4*0.01*mean:
        print(name,end=" ")
        
    

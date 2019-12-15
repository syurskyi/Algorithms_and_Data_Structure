infile = open("prob26.txt")
infile.readline()
data = infile.readlines()

for line in data:
    a,b = line.strip().split(" ")
    lcm = int(a)*int(b)
    while not(int(a)== 0 or int(b)==0) :
        a = int(a)%int(b)
        if int(a)== 0 or int(b)==0:
            break
        b = int(b)%int(a)
        
    if int(a) == 0:
        lcm = lcm/int(b)
        print("({} {})".format(int(b),int(lcm)),end=" ")
    elif int(b) == 0:
        lcm = lcm/int(a)
        print("({} {})".format(int(a),int(lcm)),end=" ")

    



















infile.close()

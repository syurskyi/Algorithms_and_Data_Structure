import cmath

infile = open("prob38.txt")
infile.readline()
data = infile.readlines()
infile.close()

for eq in data:
    output = ""
    A,B,C = [int(i) for i in eq.strip().split(" ")]
    x1 = (-B + cmath.sqrt(B**2 - (4*A*C))) / (2*A)
    x2 = (-B - cmath.sqrt(B**2 - (4*A*C))) / (2*A)
    if x1.imag == float(0.0):
        output+= str(int(x1.real))+" "

    if x2.imag == float(0.0):
        output+= str(int(x2.real))
    else:
        if x1.real == float(0.0):
            if str(x1)[0] == "-":
                output += "0"+str(x1).replace("j","i").replace("(","").replace(")","")+" "
            else:
                output += "0+"+str(x1).replace("j","i").replace("(","").replace(")","")+" "
        if x2.real == float(0.0):
            if str(x2)[0] == "-":
                output += "0"+str(x2).replace("j","i").replace("(","").replace(")","")
            else:
                output += "0+"+str(x2).replace("j","i").replace("(","").replace(")","")
        else:
            output += str(x1).replace("j","i").replace("(","").replace(")","")+" "
            output += str(x2).replace("j","i").replace("(","").replace(")","")
        
    print(output,end="; ")

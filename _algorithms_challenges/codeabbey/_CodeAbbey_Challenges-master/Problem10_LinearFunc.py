infile = open("prob10.txt")
infile.readline()
data = infile.readlines()
# using the model of y = ax+b
for line in data:
    x1,y1,x2,y2 = line.strip().split(" ")
    a = (int(y1)-int(y2))/(int(x1)-int(x2))
    b = int(y1)-(a*int(x1))

    print("({} {})".format(round(a),round(b)),end=" ")














infile.close()

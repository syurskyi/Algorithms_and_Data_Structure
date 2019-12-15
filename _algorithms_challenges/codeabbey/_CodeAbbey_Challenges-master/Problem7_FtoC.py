infile = open("prob7.txt")
data = infile.read()
data = data.split(" ")
for f in data[1:]:
    cel = (int(f)-32)/1.8
    print(round(cel),end=" ")



infile.close()

import re
infile = open("prob50.txt")
infile.readline()
data= infile.readlines()
punc = " ,.:;-"
for line in data:
    line = line.strip()
    line = re.sub("[- ,.:;?!]","",line) # replace multiple char with ""
    line = line.lower()  # make all lower
    if line == line[::-1]:  # compare with backward str
        print("Y",end=" ")
    else:
        print("N",end=" ")
    


infile.close()

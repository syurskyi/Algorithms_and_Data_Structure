


infile = open("prob75.txt","r")
infile.readline()
data = infile.readlines()
infile.close()
for line in data:
    line = line.strip().split()
    counter = [0 for i in range(7)]# ignore index 0
    for digit in line:
        counter[int(digit)] +=1
    if counter.count(5) == 1:
        print("yacht",end=" ")
    elif counter.count(4) != 0:
        print("four",end=" ")
    elif counter.count(3) == 1 and counter.count(2) ==1:
        print("full-house",end=" ")
    elif counter.count(3) == 1:
        print("three",end=" ")
    elif counter.count(2) == 1:
        print("pair",end=" ")
    elif counter.count(2) == 2:
        print("two-pairs",end=" ")
    elif counter.count(1) == 5:
        if counter[1] == 0:
            print("big-straight",end=" ")
        else:
            print("small-straight",end=" ")


infile = open("prob49.txt")
infile.readline()
data = infile.readlines()
infile.close()

# S>P
# P>R
# R>S


for line in data:
    p1 = 0
    p2 = 0
    match = line.strip().split(" ")
    for game in match:
        c1 = game[0] # p1 choice
        c2 = game[1]
        if c1 == "S":
            if c2 == "P":
                p1+=1
            elif c2 == "R":
                p2+=1
                
        elif c1 == "R":
            if c2 == "S":
                p1+=1
            elif c2 == "P":
                p2+=1
                
        elif c1 == "P":
            if c2 == "R":
                p1+=1
            elif c2 == "S":
                p2+=1

    if p1>p2:
        print("1",end=" ")
    else:
        print("2",end=" ")

















        

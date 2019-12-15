infile = open("prob19.txt")
infile.readline()
data = infile.readlines()
infile.close()


leftB = "([{<"
rightB = ")]}>"

for line in data:
    flag = True
    bracketlist=[]
    for char in line:
        if char in leftB:
            bracketlist.append(char)
        elif char in rightB:
            if len(bracketlist) == 0:
                flag = False
                break
            last_b = bracketlist.pop()
            if leftB.index(last_b) != rightB.index(char):
                flag = False
                break
       
    if len(bracketlist) != 0:
        print("0",end=" ")
    elif flag:
        print("1",end=" ")
    else:
        print("0",end=" ")

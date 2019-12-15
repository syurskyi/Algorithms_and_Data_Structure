infile = open("prob5.txt")
count = infile.readline()
ans = ""
for i in range(int(count)):
    a,b,c = infile.readline().split(" ")
    if int(a)>=int(b): #take b
        if int(b)>int(c): #take c
            ans += c +" "
        else: 
            ans += b+" "
    else: #take a
        if int(a)>int(c): # take c
            ans += c+" "
        else:
            ans += a+" "
print(ans)

infile = open("prob4.txt")
count = infile.readline()
ans = ""
for i in range(int(count)):
    a,b = infile.readline().split(" ")
    if int(a)>=int(b):
        ans += b+" "
    else:
        ans += a+" "
print(ans)

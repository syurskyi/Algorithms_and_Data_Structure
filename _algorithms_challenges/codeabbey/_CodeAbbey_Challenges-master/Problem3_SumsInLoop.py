infile = open("prob3.txt")
count = infile.readline()
ans = ""
for i in range(int(count)):
    number1,number2 = infile.readline().split(" ")
    ans += str(int(number1)+int(number2))+ " "
print(ans)




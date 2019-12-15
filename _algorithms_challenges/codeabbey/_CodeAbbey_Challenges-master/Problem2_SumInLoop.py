infile = open("prob2.txt","r")
number_of_sums = infile.readline()
data = infile.readline().split(" ")
total = 0
for i in range(int(number_of_sums)):
    total += int(data[i])
print(total)
    

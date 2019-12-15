infile = open("prob17.txt")
infile.readline()
data = infile.read().strip().split(" ")

total = 0
for digit in data:
    total += int(digit)
    total *= 113
    total = total%10000007
print(total)

infile.close()

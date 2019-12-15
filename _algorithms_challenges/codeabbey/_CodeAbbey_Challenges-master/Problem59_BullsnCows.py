infile = open("prob59.txt")
value,n = infile.readline().strip().split(" ")
guess = infile.read()
infile.close()

guess = guess.strip().split(" ")

for number in guess:
    c1 = 0 # condition 1
    c2 = 0 # condition 2
    for digit in number:
        if digit in value:
            if number.index(digit) == value.index(digit):
                c1 +=1
            else:
                c2 +=1
    print("{}-{}".format(c1,c2),end=" ")
    
    

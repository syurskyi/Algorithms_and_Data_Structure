infile = open("prob72.txt")
n,x = infile.readline().strip().split(" ")
data = infile.readline()
infile.close()
a = 445
c = 700001
m = 2097152
consonants = "bcdfghjklmnprstvwxz"
vowels = "aeiou"

for length in data.strip().split(" "):
    output = ""
    for i in range(int(length)):
        x = (int(a)*int(x)+int(c))%int(m)
        if i%2==0: # ODDS
            output+=consonants[x%19]
        else: # EVENS
            output+=vowels[x%5]
            
    print(output,end=" ")
    

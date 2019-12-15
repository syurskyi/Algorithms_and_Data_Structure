
infile = open("prob36.txt")
infile.readline()
data = infile.readlines()

poss = [[ 0 for i in range(10)] for i in range((len(data[0])-3))]

for line in data:
    guess,reply = line.strip().split()
    if reply == "0":
        for i in range(len(guess)):
            poss[i][int(guess[i])] = None
    elif reply == "1" or reply == "2":
        try:
            for j in range(len(guess)):
                poss[j][int(guess[j])] += 1
        except TypeError:
            continue

            

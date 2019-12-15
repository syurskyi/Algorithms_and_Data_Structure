infile = open("prob45.txt")
data  = infile.readlines()
infile.close()
output = ""
for line in data:
    output += str(line.strip())+" "

data = output.split(" ")[:-1]

cards = []
ranks = ["A", "2", '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']

for i in range(4):
    for j in range(13):
        cards.append(str(suits[i])+str(ranks[j]))


for i in range(len(data)):
    ran = int(data[i])%52
    # swap the two card
    cards[i],cards[ran] =cards[ran],cards[i]

print(" ".join(cards))

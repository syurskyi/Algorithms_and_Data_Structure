infile = open("prob58.txt")
infile.readline()
data = infile.read()
infile.close()

data = data.split(" ")
data = list(map(int,data))

suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

for card in data:
    suit_val = card//13
    rank_val = card%13
    print("{}-of-{}".format(ranks[rank_val],suits[suit_val]),end=" ")

    

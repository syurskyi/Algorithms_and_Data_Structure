infile = open("prob42.txt")
infile.readline()
data = infile.readlines()
infile.close()



for line in data:
    total = 0
    hand = line.strip().split(" ")
    for card in hand:
        if card.isdigit():
            total += int(card)
        elif card in "TJQK":
            total += int(10)
        elif card == "A":
            total += int(11)

    count = hand.count("A")
    while count > 0 and total>21:
        count-=1
        total -= 10

    if total<=21:
        print(total ,end=" ")
    else:
        print("Bust",end=" ")
            

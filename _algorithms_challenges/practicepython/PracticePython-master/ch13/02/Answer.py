import random
#搜尋關鍵字 撲克牌 python
#搜尋關鍵字 random choice not repeat

poker = ''  #string
pokers = set()  #set
#搜尋 python set add、 python set remove

for i in ['♥','♠','♦','♣']:
    for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
        poker = i + j
        pokers.add(poker)
        poker = ''

#搜尋關鍵字 random.choice set
for i in range(6):
    choice = random.choice(tuple(pokers))
    print(choice)
    pokers.remove(choice)
    #選中後，將該選項移出set，以免重複選取


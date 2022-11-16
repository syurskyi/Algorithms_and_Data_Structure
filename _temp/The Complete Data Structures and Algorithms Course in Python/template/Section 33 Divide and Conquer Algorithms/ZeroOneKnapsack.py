#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Zero One Knapsack in Python

c_ Item:
    ___ -  profit, weight
        profit _ profit
        weight _ weight

___ zoKnapsack(items, capacity, currentIndex
    __ capacity <_0 or currentIndex < 0 or currentIndex >_ l..(items
        r_ 0
    elif items[currentIndex].weight <_ capacity:
        profit1 _ items[currentIndex].profit + zoKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 _ zoKnapsack(items, capacity, currentIndex+1)
        r_ max(profit1, profit2)
    ____
        r_ 0

mango _ Item(31, 3)
apple _ Item(26, 1)
orange _ Item(17, 2)
banana _ Item(72, 5)

items _ [mango, apple, orange, banana]

print(zoKnapsack(items, 7, 0))
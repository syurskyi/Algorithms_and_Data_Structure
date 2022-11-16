#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Fractional Knapsack Problem  in Python

c_ Item:
    ___ -  weight, value
        weight _ weight
        value _ value
        ratio _ value / weight

___ knapsackMethod(items, capacity
    items.sort(key_lambda x: x.ratio, reverse _ True)
    usedCapacity _ 0
    totalValue _ 0
    ___ i __ items:
        __ usedCapacity + i.weight <_ capacity:
            usedCapacity +_ i.weight
            totalValue +_ i.value
        ____
            unusedWeight _ capacity - usedCapacity
            value _ i.ratio * unusedWeight
            usedCapacity +_ unusedWeight
            totalValue +_ value
        
        __ usedCapacity == capacity:
            break
    print("Total value obtained: "+str(totalValue))

item1 _ Item(20,100)
item2 _ Item(30,120)
item3 _ Item(10,60)
cList _ [item1, item2, item3]

knapsackMethod(cList, 50)
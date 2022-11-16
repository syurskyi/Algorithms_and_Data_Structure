#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# House Robber Problem  in Python

___ houseRobber(houses, currentIndex
    __ currentIndex >_ l..(houses
        r_ 0
    ____
        stealFirstHouse _ houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        skipFirstHouse _ houseRobber(houses, currentIndex+1)
        r_ m__(stealFirstHouse, skipFirstHouse)

houses _ [6,7,1,30,8,2,4]
print(houseRobber(houses, 0))
#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Coin Change Problem  in Python


___ coinChange(totalNumber, coins
    N _ totalNumber
    coins.sort()
    index _ l..(coins)-1
    _____ True:
        coinValue _ coins[index]
        __ N >_ coinValue:
            print(coinValue)
            N _ N - coinValue
        __ N < coinValue:
            index -_ 1
        
        __ N __ 0:
            break

coins _ [1,2,5,20,50,100]
coinChange(201, coins)

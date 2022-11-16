#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Number Factor Problem  in Python

___ numberFactor(n
    __ n __ (0,1,2
        r_ 1
    elif n __ 3:
        r_ 2
    ____
        subP1 _ numberFactor(n-1)
        subP2 _ numberFactor(n-3)
        subP3 _ numberFactor(n-4)
        r_ subP1+subP2+subP3

print(numberFactor(5))
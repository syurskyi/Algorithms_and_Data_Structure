#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Searching algorithms - Binary Search
import math
___ binarySearch(array, value
    start _ 0
    end _ len(array)-1
    middle _ math.floor((start+end)/2)
    _____ n..(array[middle]==value) and start<_end:
        __ value < array[middle]:
            end _ middle - 1
        ____
            start _ middle + 1
        middle _ math.floor((start+end)/2)
        # print(start, middle, end)
    __ array[middle] == value:
        r_ middle
    ____
        r_ -1
        



custArray _ [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))
# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#  S              M               E
#  S  M      E
#        SM  E
#            SME
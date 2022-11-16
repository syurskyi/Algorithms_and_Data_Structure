#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Convert One String to Another with minimum operation in Python

___ findMinOperation(s1, s2, index1, index2
    __ index1 == len(s1
        r_ len(s2)-index2
    __ index2 == len(s2
        r_ len(s1)-index1
    __ s1[index1] == s2[index2]:
        r_ findMinOperation(s1, s2, index1+1, index2+1)
    ____
        deleteOp _ 1 + findMinOperation(s1, s2, index1, index2+1)
        insertOp _ 1 + findMinOperation(s1, s2, index1+1, index2)
        replaceOp _ 1 + findMinOperation(s1, s2, index1+1, index2+1)
        r_ min (deleteOp, insertOp, replaceOp)

print(findMinOperation("table", "tbrltt", 0, 0))
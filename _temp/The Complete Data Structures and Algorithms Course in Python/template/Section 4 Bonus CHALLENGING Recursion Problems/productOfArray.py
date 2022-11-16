#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# productOfArray Solution

___ productOfArray(arr
    __ l..(arr) __ 0:
        r_ 1
    r_ arr[0] * productOfArray(arr[1:])

print(productOfArray([1,2,3])) #6
print(productOfArray([1,2,3,10])) #60


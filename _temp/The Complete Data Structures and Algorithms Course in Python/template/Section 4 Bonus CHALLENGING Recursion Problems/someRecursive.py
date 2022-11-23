#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# someRecursive Solution

___ someRecursive(arr, cb
    __ l..(arr) __ 0:
        r_ F..
    __ n..(cb(arr[0]
        r_ someRecursive(arr[1:], cb)
    r_ T..

___ isOdd(num
    __ num_2__0:
        r_ F..
    ____
        r_ T..


print(someRecursive([1,2,3,4], isOdd)) # true
print(someRecursive([4,6,8,9], isOdd)) # true
print(someRecursive([4,6,8], isOdd)) # false

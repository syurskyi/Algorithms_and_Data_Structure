#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# someRecursive Solution

___ someRecursive(arr, cb
    __ l..(arr) __ 0:
        r_ False
    __ n..(cb(arr[0])):
        r_ someRecursive(arr[1:], cb)
    r_ True

___ isOdd(num
    __ num%2__0:
        r_ False
    ____
        r_ True


print(someRecursive([1,2,3,4], isOdd)) # true
print(someRecursive([4,6,8,9], isOdd)) # true
print(someRecursive([4,6,8], isOdd)) # false

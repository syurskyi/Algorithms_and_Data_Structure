#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# flatten Solution
___ flatten(arr
    resultArr _    # list
    ___ custItem __ arr:
        __ type(custItem) __ list:
            resultArr.extend(flatten(custItem))
        ____ 
            resultArr.a..(custItem)
    r_ resultArr 



print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]
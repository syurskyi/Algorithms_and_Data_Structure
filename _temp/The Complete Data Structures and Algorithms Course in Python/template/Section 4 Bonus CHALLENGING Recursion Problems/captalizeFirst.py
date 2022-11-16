#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# capitalizeFirst Solution

___ capitalizeFirst(arr
    result _ []
    __ len(arr) == 0:
        r_ result
    result.append(arr[0][0].upper() + arr[0][1:])
    r_ result + capitalizeFirst(arr[1:]) 




print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']
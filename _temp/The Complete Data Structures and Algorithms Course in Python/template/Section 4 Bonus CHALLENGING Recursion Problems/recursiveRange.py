#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# recursiveRange Solution

___ recursiveRange(num
    __ num <_ 0:
        r_ 0
    r_ num + recursiveRange(num - 1)


print(recursiveRange(6))
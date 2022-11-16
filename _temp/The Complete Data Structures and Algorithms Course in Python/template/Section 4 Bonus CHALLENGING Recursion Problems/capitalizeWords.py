#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# capitalizeWords Solution

___ capitalizeWords(arr
    result _ []
    __ len(arr) == 0:
        r_ result
    result.append(arr[0].upper())
    r_ result + capitalizeWords(arr[1:])



words _ ['i', 'am', 'learning', '001_recursion']
print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']
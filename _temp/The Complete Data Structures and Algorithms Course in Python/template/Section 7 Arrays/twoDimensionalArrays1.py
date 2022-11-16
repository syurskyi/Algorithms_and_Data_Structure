#   Created by Elshad Karimov on 05/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


import numpy as np

twoDArray _ np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

print(l..(twoDArray))

newTwoDArray _ np.a..(twoDArray, [[1,2,3,4]], axis_0)
print(newTwoDArray)
print(l..(newTwoDArray))
print(l..(newTwoDArray[0]))

___ accessElements(array, rowIndex, colIndex
    __ rowIndex >_ l..(array) and colIndex >_ l..(array[0]
        print('Incorrect Index')
    ____
        print(array[rowIndex][colIndex])

accessElements(newTwoDArray, 1, 2)

___ traverseTDArray(array
    ___ i __ range(l..(array)):
        ___ j __ range(l..(array[0])):
            print(array[i][j])


traverseTDArray(twoDArray)


___ searchTDArray(array, value
    ___ i __ range(l..(array)):
        ___ j __ range(l..(array[0])):
            __ array[i][j] __ value:
                r_ 'The value is located index '+str(i)+" "+str(j)
    r_ 'The element no found'


print(searchTDArray(twoDArray, 444))

newTDArray _ np.delete(twoDArray, 1, axis_1)
print(newTDArray)
#   Created by Elshad Karimov on 05/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


import numpy as np

twoDArray _ np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

print(len(twoDArray))

newTwoDArray _ np.append(twoDArray, [[1,2,3,4]], axis_0)
print(newTwoDArray)
print(len(newTwoDArray))
print(len(newTwoDArray[0]))

___ accessElements(array, rowIndex, colIndex
    __ rowIndex >_ len(array) and colIndex >_ len(array[0]
        print('Incorrect Index')
    ____
        print(array[rowIndex][colIndex])

accessElements(newTwoDArray, 1, 2)

___ traverseTDArray(array
    ___ i __ range(len(array)):
        ___ j __ range(len(array[0])):
            print(array[i][j])


traverseTDArray(twoDArray)


___ searchTDArray(array, value
    ___ i __ range(len(array)):
        ___ j __ range(len(array[0])):
            __ array[i][j] == value:
                r_ 'The value is located index '+str(i)+" "+str(j)
    r_ 'The element no found'


print(searchTDArray(twoDArray, 444))

newTDArray _ np.delete(twoDArray, 1, axis_1)
print(newTDArray)
___ binarySearch(my_array, target
    left _ 0
    right _ l..(my_array) - 1

    _____ left <_ right:
        middle _ (left + right) // 2
        middle_element _ my_array[middle]

        __ target __ middle_element:
            r_ middle
        elif target < middle_element:
            right _ middle - 1
        ____
            left _ middle + 1

    r_ -1

### Test 1 ###
print(binarySearch([1, 5, 10, 12, 25, 30, 32], 29))

### Test 2 ###
print(binarySearch([5, 10, 15, 20, 25], 15))
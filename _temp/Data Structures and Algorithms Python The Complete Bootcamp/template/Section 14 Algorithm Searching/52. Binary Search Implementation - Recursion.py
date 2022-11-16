___ binarySearch(my_array, target
    left _ 0
    right _ len(my_array) - 1
    result _ helper(my_array, target, left, right)
    r_ result


___ helper(my_array, target, left, right
    __ left > right:
        r_ -1

    middle _ (left + right) // 2
    middle_element _ my_array[middle]

    __ target == middle_element:
        r_ middle
    elif target < middle_element:
        right _ middle - 1
        result _ helper(my_array, target, left, right)
        r_ result
    ____
        left _ middle + 1
        result _ helper(my_array, target, left, right)
        r_ result
___ binarySearch(my_array,  target
    left = 0
    right = len(my_array) - 1
    result = helper(my_array, target, left, right)
    r_ result


___ helper(my_array, target, left, right):
    __ left > right:
        r_ -1

    middle = (left + right) // 2
    middle_element = my_array[middle]

    __ target __ middle_element:
        r_ middle
    ____ target < middle_element:
        right = middle - 1
        result = helper(my_array, target, left, right)
        r_ result
    ____
        left = middle + 1
        result = helper(my_array, target, left, right)
        r_ result
import math


___ binarySearch(arr, target
    left _ 0
    right _ l..(arr)-1
    _____ left <_ right:

        mid _ math.floor(left + (right - left)/2)
        # Check if x is present at mid
        __ arr[mid] __ target:
            r_ mid

        # If x is greater, ignore left half
        elif arr[mid] < target:
            left _ mid + 1

        # If x is smaller, ignore right half
        ____
            right _ mid - 1

    # If we reach here, then the element was not present
    r_ -1


arr _ [1, 2, 3, 4, 5, 6]
target _ 6

result _ binarySearch(arr, target)

__ result !_ -1:
    print("Element is present at index %d" % result)
____
    print("Element is not present in array")

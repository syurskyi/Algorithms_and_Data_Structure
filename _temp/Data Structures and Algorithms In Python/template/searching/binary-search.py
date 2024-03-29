# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ binary_search(a, n, searchValue
    first _ 0
    last _ n-1

    _____ first <_ last :
        mid _ (first + last)//2
        __ searchValue < a[mid]:
            last _ mid-1     # Search in left half
        ____ searchValue > a[mid]:
            first _ mid+1    # Search in right half
        ____
            r_ mid	     # searchValue present at index mid
    r_ -1

####################################################

n _ i..(i..("Enter the number of elements : "))
a _ [N..]*n

print("Enter the elements in sorted order  - ")
___ i __ r..(n
    a[i] _ i..(i..("Enter element : "))

searchValue _ i..(i..("Enter the search value : "))

index _ binary_search(a, n, searchValue)

__ index __ -1:
    print("Value " , searchValue , " not present in the array")
____
    print("Value " , searchValue , " present at index " , index)



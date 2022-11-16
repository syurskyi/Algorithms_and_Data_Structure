# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ binary_search(a, n, searchValue
    r_ _search(a, 0, n-1, searchValue)

___ _search(a, first, last, searchValue
    __ (first > last
        r_ -1
    mid _ (first + last) // 2
    __ searchValue > a[mid]:	 #Search in right half
        r_ _search(a, mid+1, last, searchValue)
    elif searchValue < a[mid]:	 #Search in left half
        r_ _search(a, first, mid-1, searchValue)
    ____
        r_ mid
    
############################################################
    
n _ int(input("Enter the number of elements : "))
a _ [N..]*n
print("Enter the elements in sorted order  - ")
___ i __ range(n
    a[i] _ int(input("Enter element : "))

searchValue _ int(input("Enter the search value : "))
index _ binary_search(a, n, searchValue)

__ index == -1:
    print("Value " , searchValue , " not present in the array")
____
    print("Value " , searchValue , " present at index " , index)

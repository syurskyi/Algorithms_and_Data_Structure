# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ Search(a, n, searchValue
    ___ i __ range(n
        __ a[i] __ searchValue:
            r_ i
    r_ -1


#######################################################

n _ int(input("Enter the number of elements : "))
a _ [N..]*n
print("Enter the elements - ")
___ i __ range(n
    a[i] _ int(input("Enter element : "))

searchValue _ int(input("Enter the search value : "))
index _ Search(a, n, searchValue)

__ index __ -1:
    print("Value " , searchValue , " not present in the list")
____
    print("Value " , searchValue , " present at index " , index)

    



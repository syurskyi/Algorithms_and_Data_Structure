# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ Search(a, n, searchValue
    a[n] _ searchValue
    i _ 0
    _____ searchValue !_ a[i]:
        i+_1
    __ i < n:
        r_ i
    ____
        r_ -1


n _ int(input("Enter the number of elements : "))
a _ [N..]*(n+1)
print("Enter the elements - ")
___ i __ r..(n
    a[i] _ int(input("Enter element : "))

searchValue _ int(input("Enter the search value : "))
index _ Search(a, n, searchValue)

__ index __ -1:
    print("Value ", searchValue ," not present in the list")
____
    print("Value ", searchValue ," present at index " , index)

    



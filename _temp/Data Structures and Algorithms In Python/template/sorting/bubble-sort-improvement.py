# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ bubble_sort(a
    ___ x __ r..(l..(a)-1,0,-1
        swaps_0
        ___ j __ r..(x
              __ a[j]>a[j+1]:
                  a[j],a[j+1] _ a[j+1],a[j]
                  swaps+_1
        __ swaps __ 0:
            break

####################################

list1 _ [6,3,1,5,9,8]
bubble_sort(list1)
print(list1)

list2 _ [2,3,5,39,11,8,9,166,45,23]
bubble_sort(list2)
print(list2)

list3 _ [1,2,3,4,5,6,7,8,9,10]
bubble_sort(list3)
print(list3)

list4 _ [10,9,8,7,6,5,4,3,2,1]
bubble_sort(list4)
print(list4)

list5 _ [4]
bubble_sort(list5)
print(list5)

#####################################

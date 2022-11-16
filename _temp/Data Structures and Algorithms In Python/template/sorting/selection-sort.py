# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ selection_sort(a
    ___ i __ range(len(a)-1   
        minIndex _ i
        ___ j __ range(i+1,len(a)):
            __ a[j] < a[minIndex]:
                    minIndex _ j
        __ i!_minIndex:
            a[i],a[minIndex] _ a[minIndex],a[i]


####################################

list1 _ [6,3,1,5,9,8]
selection_sort(list1)
print(list1)

list2 _ [2,3,5,39,11,8,9,166,45,23]
selection_sort(list2)
print(list2)

list3 _ [1,2,3,4,5,6,7,8,9,10]
selection_sort(list3)
print(list3)

list4 _ [10,9,8,7,6,5,4,3,2,1]
selection_sort(list4)
print(list4)

list5 _ [4]
selection_sort(list5)
print(list5)

#####################################


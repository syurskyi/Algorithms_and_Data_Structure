# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ quick_sort(a
    sort(a,0,len(a)-1)
    
___ sort(a, low, up
    __ low >_ up: # zero or one element in sublist
        r_
    p _ partition(a,low,up)
    sort(a,low,p-1)  # Sort left sublist
    sort(a,p+1,up)   # Sort right sublist
    
___ partition(a, low, up
    pivot _ a[low]
    i _ low+1  # moves from left to right
    j _ up     # moves from right to left

    _____ i <_ j:
        _____ a[i] < pivot and i < up:
            i+_1
        _____ a[j] > pivot:
            j-_1

        __  i < j: # swap a[i] and a[j]
            temp _ a[i]
            a[i] _ a[j]
            a[j] _ temp
            i+_1
            j-_1
        ____ # found proper place for pivot
            break
            
    # Proper place for pivot is j
    a[low] _ a[j]
    a[j] _ pivot
    
    r_ j

####################################

list1 _ [6,3,1,5,9,8]
quick_sort(list1)
print(list1)

list2 _ [2,3,5,39,11,8,9,166,45,23]
quick_sort(list2)
print(list2)

list3 _ [1,2,3,4,5,6,7,8,9,10]
quick_sort(list3)
print(list3)

list4 _ [10,9,8,7,6,5,4,3,2,1]
quick_sort(list4)
print(list4)

list5 _ [4]
quick_sort(list5)
print(list5)

#####################################


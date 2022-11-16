# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ merge_sort(a
    n_len(a)
    temp _ [N..]*n
    sort(a,temp,0,n-1)
             

___ sort(a,temp,low,up
    __ low == up: # only one element
        r_

    mid _ (low + up)//2

    sort(a, temp, low, mid)  # Sort a[low]....a[mid]
    sort(a, temp, mid+1, up) # Sort a[mid+1]....a[up]

    # Merge a[low]...a[mid] and a[mid+1]....a[up] to temp[low]...temp[up]
    merge(a, temp, low, mid, mid+1, up)
    	
    # Copy temp[low]...temp[up] to a[low]...a[up]
    copy(a, temp, low, up)
    

# a[low1]...a[up1] and a[low2]...a[up2] merged to temp[low1]...temp[up2] 
___ merge(a, temp, low1, up1, low2, up2
    i _ low1
    j _ low2
    k _ low1

    _____ i <_ up1  and j <_ up2:
            __ a[i] <_ a[j]:
                temp[k] _ a[i]
                i+_1
            ____
                temp[k] _ a[j]
                j+_1
            k+_1
    
    _____ i <_ up1:
                temp[k] _ a[i]
                i+_1
                k+_1
            
    _____ j <_ up2:
                temp[k] _ a[j]
                j+_1
                k+_1

# copies temp[low]....temp[up] to a[low]...a[up]
___ copy(a, temp, low, up
    ___ i __ range(low,up+1
        a[i] _ temp[i]


#############################################################    
             
list1 _ [6,3,1,5,9,8]
merge_sort(list1)
print(list1)

list2 _ [2,3,5,39,11,8,9,166,45,23]
merge_sort(list2)
print(list2)

list3 _ [1,2,3,4,5,6,7,8,9,10]
merge_sort(list3)
print(list3)

list4 _ [10,9,8,7,6,5,4,3,2,1]
merge_sort(list4)
print(list4)

list5 _ [4]
merge_sort(list5)
print(list5)

#################################################################



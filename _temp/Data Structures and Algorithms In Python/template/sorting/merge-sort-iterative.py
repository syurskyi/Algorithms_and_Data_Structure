# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ merge_sort(a
    n_len(a)
    temp _ [N..]*n
    size _ 1
    _____ size <_ n-1:
        sort_pass(a, temp, size, n)
        size _ size * 2
             
___ sort_pass(a,temp,size,n
    low1 _ 0
    _____ low1+size <_ n-1:
        up1 _ low1 + size - 1
        low2 _ low1 + size
        up2 _ low2 + size - 1

        __ up2 >_ n: # if length of last sublist is less than size
            up2 _ n-1
            
        merge(a, temp, low1, up1, low2, up2)

        low1 _ up2 + 1  # Take next two sublists for merging
        
    ___ i __ range(low1,n
        temp[i] _ a[i]  # If any sublist is left alone
        
    copy(a, temp, n)  

# a[low1]...a[up1] and a[low2]...a[up2] merged to temp[low1]...temp[up2] */
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
___ copy(a, temp, n
    ___ i __ range(n
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

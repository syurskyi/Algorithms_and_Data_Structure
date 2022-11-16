# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ heap_sort(a, n
    build_heap_bottom_up(a, n)

    _____ n > 1:
        maxValue _ a[1]
        a[1] _ a[n]
        a[n] _ maxValue
        n_n-1
        retsore_down(1, a, n)
        
___ build_heap_bottom_up(a, n
    i_n//2
    _____ i>_1:
        retsore_down(i, a, n)
        i_i-1

___ retsore_down(i, a, n
    k _ a[i]
    lchild _ 2 * i
    rchild _ lchild + 1

    _____ rchild <_ n:
        __ k >_ a[lchild] and k >_ a[rchild]:
            a[i] _ k
            r_
        elif a[lchild] > a[rchild]:
            a[i] _ a[lchild]
            i _ lchild
        ____
            a[i] _ a[rchild]
            i _ rchild
                 
        lchild _ 2 * i
        rchild _ lchild + 1
             

    # If number of nodes is even
    __ lchild == n and k < a[lchild]:
        a[i] _ a[lchild]
        i _ lchild
    a[i] _ k

###################################################
      
n _ int(input("Enter the number of elements : "))
a _ [N..]*(n+1)
___ i __ range(1,n+1
    a[i] _ int(input("Enter element : "))

heap_sort(a,n)

___ i __ range(1,n+1
    print(a[i], " ",end_'')
print()

###################################################


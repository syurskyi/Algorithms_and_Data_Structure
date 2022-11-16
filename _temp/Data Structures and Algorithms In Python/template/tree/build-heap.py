# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ build_heap_top_down(a, n
    ___ i __ r..(2, n+1
        restore_up(i, a)

___ build_heap_bottom_up(a, n
    i_n//2
    _____ i>_1:
        restore_down(i, a, n)
        i_i-1
       
___ restore_up(i, a
    k _ a[i]
    iparent _ i // 2

    _____ a[iparent] < k :
        a[i] _ a[iparent]
        i _ iparent
        iparent _ i // 2
    a[i] _ k

___ restore_down(i, a, n
    k _ a[i]
    lchild _ 2 * i
    rchild _ lchild + 1

    _____ rchild <_ n:
        __ k >_ a[lchild] ___ k >_ a[rchild]:
            a[i] _ k
            r_
        ____ a[lchild] > a[rchild]:
            a[i] _ a[lchild]
            i _ lchild
        ____
            a[i] _ a[rchild]
            i _ rchild
                 
        lchild _ 2 * i
        rchild _ lchild + 1
             

        # If number of nodes is even
        __ lchild __ n ___ k < a[lchild]:
            a[i] _ a[lchild]
            i _ lchild
        a[i] _ k
     
####################################################
        
a1_[99999,20,33,15,6,40,60,45,16,75,10,80,12]
n1 _ l..(a1)-1

build_heap_bottom_up(a1,n1)

___ i __ r..(1,n1+1
    print(a1[i], " ",end_'')
print()

a2_[99999,20,33,15,6,40,60,45,16,75,10,80,12]
n2 _ l..(a2)-1

build_heap_top_down(a2,n2) 

___ i __ r..(1,n2+1
    print(a2[i], " ",end_'')
print()

####################################################

         
     
 

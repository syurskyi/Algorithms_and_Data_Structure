# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ HeapEmptyError(Exception
    pass

c_ Heap:

    ___ - maxSize_10
        a _ [N..]*maxSize
        n _ 0
        a[0] _ 99999
         
    ___ insert value
        n+_1
        a[n] _ value
        restore_up(n)
     
    ___ restore_upi
        k _ a[i]
        iparent _ i // 2

        _____ a[iparent] < k: # No sentinel - while(iparent>=1 && self.a[iparent]<k)
            a[i] _ a[iparent]
            i _ iparent
            iparent _ i // 2
        a[i] _ k
    
    ___ delete_root 
        __ n __ 0:
            raise HeapEmptyError("Heap is empty")

        maxValue _ a[1]
        a[1] _ a[n]
        n-_1
        restore_down(1)
        r_ maxValue
     

    ___ restore_down i
        k _ a[i]
        lchild _ 2*i
        rchild _ lchild+1

        _____ rchild <_ n:
            __ k >_ a[lchild] and k >_ a[rchild]:
                a[i] _ k
                r_
            ____
                __ a[lchild] > a[rchild]:
                    a[i] _ a[lchild]
                    i _ lchild
                ____
                    a[i] _ a[rchild]
                    i _ rchild
             
            lchild _ 2 * i
            rchild _ lchild + 1

        # If number of nodes is even 
        __ lchild __ n and k < a[lchild]:
            a[i] _ a[lchild]
            i _ lchild
        a[i] _ k

    ___ display 
        __ n __ 0:
            print("Heap is empty")
            r_
        print("Heap size = " , n)
        ___ i __ range(1,n+1
                print(a[i] , " ", end _' ')
        print() 

######################################################
        
h _ Heap(20)
_____ True:
    print("1.Insert")
    print("2.Delete root")
    print("3.Display")
    print("4.Exit")
    print("Enter your choice : ")
    choice _ int(input("Enter your choice : "))

    __ choice __ 1:
        value _ int(input("Enter the value to be inserted : "))
        h.insert(value)
    elif choice __ 2:
        print("Maximum value is " , h.delete_root())
    elif choice __ 3:
        h.display()
    elif choice __ 4:
        break
    ____
         print("Wrong choice")
        


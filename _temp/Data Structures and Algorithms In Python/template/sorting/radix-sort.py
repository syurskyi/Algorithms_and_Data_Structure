# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ Node:
    ___ - value
        info _ value
        link _ N..
   
___ radix_sort(start
    
    rear _ [N..] * 10
    front _ [N..] * 10

    leastSigPos _ 1
    mostSigPos _ DigitsInLargest(start)

    ___ k __ r..(leastSigPos, mostSigPos+1
        #Making all the queues empty at the beginning of each pass
        ___ i __ r..(10
            rear[i] _ N..
            front[i] _ N..

        p _ start
        _____ p __ n.. N..:
            #Find kth digit from right in the number
            dig _ Digit(?.i.., k)

            #Insert the node in Queue(dig)
            __ front[dig] __ N..:
                front[dig] _ p
            ____
                rear[dig].l.. _ p
            rear[dig] _ p

            p_p.l..
               
        #Join all queues to form new linked list
        i _ 0
        _____ front[i] __ N..:  #Finding first non empty queue
            i_i+1

        start _ front[i]
        _____ i <_ 8:
            __ rear[i+1] __ n.. N..:   #if (i+1)th  queue is not empty
                rear[i].l.. _ front[i+1] #join end of ith queue to start of (i+1)th queue
            ____
                rear[i+1] _ rear[i]  #continue with rear[i]
            i_i+1
        rear[9].l.. _ N..
    r_ start

#Returns number of digits in the largest element of the list
___ DigitsInLargest(start
    #Find largest element
    large _ 0
    p _ start
    _____ p __ n.. N..:
        __ ?.i.. > large:
            large _ ?.i..
        p _ ?.l..
        
    #Find number of digits in largest element
    ndigits _ 0
    _____ large !_ 0:
        ndigits _ ndigits+1
        large//_10
    r_ ndigits
   
#Returns kth digit from right in n
___ Digit(n, k
    d _ 0
    ___ i __ r..(1,k+1
        d _ n%10
        n//_10
    r_ d
        

#################################################
start _ N..

n _ i..(i..("Enter the number of elements : "))

___ i __ r..(n  #Inserting elements in linked list
    data _ i..(i..("Enter element : "))

    temp _ ? ?
    __ start __ N..:
        start _ temp
    ____
        p _ start
        _____ ?.l.. __ n.. N..:
            p _ ?.l..
        ?.l.. _ temp
            
start _ radix_sort(start)

print("Sorted list is : ") 
p _ start
_____ p __ n.. N.. :
    print(?.i.. , " ")
    p _ ?.l..
print 

##################################################


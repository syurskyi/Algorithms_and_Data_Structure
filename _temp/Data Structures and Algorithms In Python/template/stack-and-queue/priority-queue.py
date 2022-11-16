# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyQueueError(Exception
    pass

c_ Node:

    ___ - value,pr
        info _ value
        priority _ pr
        link _ N..
        
c_ PriorityQueue:

    ___ -
        front _ N..

    ___ enqueue data, data_priority

        temp _ Node(data, data_priority)
        
        #If queue is empty or element to be added has priority more than first element
        __ is_empty() __ data_priority < front.priority:
            temp.link _ front
            front _ temp
        ____
            p _ front
            _____ p.link !_ N.. ___ p.link.priority <_ data_priority:
                p _ p.link
            temp.link _ p.link
            p.link _ temp
                 
    ___ dequeue
        __ is_empty(
            raise EmptyQueueError("Queue is empty")
        x _ front.info
        front _ front.link
        r_ x
    
    ___ is_empty
        r_ front __ N..
            
    ___ display
        __ is_empty(
            print("Queue is empty")
            r_

        print("Queue is : ")
        p _ front
        _____ p __ n.. N..:
            print(p.info , "     ", p.priority)
            p _ p.link
        print()
    
    ___ size
        n _ 0
        p _ front
        _____ p __ n.. N..:
            n+_1
            p _ p.link
        r_ n
    
    
    
#########################################################################################

__ __name__ __ "__main__":
    qu _ PriorityQueue()

    _____ T..:
        print("1.Enqueue") 
        print("2.Dequeue") 
        print("3.Display all queue elements") 
        print("4.Display size of the queue")  
        print("5.Quit") 
         
        choice _ int(input("Enter your choice : "))

        __ choice __ 1:
            x _ int(input("Enter the element : "))
            pr _ int(input("Enter its priority : "))
            qu.enqueue(x,pr) 
        ____ choice __ 2:
            x_qu.dequeue()
            print("Element is : " , x) 
        ____ choice __ 3:
            qu.display() 
        ____ choice __ 4:
            print("Size of queue " , qu.size()) 
        ____ choice __ 5:
          break;
        ____
          print("Wrong choice") 
        print() 

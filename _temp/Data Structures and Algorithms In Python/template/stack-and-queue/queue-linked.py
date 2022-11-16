# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyQueueError(Exception
    pass

c_ Node:

    ___ - value
        info _ value
        link _ N..
                
c_ Queue:

    ___ -  
        front _ N..
        rear _ N..
        size_queue _ 0

    ___ is_empty 
        r_ front __ N..
    
    ___ size 
        r_ size_queue
    
    ___ enqueue data
        temp _ Node(data)
        __ front __ N..:
            front _ temp
        ____
            rear.link _ temp
        rear _ temp
        size_queue+_1
                 
    ___ dequeue 
        __ is_empty(
            raise EmptyQueueError("Queue is empty")
        x _ front.info
        front _ front.link
        size_queue-_1
        r_ x

    ___ peek 
        __ is_empty(
            raise EmptyQueueError("Queue is empty")
        r_ front.info
        
    ___ display 
        __ is_empty(
            print("Queue is empty")
            r_
        print("Queue is :   ")
        p _ front
        _____ p __ n.. N..:
            print(p.info, " ", end_'')
            p _ p.link
        print()
    
    
#########################################################################################

__ __name__ __ "__main__":
    qu _ Queue()

    _____ True:
        print("1.Enqueue") 
        print("2.Dequeue")
        print("3.Peek")
        print("4.Size") 
        print("5.Display")  
        print("6.Quit") 
         
        choice _ int(input("Enter your choice : "))

        __ choice __ 1:
            x_int(input("Enter the element : "))
            qu.enqueue(x) 
        elif choice __ 2:
            x_qu.dequeue()
            print("Element deleted from the queue is : " , x) 
        elif choice __ 3:
            print("Element at the front end is " , qu.peek()) 
        elif choice __ 4:
            print("Size of queue ", qu.size()) 
        elif choice __ 5:
            qu.display() 
        elif choice __ 6:
          break;
        ____
          print("Wrong choice") 
        print()
        

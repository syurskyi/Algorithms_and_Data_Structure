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
        rear _ N..
       
    ___ is_empty
        r_ rear __ N..
            
    ___ size
        __ is_empty(
            r_ 0
        n _ 0
        p _ rear.link
        _____ T..:
            n+_1
            p _ p.link
            __  p __ rear.link:
                break
        r_ n
    
    ___ enqueue data
        temp _ Node(data)
        
        __ is_empty(
            rear _ temp
            rear.link _ rear
        ____
            temp.link _ rear.link
            rear.link _ temp
            rear _ temp
        
    ___ dequeue
        __ is_empty(
            raise EmptyQueueError("Queue is Empty")
        
        __ rear.link __ rear: #List has only one node
            temp _ rear
            rear _ N..
        ____
            temp _ rear.link
            rear.link _ rear.link.link
        r_ temp.info

    ___ peek
        __ is_empty(
            raise EmptyQueueError("Queue is Empty")
        r_ rear.link.info

    ___ display
        __ is_empty(
            print("List is empty")
            r_

        p _ rear.link
        _____ T..:
            print(p.info , " ",end_'')
            p _ p.link
            __ p __ rear.link:
                break
        print()
        
########################################################################

__ __name__ __ "__main__":
    qu _ Queue()

    _____ T..:
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
        ____ choice __ 2:
            x_qu.dequeue()
            print("Element deleted from the queue is : " , x) 
        ____ choice __ 3:
            print("Element at the front end is " , qu.peek()) 
        ____ choice __ 4:
            print("Size of queue ", qu.size()) 
        ____ choice __ 5:
            qu.display() 
        ____ choice __ 6:
          break;
        ____
          print("Wrong choice") 
        print()


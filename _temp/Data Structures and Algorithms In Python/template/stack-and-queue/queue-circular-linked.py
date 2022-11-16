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
        r_ rear == N..
            
    ___ size
        __ is_empty(
            r_ 0
        n _ 0
        p _ rear.link
        _____ True:
            n+_1
            p _ p.link
            __  p == rear.link:
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
        
        __ rear.link == rear: #List has only one node
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
        _____ True:
            print(p.info , " ",end_'')
            p _ p.link
            __ p == rear.link:
                break
        print()
        
########################################################################

__ __name__ == "__main__":
    qu _ Queue()

    _____ True:
        print("1.Enqueue") 
        print("2.Dequeue")
        print("3.Peek")
        print("4.Size") 
        print("5.Display")  
        print("6.Quit") 
         
        choice _ int(input("Enter your choice : "))

        __ choice == 1:
            x_int(input("Enter the element : "))
            qu.enqueue(x) 
        elif choice == 2:
            x_qu.dequeue()
            print("Element deleted from the queue is : " , x) 
        elif choice == 3:
            print("Element at the front end is " , qu.peek()) 
        elif choice == 4:
            print("Size of queue ", qu.size()) 
        elif choice == 5:
            qu.display() 
        elif choice == 6:
          break;
        ____
          print("Wrong choice") 
        print()


# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyQueueError(Exception
    pass

c_ Queue:
  
    ___ -  
        items _    # list

    ___ is_empty 
        r_ items __    # list

    ___ size 
        r_ l..(items)

    ___ enqueue item
        items.a..(item)
        
    ___ dequeue 
        __ is_empty(
            raise EmptyQueueError("Queue is Empty")
        r_ items.pop(0)
    
    ___ peek 
        __ is_empty(
            raise EmptyQueueError("Queue is Empty")
        r_ items[0]

    ___ display 
        print(items)
        
###########################################################

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



# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ E.. E..
    p..

c_ Queue:
    
    ___ -  
        items _    # list
        front _ 0
      
    ___ is_empty 
        r_ front __ l..(items)
    
    ___ size 
        r_ l..(items)-front
        
    ___ enqueue item
        items.a..(item)
        
    ___ dequeue 
        __ is_empty(
            r... E..("Queue is Empty")
        
        x _ items[front]
        items[front] _ N..
        front _ front + 1
        r_ x
    
    ___ peek 
        __ is_empty(
            r... E..("Queue is Empty")
        
        r_ items[front]
        
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
         
        choice _ i..(i..("Enter your choice : "))

        __ choice __ 1:
            x_int(i..("Enter the element : "))
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
          b..;
        ____
          print("Wrong choice") 
        print()


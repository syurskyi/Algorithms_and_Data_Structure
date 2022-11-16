# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyQueueError(Exception
    pass

c_ Queue:
    
    ___ - default_size_10
        items _ [N..] * default_size
        front _ 0
        count _ 0

    ___ is_empty 
        r_ count __ 0

    ___ size 
        r_ count
    
    ___ enqueue item
        __ count __ l..(items
            resize( 2*l..(items) )
            
        i _ (front + count) % l..(items)
        items[i] _ item
        count+_1
        
    ___ dequeue 
        __ is_empty(
            raise EmptyQueueError("Queue is empty")

        x _ items[front]
        items[front] _ N..
        front _ (front + 1) % l..(items)
        count-_1
        r_ x

    ___ peek 
        __ is_empty(
            raise EmptyQueueError("Queue is empty")
        r_ items[front]
        
    ___ display 
        print(items)
        
    ___ resizenewsize
        old_list _ items
        items _ [N..]*newsize
        i _ front
        ___ j __ r..(count
            items[j] _ old_list[i]
            i _ (1+i)%l..(old_list)
        front _ 0

###########################################################

__ __name__ __ "__main__":
    qu _ Queue(6)

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
          break
        ____
          print("Wrong choice") 
        print()

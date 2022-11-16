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
        r_ count == 0

    ___ size 
        r_ count
    
    ___ enqueue item
        __ count == len(items
            resize( 2*len(items) )
            
        i _ (front + count) % len(items)
        items[i] _ item
        count+_1
        
    ___ dequeue 
        __ is_empty(
            raise EmptyQueueError("Queue is empty")

        x _ items[front]
        items[front] _ N..
        front _ (front + 1) % len(items)
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
        ___ j __ range(count
            items[j] _ old_list[i]
            i _ (1+i)%len(old_list)
        front _ 0

###########################################################

__ __name__ == "__main__":
    qu _ Queue(6)

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
          break
        ____
          print("Wrong choice") 
        print()

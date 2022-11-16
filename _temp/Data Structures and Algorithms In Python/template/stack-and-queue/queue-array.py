# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyQueueError(Exception
    pass

c_ Queue:
  
    ___ -  
        items _ []

    ___ is_empty 
        r_ items == []

    ___ size 
        r_ len(items)

    ___ enqueue item
        items.append(item)
        
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



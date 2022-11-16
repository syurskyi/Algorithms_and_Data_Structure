# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyQueueError(Exception
    pass
       
c_ Deque:

    ___ - default_size_10
        items _ [N..] * default_size
        front _ 0
        count _ 0
    
    ___ is_empty 
        r_ count == 0
    
    ___ size 
        r_ count
    
    ___ insert_front item
        __ count == len(items
            resize( 2*len(items) )

        front _ (front - 1) % len(items)
        items[front] _ item
        count+_1
        
    ___ insert_rear item
        __ count == len(items
            resize( 2*len(items) )
            
        i _ (front + count) % len(items)
        items[i] _ item
        count+_1
        
    ___ delete_front 
        __ is_empty(
            raise EmptyQueueError("Queue is empty")

        x _ items[front]
        items[front] _ N..
        front _ (front + 1) % len(items)
        count-_1
        r_ x
       
    ___ delete_rear 
        __ is_empty(
            raise EmptyQueueError("Queue is empty")
        rear _ (front + count - 1) % len(items)
        x _ items[rear]
        items[rear] _ N..
        count-_1
        r_ x
        
    ___ first 
        __ is_empty(
            raise EmptyQueueError("Queue is empty")
        r_ items[front]

    ___ last 
        __ is_empty(
            raise EmptyQueueError("Queue is empty")
        rear _ (front + count - 1) % len(items)
        r_ items[rear]    

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
        
####################################################################

__ __name__ == "__main__":
    qu _ Deque(6)

    _____ True:
        print("1.Insert at the front end")
        print("2.Insert at the rear end")
        print("3.Delete from front end")
        print("4.Delete from rear end")
        print("5.Display first element")
        print("6.Display last element")
        print("7.Display")
        print("8.Size")
        print("9.Quit")
             
        choice _ int(input("Enter your choice : "))

        __ choice == 1:
            x_int(input("Enter the element : "))
            qu.insert_front(x)
        elif choice== 2:
            x_int(input("Enter the element : "))
            qu.insert_rear(x)
        elif choice == 3:
            x _ qu.delete_front()
            print("Element deleted from front end is  ", x)
        elif choice == 4:
            x _ qu.delete_rear()
            print("Element deleted from rear end is  ", x)
        elif choice == 5:
            print("First element is  ", qu.first())
        elif choice == 6:
            print("Last element is  ", qu.last())
        elif choice == 7:
            qu.display()
        elif choice == 8:
            print("Size of queue " , qu.size())
        elif choice == 9:
            break
        ____
            print("Wrong choice")
        print()


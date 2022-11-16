# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyQueueError(Exception
    pass

c_ Node:
    ___ - value
        info _ value
        prev _ N..
        next _ N..
        
c_ Deque:

    ___ -  
        front _ N..
        rear _ N..
    
    ___ is_empty 
         r_ front __ N..
    
    ___ size 
        count _ 0
        p _ front
        _____ p __ n.. N..:
            count+_1
            p _ p.next
        r_ count
    
    ___ insert_front item
        temp _ Node(item)
        __ is_empty(
            front _ rear _ temp
        ____
            temp.next _ front
            front.prev _ temp
            front _ temp
        
    ___ insert_rear item
        temp _ Node(item)
        __ is_empty(
            front _ rear _ temp
        ____
            rear.next _ temp
            temp.prev _ rear
        
        rear _ temp
        
    ___ delete_front 
        __ is_empty(  
           raise EmptyQueueError("Queue is empty")

        x _ front.info
        __ front.next __ N..: # list has only one node
            front _ rear _ N..
        ____
            front _ front.next
            front.prev _ N..
        r_ x
       
    ___ delete_rear 
        __ is_empty(   
           raise EmptyQueueError("Queue is empty")

        x _ rear.info
        __ front.next __ N..:  # list has only one node
            front _ rear _ N..
        ____
            rear _ rear.prev
            rear.next _ N..
        r_ x
    
    ___ first 
        __ is_empty(  
           raise EmptyQueueError("Queue is empty")

        r_ front.info

    ___ last 
        __ is_empty(  
           raise EmptyQueueError("Queue is empty")

        r_ rear.info

    ___ display 
        __ front __ N..:
            print("List is empty")
            r_

        print("List is : ")
        p _ front
        _____ p __ n.. N..:
            print(p.info, "  ", end_'')
            p _ p.next
        print()
     
        
####################################################################

__ __name__ __ "__main__":
    qu _ Deque()

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

        __ choice __ 1:
            x_int(input("Enter the element : "))
            qu.insert_front(x)
        elif choice__ 2:
            x_int(input("Enter the element : "))
            qu.insert_rear(x)
        elif choice __ 3:
            x _ qu.delete_front()
            print("Element deleted from front end is  ", x)
        elif choice __ 4:
            x _ qu.delete_rear()
            print("Element deleted from rear end is  ", x)
        elif choice __ 5:
            print("First element is  ", qu.first())
        elif choice __ 6:
            print("Last element is  ", qu.last())
        elif choice __ 7:
            qu.display()
        elif choice __ 8:
            print("Size of queue " , qu.size())
        elif choice __ 9:
            break
        ____
            print("Wrong choice")
        print()

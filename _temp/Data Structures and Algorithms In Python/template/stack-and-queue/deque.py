# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyQueueError(Exception
    pass

c_ Deque:
    ___ -
        items _ []

    ___ is_empty
        r_ items == []

    ___ size
        r_ len(items)

    ___ insert_front item
        items.insert(0,item)
    
    ___ insert_rear item
        items.append(item)

    ___ delete_front
        __ is_empty(
            raise EmptyQueueError("Queue is Empty")
        r_ items.pop(0)
        
    ___ delete_rear
        __ is_empty(
            raise EmptyQueueError("Queue is Empty")
        r_ items.pop()

    ___ first
        __ is_empty(
            raise EmptyQueueError("Queue is Empty")
        r_ items[0]

    ___ last
        __ is_empty(
            raise EmptyQueueError("Queue is Empty")
        r_ items[-1]
    
    ___ display
        print(items)

####################################################################
__ __name__ == "__main__":
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


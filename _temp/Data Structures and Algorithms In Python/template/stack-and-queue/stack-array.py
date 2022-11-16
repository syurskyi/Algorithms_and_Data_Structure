# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyStackError(Exception
    pass

c_ Stack:
        
    ___ -
        items _    # list

    ___ is_empty
        r_ items __    # list

    ___ size
        r_ l..(items)

    ___ push item
        items.a..(item)

    ___ pop
        __ is_empty(
            raise EmptyStackError("Stack is empty")
        r_ items.pop()
    
    ___ peek
        __ is_empty(
            raise EmptyStackError("Stack is empty")
        r_ items[l..(items)-1]

    ___ display
        print(items)

###########################################################

__ __name__ __ "__main__":
    st _ Stack()

    _____ True:
        print("1.Push") 
        print("2.Pop") 
        print("3.Peek") 
        print("4.Size")
        print("5.Display") 
        print("6.Quit")
         
        choice _ int(input("Enter your choice : "))

        __ choice __ 1:
            x_int(input("Enter the element to be pushed : "))
            st.push(x) 
        elif choice __ 2:
            x_st.pop()
            print("Popped element is : " , x) 
        elif choice __ 3:
            print("Element at the top is : " , st.peek()) 
        elif choice __ 4:
            print("Size of stack " , st.size()) 
        elif choice __ 5:
            st.display()         
        elif choice __ 6:
          break;
        ____
          print("Wrong choice") 
        print() 


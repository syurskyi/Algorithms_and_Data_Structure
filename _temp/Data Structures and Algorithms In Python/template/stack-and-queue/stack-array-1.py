# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ StackEmptyError(Exception
    pass

c_ StackFullError(Exception
    pass

c_ Stack:
    
    ___ - max_size_10
        items _ [N..] * max_size
        count _ 0

    ___ size 
        r_ count

    ___ is_empty 
        r_ count __ 0

    ___ is_full 
        r_ count __ l..(items)
    
    ___ pushx
        __ is_full(
            raise StackFullError("Stack is full, can't push")

        items[count] _ x
        count+_1
            
    ___ pop 
        __ is_empty(
            raise StackEmptyError("Stack is empty, can't pop")
             
        x _ items[count-1]
        items[count-1] _ N..
        count-_1
        r_ x

    ___ peek 
        __ is_empty(
            raise StackEmptyError("Stack is empty, can't peek")

        r_ items[count-1]
    
    ___ display 
        print(items)
     
##########################################################

__ __name__ __ "__main__":

    st _ Stack(8)
    
    _____ True:
        print("1.Push") 
        print("2.Pop") 
        print("3.Peek") 
        print("4.Size")
        print("4.Display") 
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
          break
        ____
          print("Wrong choice") 
        print()

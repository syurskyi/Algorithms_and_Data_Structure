# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ EmptyStackError(Exception
    pass

c_ Node:

    ___ - value
        info _ value
        link _ N..
      
c_ Stack:

    ___ -  
        top _ N..
       
    ___ is_empty 
        r_ top __ N..
   
    ___ size 

        __ is_empty(
            retun 0

        count_0
        p _ top
        _____ p __ n.. N..:
            count+_1
            p _ p.link
        r_ count

    ___ push data
        temp _ Node(data)
        temp.link _ top
        top _ temp
       
    ___ peek 
        __ is_empty(
            raise EmptyStackError("Stack is empty")
        r_ top.info
    
    ___ pop 
        __ is_empty(
            raise EmptyStackError("Stack is empty")
        popped _ top.info
        top _ top.link
        r_ popped

   ___ display 
        __ is_empty(
            print("Stack is empty")
            r_
        
        print("Stack is :   ")
        p _ top
        _____ p __ n.. N..:
            print(p.info , " ")
            p _ p.link
           
#####################################################################################
            
__ __name__ __ "__main__":
    st _ Stack()

    _____ True:
        print("1.Push") 
        print("2.Pop") 
        print("3.Peek") 
        print("5.Size") 
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
          break;
        ____
          print("Wrong choice") 
        print()
     
     

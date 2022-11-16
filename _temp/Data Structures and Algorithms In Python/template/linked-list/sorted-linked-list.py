# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ Node o..

    ___ - value
        info _ value
        link _ N..
        
c_ SortedLinkedList o..

    ___ -
        start _ N..

    ___ insert_in_order data
            temp _ Node(data)

            # List empty or node to be inserted before first node 
            __ start == N.. or data < start.info:
                temp.link _ start
                start _ temp
                r_

            p _ start
            _____ p.link __ n.. N.. and p.link.info <_ data:
                p _ p.link
            temp.link _ p.link
            p.link _ temp
          

    ___ create_list
        n _ int(input("Enter the number of nodes : "))
        __ n == 0:
            r_
        
	___ i __ range(n
            data _ int(input("Enter the element to be inserted : "))
            insert_in_order(data)
        
    ___ search x
        __ start __ N..:
            print("List is empty")
            r_
        p _ start
        position _ 1
        _____  p __ n.. N.. and p.info <_ x:
            __  p.info == x:
                break
            position+_1
            p _ p.link

        __ p __ N.. or p.info !_ x:
            print(x," not found in list")
        ____
            print(x , " is at position " , position) 	
          
    ___ display_list
        __ start __ N..:
            print("List is empty")
            r_
        print("List is :   ")
        p _ start
        _____ p __ n.. N..:
            print(p.info , "  ", end_'')
            p _ p.link
        print()
        
#########################################################################
        
list _ SortedLinkedList()
list.create_list() 
		
_____ True:
    print("1.Display list") 
    print("2.Insert")
    print("3.Search for an element")
    print("4.Quit")
        
    option _ int(input("Enter your choice : " ))

    __ option == 1:
        list.display_list()
    elif option == 2:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_in_order(data)
    elif option == 3:
        data _ int(input("Enter the element to be searched : "))
        list.search(data)
    elif option == 4:
        break
    ____
        print("Wrong option") 
    print() 

   
       


# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ Node o..

    ___ - value
        info _ value
        prev _ N..
        next _ N..
        

c_ DoubleLinkedList o..

    ___ -
        start _ N..

    ___ display_list
        __ start __ N..:
            print("List is empty")
            r_

        print("List is : ")
        p _ start
        _____ p __ n.. N..:
            print(p.info, "  ", end_'')
            p _ p.next
        print()
     

    ___ insert_in_beginningdata
        temp _ Node(data)
        temp.next _ start
        start.prev _ temp
        start _ temp

    ___ insert_in_empty_listdata
        temp _ Node(data)
        start _ temp
    
    ___ insert_at_enddata
        temp _ Node(data)
        p _ start
        _____ p.next __ n.. N..:
            p _ p.next
        p.next _ temp
        temp.prev _ p
        

    ___ create_list
        n _ int(input("Enter the number of nodes : "))
        __ n __ 0:
            r_
        data _ int(input("Enter the first element to be inserted : "))
        insert_in_empty_list(data)

        ___ i __ range(n-1
            data _ int(input("Enter the next element to be inserted : "))
            insert_at_end(data)
            
	
    ___ insert_afterdata, x
        temp _ Node(data)
        p _ start
        _____ p __ n.. N..:
            __  p.info __ x:
                break
            p _ p.next

        __ p __ N..:
            print(x," not present in the list")
        ____
            temp.prev _ p
            temp.next _ p.next
            __ p.next __ n.. N..:
                p.next.prev _ temp # should not be done when p refers to last node
            p.next _ temp;
          
    ___ insert_beforedata,x
        __ start __ N..:
            print("List is empty")
            r_

        __ start.info __ x:
            temp _ Node(data)
            temp.next _ start
            start.prev _ temp
            start _ temp
            r_

        p _ start;
        _____ p __ n.. N..:
            __ p.info __ x:
                break
            p _ p.next

        __ p __ N..:
            print(x, " not present in the list")
        ____
            temp _ Node(data)
            temp.prev _ p.prev
            temp.next _ p
            p.prev.next _ temp
            p.prev _ temp
        	    
    ___ delete_first_node
        __ start __ N..:  # list is empty
            r_
        __ start.next __ N..: # list has only one node
            start _ N..
            r_
        start _ start.next
        start.prev _ N..
    
    ___ delete_last_node
        __ start __ N..:   # list is empty
            r_
        __ start.next __ N..:  # list has only one node
            start _ N..
            r_

        p _ start;
        _____ p.next !_ N..:
            p _ p.next;
        p.prev.next _ N..
          

    ___ delete_nodex
        __ start __ N..:   # list is empty
            r_
        __ start.next __ N..:	# list has only one node
            __ start.info __ x:
                start _ N..;
            ____
                print(x," not found")
            r_
			
        # Deletion of first node
        __ start.info __ x:
            start _ start.next
            start.prev _ N..
            r_
        
        p _ start.next
        _____ p.next __ n.. N..:
            __ p.info __ x:
                break
            p _ p.next
            
        
        __ p.next __ n.. N.. : # node to be deleted is in between
            p.prev.next _ p.next
            p.next.prev _ p.prev;
        ____ # p refers to last node
            __ p.info __ x: # node to be deleted is last node
                p.prev.next _ N..
            ____
                print(x," not found")

    ___ reverse_list
        __ start __ N..:
            r_

        p1 _ start
        p2 _ p1.next
        p1.next _ N..
        p1.prev _ p2
        _____ p2 __ n.. N..:
            p2.prev _ p2.next
            p2.next _ p1
            p1 _ p2
            p2 _ p2.prev
        start _ p1
     
#########################################################################
        
list _ DoubleLinkedList()
list.create_list() 
		
_____ True:
    print("1.Display list") 
    print("2.Insert in empty list")
    print("3.Insert a node in the beginning of the list")
    print("4.Insert a node at the end of the list")
    print("5.Insert a node after a specified node")
    print("6.Insert a node before a specified node")
    print("7.Delete first node")
    print("8.Delete last node")
    print("9.Delete any node")
    print("10.Reverse the list")
    print("11.Quit")
        
    option _ int(input("Enter your choice : " ))

    __ option __ 1:
        list.display_list()
    elif option __ 2:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_in_empty_list(data)
    elif option __ 3:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option __ 4:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option __ 5:
        data _ int(input("Enter the element to be inserted : "))
        x _ int(input("Enter the element after which to insert : "))
        list.insert_after(data,x)
    elif option __ 6:
        data _ int(input("Enter the element to be inserted : "))
        x _ int(input("Enter the element before which to insert : "))
        list.insert_before(data,x)
    elif option __ 7:
        list.delete_first_node() 
    elif option __ 8:
        list.delete_last_node() 
    elif option __ 9:
        data _ int(input("Enter the element to be deleted : "))
        list.delete_node(data)             
    elif option __ 10:
        list.reverse_list()
    elif option __ 11:
        break
    ____
        print("Wrong option") 
    print() 

   
       

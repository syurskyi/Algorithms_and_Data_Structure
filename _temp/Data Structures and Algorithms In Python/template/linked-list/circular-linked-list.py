# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ Node o..

    ___ - value
        info _ value
        link _ N..
        

c_ CircularLinkedList o..

    ___ -  
        last _ N..

    ___ display_list 
        __ last == N..:
            print("List is empty\n")
            r_

        p _ last.link

        _____ True:
            print(p.info , " ",end_'')
            p _ p.link
            __  p == last.link:
                break
        print() 
	
    ___ insert_in_beginningdata
        temp _ Node(data)
        temp.link _ last.link
        last.link _ temp
 
    ___ insert_in_empty_listdata
        temp _ Node(data)
        last _ temp
        last.link _ last

    ___ insert_at_enddata
        temp _ Node(data)
        temp.link _ last.link
        last.link _ temp
        last _ temp

    ___ create_list 
        n _ int(input("Enter the number of nodes : "))
        __ n == 0:
            r_
        data _ int(input("Enter the element to be inserted : "))
        insert_in_empty_list(data)
        
        ___ i __ range(n-1
            data _ int(input("Enter the element to be inserted : "))
            insert_at_end(data)
            
    ___ insert_afterdata,x
        p _ last.link

        _____ True:
            __ p.info == x:
                break 
            p _ p.link
            __ p == last.link:
                break
            
        __ p == last.link and p.info !_ x:
            print(x , " not present in the list")
        ____
            temp _ Node(data)
            temp.link _ p.link
            p.link _ temp
            __ p == last:
                last _ temp

    ___ delete_first_node 
        __ last __ N..: # List is empty
            r_
        __ last.link == last: # List has only one node
            last _ N..
            r_
        last.link _ last.link.link
      

    ___ delete_last_node 
        __ last __ N..: # List is empty
            r_
        __ last.link == last: # List has only one node
            last _ N..
            r_
          
        p _ last.link
        _____ p.link !_ last:
            p _ p.link
        p.link _ last.link
        last _ p

    ___ delete_node x
         
        __ last __ N..: # List is empty
                r_
        __ last.link == last and last.info == x:  # Deletion of only node
            last _ N..
            r_
        
        __ last.link.info == x:  # Deletion of first node
            last.link _ last.link.link
            r_
                    
        p _ last.link
        _____ p.link !_ last.link:
            __  p.link.info == x :
                break 
            p _ p.link
 
        __ p.link == last.link:
            print(x , " not found in the list")
        ____
            p.link _ p.link.link
            __ last.info == x:
                last _ p

                
##############################################################
                
list _ CircularLinkedList()
list.create_list() 
		
_____ True:
    print("1.Display list") 
    print("2.Insert in empty list")
    print("3.Insert a node in the beginning of the list")
    print("4.Insert a node at the end of the list")
    print("5.Insert a node after a specified node")
    print("6.Delete first node")
    print("7.Delete last node")
    print("8.Delete any node")
    print("9.Quit")
        
    option _ int(input("Enter your choice : " ))

    __ option == 1:
        list.display_list()
    elif option == 2:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_in_empty_list(data)
    elif option == 3:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 4:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 5:
        data _ int(input("Enter the element to be inserted : "))
        x _ int(input("Enter the element after which to insert : "))
        list.insert_after(data,x)
    elif option == 6:
        list.delete_first_node() 
    elif option == 7:
        list.delete_last_node() 
    elif option == 8:
        data _ int(input("Enter the element to be deleted : "))
        list.delete_node(data)             
    elif option == 9:
        break
    ____
        print("Wrong option") 
    print() 

   
       

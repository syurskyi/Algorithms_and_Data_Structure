# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ Node o..

    ___ - value
        info _ value
        link _ N..

c_ HeaderLinkedList o..

    ___ -
        head _ Node(0)

    ___ display_list
        __ head.link __ N..:
            print("List is empty")
            r_

        p _ head.link
        print("List is : ")
        _____ p __ n.. N..:
            print(p.info, " ", end_'')
            p _ p.link
        print() 
	     
       

    ___ create_list
        n _ int(input("Enter the number of nodes : "))
        ___ i __ range(n
            data _ int(input("Enter the element to be inserted : "))
            insert_at_end(data)


    ___ insert_at_enddata
            
        temp _ Node(data)

        p _ head
        _____ p.link __ n.. N..:
            p _ p.link

        p.link _ temp
        temp.link _ N..
        
    ___ insert_before data, x
        # Find pointer to predecessor of node containing x
        p _ head
        _____  p.link __ n.. N..:
            __ p.link.info __ x:
                break
            p _ p.link
            
        __ p.link __ N..:
            print(x , " not present in the list")
        ____
            temp _ Node(data)
            temp.link _ p.link
            p.link _ temp
 
    ___ insert_at_positiondata,k
        p _ head
        i _ 1
        _____ i <_ k-1 and p __ n.. N..:
            p _ p.link
            i+_1
            
        __ p __ N..:
            print("You can insert only upto " , (i-1) , "th position ")
        ____
            temp _ Node(data)
            temp.link _ p.link
            p.link _ temp
    
    ___ delete_nodedata
        p _ head
        _____ p.link __ n.. N..:
            __ p.link.info __ data:
                break
            p _ p.link
        
        __ p.link __ N..:
            print(data + "Element %d not found")
        ____
            p.link _ p.link.link
         
    ___ reverse_list
        prev _ N..
        p _ head.link
        _____ p __ n.. N..:
            next _ p.link
            p.link _ prev
            prev _ p
            p _ next

        head.link _ prev
            
list _ HeaderLinkedList()

list.create_list() 
		
_____ True:
    print("1.Display list") 
    print("2.Insert a node at the end of the list")
    print("3.Insert a node before a specified node")
    print("4.Insert a node at a given position")
    print("5.Delete a node")
    print("6.Reverse the list")
    print("7.Quit")
        
    option _ int(input("Enter your choice : " ))

    __ option __ 1:
        list.display_list()
    elif option __ 2:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option __ 3:
        data _ int(input("Enter the element to be inserted : "))
        x _ int(input("Enter the element before which to insert : "))
        list.insert_before(data,x)
    elif option __ 4:
        data _ int(input("Enter the element to be inserted : "))
        k _ int(input("Enter the position at which to insert : "))
        list.insert_at_position(data,k)
    elif option __ 5:
        data _ int(input("Enter the element to be deleted : "))
        list.delete_node(data)             
    elif option __ 6:
        list.reverse_list()
    elif option __ 7:
        break
    ____
        print("Wrong option") 
    print() 

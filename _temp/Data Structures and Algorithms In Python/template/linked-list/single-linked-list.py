# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ Node:

    ___ - value
        info _ value
        link _ N..
        
c_ SingleLinkedList:

    ___ -
        start _ N..
     
    ___ display_list
        __ start __ N..:
            print("List is empty")
            r_
        ____
            print("List is :   ")
            p _ start
            _____ p __ n.. N..:
                print(p.info , " ", end_'')
                p _ p.link
            print()

    ___ count_nodes
        p _ start
        n _ 0
        _____ p __ n.. N..:
            n+_1
            p _ p.link
        print("Number of nodes in the list = " ,n)
    
    ___ searchx
        position _ 1
        p _ start
        _____ p __ n.. N..:
            __ p.info == x:
                print(x , " is at position ", position)
                r_ True
            position+_1
            p _ p.link
        ____
            print(x," not found in list")
            r_ False

    ___ insert_in_beginning data
        temp _ Node(data)
        temp.link _ start
        start _ temp
   
    ___ insert_at_end data
        temp _ Node(data)
        __ start __ N..:
            start _ temp
            r_
        
        p _ start
        _____ p.link __ n.. N..:
            p _ p.link
        p.link _ temp

    ___ create_list
        n _ int(input("Enter the number of nodes : "))
        __ n == 0:
            r_
        ___ i __ range(n
            data _ int(input("Enter the element to be inserted : "))
            insert_at_end(data)
           
    ___ insert_afterdata,x
        pass    
           
    ___ insert_before data, x
        pass
     
    ___ insert_at_position data, k
        pass
    
    ___ delete_nodex
        pass   
                 
    ___ delete_first_node
        pass

    ___ delete_last_node
        pass
    
    ___ reverse_list
        pass   

    ___ bubble_sort_exdata
        pass
    
    ___ bubble_sort_exlinks
        pass
           
    ___ has_cycle
        pass

    ___ find_cycle
        pass

    ___ remove_cycle
        pass   

    ___ insert_cyclex
        pass
    
    ___ merge2list2
        pass
    
    ___ _merge2 p1, p2
        pass

    ___ merge_sort
        pass    

    ___ _merge_sort_reclistStart
        pass

    ___ _divide_list p
        pass
        

#######################################################################################
            
list _ SingleLinkedList()

list.create_list() 
		
_____ True:
    print("1.Display list") 
    print("2.Count the number of nodes") 
    print("3.Search for an element")
    print("4.Insert in empty list/Insert in beginning of the list")
    print("5.Insert a node at the end of the list")
    print("6.Insert a node after a specified node")
    print("7.Insert a node before a specified node")
    print("8.Insert a node at a given position")
    print("9.Delete first node")
    print("10.Delete last node")
    print("11.Delete any node")
    print("12.Reverse the list")
    print("13.Bubble sort by exchanging data")
    print("14.Bubble sort by exchanging links")
    print("15.MergeSort")
    print("16.Insert Cycle")
    print("17.Detect Cycle")
    print("18.Remove cycle")
    print("19.Quit")
        
    option _ int(input("Enter your choice : " ))

    __ option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data _ int(input("Enter the element to be searched : "))
        list.search(data)
    elif option == 4:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 5:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 6:
        data _ int(input("Enter the element to be inserted : "))
        x _ int(input("Enter the element after which to insert : "))
        list.insert_after(data,x)
    elif option == 7:
        data _ int(input("Enter the element to be inserted : "))
        x _ int(input("Enter the element before which to insert : "))
        list.insert_before(data,x)
    elif option == 8:
        data _ int(input("Enter the element to be inserted : "))
        k _ int(input("Enter the position at which to insert : "))
        list.insert_at_position(data,k)
    elif option == 9:
        list.delete_first_node() 
    elif option == 10:
        list.delete_last_node() 
    elif option == 11:
        data _ int(input("Enter the element to be deleted : "))
        list.delete_node(data)             
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_exdata() 
    elif option == 14:
        list.bubble_sort_exlinks() 
    elif option == 15:
        list.merge_sort() 
    elif option == 16:
        data _ int(input("Enter the element at which the cycle has to be inserted : "))
        list.insert_cycle(data) 
    elif option == 17:
        __ list.has_cycle(
            print("List has a cycle")
        ____
            print("List does not have a cycle") 
    elif option == 18:
        list.remove_cycle() 
    elif option == 19:
        break
    ____
        print("Wrong option") 
    print() 

   

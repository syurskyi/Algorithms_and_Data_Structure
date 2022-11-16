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
            __ p.info __ x:
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
        __ n __ 0:
            r_
        ___ i __ range(n
            data _ int(input("Enter the element to be inserted : "))
            insert_at_end(data)
           
    ___ insert_afterdata,x
        p _ start
        _____ p __ n.. N..:
            __ p.info __ x:
                break
            p _ p.link

        __ p __ N..:
            print(x, "not present in the list")
        ____
            temp _ Node(data)
            temp.link _ p.link
            p.link _ temp
            
     
            
    ___ insert_before data, x
        # If list is empty
        __ start __ N..:
            print("List is empty") 
            r_
    
        # x is in first node,new node is to be inserted before first node
        __ x __ start.info:
            temp _ Node(data)
            temp.link _ start
            start _ temp
            r_
        
        # Find reference to predecessor of node containing x
        p _ start
        _____ p.link __ n.. N..:
            __ p.link.info __ x:
                break 	
            p _ p.link


        __ p.link __ N..:
             print(x , " not present in the list") 
        ____
            temp _ Node(data)
            temp.link _ p.link
            p.link _ temp
    
     

    ___ insert_at_position data, k
        __ k __ 1:
            temp _ Node(data)
            temp.link _ start
            start _ temp
            r_
                    
        p _ start
        i _ 1
        _____ i<k-1 and p __ n.. N..: # find a reference to k-1 node
            p _ p.link
            i+_1

        __ p __ N..:
            print("You can insert only upto position",i) 
        ____
            temp _ Node(data)
            temp.link _ p.link
            p.link _ temp

    ___ delete_nodex
      
            __ start __ N..:
                print("List is empty") 
                r_

            # Deletion of first node
            __ start.info __ x:
                start _ start.link
                r_

            # Deletion in between or at the end
            p _ start
            _____ p.link __ n.. N..:
                __ p.link.info __ x:
                    break 	
                p _ p.link

            __ p.link __ N..:
                print("Element ", x ,"not in list") 
            ____
                p.link _ p.link.link
       
                 
    ___ delete_first_node
      
        __ start __ N..:
            r_
        start _ start.link
       

    ___ delete_last_node
      
        __ start __ N..:
            r_

        __ start.link __ N..:
            start _ N..
            r_
           
        p _ start
        _____ p.link.link __ n.. N..:
            p _ p.link
        p.link _ N..

    ___ reverse_list
      
        prev _ N..
        p _ start
        _____ p __ n.. N..:
            next _ p.link
            p.link _ prev
            prev _ p
            p _ next
           
        start _ prev
           


    ___ bubble_sort_exdata
        end_None

        _____ end !_ start.link:

            p _ start
            _____  p.link !_ end:
                q _ p.link
                __ p.info > q.info:
                    p.info,q.info _ q.info,p.info
                p _ p.link
            end _ p

    
    ___ bubble_sort_exlinks
        end _ N..
        _____ end !_ start.link:
            r _ p _ start
            _____ p.link !_ end:
                q _ p.link
                __ p.info > q.info :
                    p.link _ q.link
                    q.link _ p
                    __ p!_self.start:
                        r.link _ q
                    ____
                        start _ q
                    p,q _ q,p
                r _ p
                p _ p.link
            end _ p
   
           
    ___ has_cycle
      
        __ find_cycle() __ N..:
            r_ False
        ____
            r_ True
       

    ___ find_cycle

        __ start __ N.. or start.link __ N..:
            r_ N..

        slowR _ start
        fastR _ start

        _____ fastR __ n.. N.. and fastR.link __ n.. N..:
            slowR _ slowR.link
            fastR _ fastR.link.link
            __ slowR __ fastR:
                r_ slowR
        r_ N..


    ___ remove_cycle
          
        c _ find_cycle()
        __ c __ N..:
            r_
        print("Node at which the cycle was detected is " , c.info) 
        
        p _ c
        q _ c
        lenCycle _ 0

        _____ True:
            lenCycle+_1
            q _ q.link
            __ p __ q:
                break;

        print("Length of cycle is :", lenCycle) 

        lenRemList _ 0
        p _ start
        _____ p !_ q:
            lenRemList+_1
            p _ p.link
            q _ q.link
        
        print("Number of nodes not included in the cycle are : ", lenRemList) 

        length_list _ lenCycle + lenRemList
        print("Length of the list is : " , length_list) 

        p _ start
        ___ i __ range(length_list-1
                p _ p.link
        p.link _ N..
           

    ___ insert_cyclex
        __ start __ N..:
            r_
        p _ start
        px _ N..
        prev _ N..

        _____ p __ n.. N..:
            __ p.info __ x:
                px _ p
            prev _ p
            p _ p.link
                           
        __ px __ n.. N..:
            prev.link _ px
        ____
            print(x , " not present in list")

    
    ___ merge2list2
        merge_list _ SingleLinkedList()
        merge_list.start _ _merge2(start, list2.start)
        r_ merge_list
        
    ___ _merge2 p1, p2

        __ p1.info <_ p2.info:
            startM _ p1
            p1 _ p1.link
        ____
            startM _ p2
            p2 _ p2.link
            
        pM _ startM

        _____ p1 __ n.. N.. and p2 __ n.. N..:
            __ p1.info <_ p2.info :
                pM.link _ p1
                pM _ pM.link
                p1 _ p1.link
            ____
                pM.link _ p2
                pM _ pM.link
                p2 _ p2.link
            
        __ p1 __ N..:
            pM.link _ p2
        ____
            pM.link _ p1

        r_ startM
        


    ___ merge_sort
        start _ _merge_sort_rec(start)
        

    ___ _merge_sort_reclist_start

        #if list empty or has one element
        __ list_start __ N.. or list_start.link __ N..:
                r_ list_start

        #if more than one element
        start1 _ list_start
        start2 _ _divide_list(list_start)
        start1 _ _merge_sort_rec(start1)
        start2 _ _merge_sort_rec(start2)
        startM _ _merge2(start1, start2)
        r_ startM
        

    ___ _divide_list p
        q _ p.link.link
        _____ q __ n.. N.. and q.link __ n.. N..:
            p _ p.link
            q _ q.link.link
        start2 _ p.link
        p.link _ N..
        r_ start2
        
        

########################################################################################
            
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

    __ option __ 1:
        list.display_list()
    elif option __ 2:
        list.count_nodes()
    elif option __ 3:
        data _ int(input("Enter the element to be searched : "))
        list.search(data)
    elif option __ 4:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option __ 5:
        data _ int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option __ 6:
        data _ int(input("Enter the element to be inserted : "))
        x _ int(input("Enter the element after which to insert : "))
        list.insert_after(data,x)
    elif option __ 7:
        data _ int(input("Enter the element to be inserted : "))
        x _ int(input("Enter the element before which to insert : "))
        list.insert_before(data,x)
    elif option __ 8:
        data _ int(input("Enter the element to be inserted : "))
        k _ int(input("Enter the position at which to insert : "))
        list.insert_at_position(data,k)
    elif option __ 9:
        list.delete_first_node() 
    elif option __ 10:
        list.delete_last_node() 
    elif option __ 11:
        data _ int(input("Enter the element to be deleted : "))
        list.delete_node(data)             
    elif option __ 12:
        list.reverse_list()
    elif option __ 13:
        list.bubble_sort_exdata() 
    elif option __ 14:
        list.bubble_sort_exlinks() 
    elif option __ 15:
        list.merge_sort() 
    elif option __ 16:
        data _ int(input("Enter the element at which the cycle has to be inserted : "))
        list.insert_cycle(data) 
    elif option __ 17:
        __ list.has_cycle(
            print("List has a cycle")
        ____
            print("List does not have a cycle") 
    elif option __ 18:
        list.remove_cycle() 
    elif option __ 19:
        break
    ____
        print("Wrong option") 
    print() 

   

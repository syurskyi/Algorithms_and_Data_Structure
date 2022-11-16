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
        ___ i __ r..(n
            data _ int(input("Enter the element to be inserted : "))
            insert_at_end(data)
    

    ___ bubble_sort_exdata 
        end _ N..
        _____ end !_ start.link:

            p _ start
            _____  p.link !_ end:
                q _ p.link
                __ p.info > q.info:
                    p.info,q.info _ q.info,p.info
                p _ p.link
            end _ p

    ___ merge1 list2
        merge_list _ SingleLinkedList()
        merge_list.start _ _merge1(start, list2.start)
        r_ merge_list
    
    ___ _merge1 p1, p2
        __ p1.info <_ p2.info:
            startM _ Node(p1.info)
            p1 _ p1.link
        ____
            startM _ Node(p2.info)
            p2 _ p2.link;
        
        pM _ startM

        _____ p1 __ n.. N.. ___ p2 __ n.. N..:
            __ p1.info <_ p2.info :
                pM.link _ Node(p1.info)
                p1 _ p1.link
            ____
                pM.link _ Node(p2.info);
                p2 _ p2.link;
            pM _ pM.link;
            

        #If second list has finished and elements left in first list
        _____ p1 __ n.. N..:
            pM.link _ Node(p1.info)
            p1 _ p1.link
            pM _ pM.link
        
        #If first list has finished and elements left in second list
        _____ p2 __ n.. N..:
            pM.link _ Node(p2.info)
            p2 _ p2.link
            pM _ pM.link

        r_ startM

        
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

        _____ p1 __ n.. N.. ___ p2 __ n.. N..:
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
        

#########################################################################################

list1 _ SingleLinkedList()
list2 _ SingleLinkedList()

list1.create_list() 
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()
	
print("First List - "); list1.display_list()
print("Second List - "); list2.display_list()

list3 _ list1.merge1(list2)
print("Merged List - "); list3.display_list()
		
print("First List - "); list1.display_list()
print("Second List - "); list2.display_list()
		
list3 _ list1.merge2(list2)
print("Merged List - "); list3.display_list()
print("First List - ");  list1.display_list()
print("Second List - "); list2.display_list()


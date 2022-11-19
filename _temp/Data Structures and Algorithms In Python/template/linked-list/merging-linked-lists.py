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
                print(?.i.. , " ", end_'')
                p _ ?.l..
            print()
   
    ___ insert_at_end data
        temp _ ? ?
        __ start __ N..:
            start _ temp
            r_
        
        p _ start
        _____ ?.l.. __ n.. N..:
            p _ ?.l..
        ?.l.. _ temp


    ___ create_list 
        n _ i..(i..("Enter the number of nodes : "))
        __ n __ 0:
            r_
        ___ i __ r..(n
            data _ i..(i..("Enter the element to be inserted : "))
            insert_at_end(data)
    

    ___ bubble_sort_exdata 
        end _ N..
        _____ end !_ start.l..:

            p _ start
            _____  ?.l.. !_ end:
                q _ ?.l..
                __ ?.i.. > q.i..:
                    ?.i..,q.i.. _ q.i..,?.i..
                p _ ?.l..
            end _ p

    ___ merge1 list2
        merge_list _ SingleLinkedList()
        merge_list.start _ _merge1(start, list2.start)
        r_ merge_list
    
    ___ _merge1 p1, p2
        __ p1.i.. <_ p2.i..:
            startM _ Node(p1.i..)
            p1 _ p1.l..
        ____
            startM _ Node(p2.i..)
            p2 _ p2.l..;
        
        pM _ startM

        _____ p1 __ n.. N.. ___ p2 __ n.. N..:
            __ p1.i.. <_ p2.i.. :
                pM.l.. _ Node(p1.i..)
                p1 _ p1.l..
            ____
                pM.l.. _ Node(p2.i..);
                p2 _ p2.l..;
            pM _ pM.l..;
            

        #If second list has finished and elements left in first list
        _____ p1 __ n.. N..:
            pM.l.. _ Node(p1.i..)
            p1 _ p1.l..
            pM _ pM.l..
        
        #If first list has finished and elements left in second list
        _____ p2 __ n.. N..:
            pM.l.. _ Node(p2.i..)
            p2 _ p2.l..
            pM _ pM.l..

        r_ startM

        
    ___ merge2list2
        merge_list _ SingleLinkedList()
        merge_list.start _ _merge2(start, list2.start)
        r_ merge_list
        
    ___ _merge2 p1, p2

        __ p1.i.. <_ p2.i..:
            startM _ p1
            p1 _ p1.l..
        ____
            startM _ p2
            p2 _ p2.l..
            
        pM _ startM

        _____ p1 __ n.. N.. ___ p2 __ n.. N..:
            __ p1.i.. <_ p2.i.. :
                pM.l.. _ p1
                pM _ pM.l..
                p1 _ p1.l..
            ____
                pM.l.. _ p2
                pM _ pM.l..
                p2 _ p2.l..
            
        __ p1 __ N..:
            pM.l.. _ p2
        ____
            pM.l.. _ p1

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


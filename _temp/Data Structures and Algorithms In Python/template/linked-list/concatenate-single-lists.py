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
        __ n == 0:
            r_
        ___ i __ range(n
            data _ int(input("Enter the element to be inserted : "))
            insert_at_end(data)

    ___ concatenate list2
        __ start __ N..:
            start _ list2.start
            r_
            
        __ list2.start __ N..:
            r_

        p _ start
        _____ p.link __ n.. N..:
            p _ p.link

        p.link _ list2.start
              
#########################################################################################
            
list1 _ SingleLinkedList()
list2 _ SingleLinkedList()
		
print("Enter first list :- ")
list1.create_list()
print("Enter second list :- ")
list2.create_list()

print("First "); list1.display_list()
print("Second "); list2.display_list()

list1.concatenate(list2)
print("First "); list1.display_list()


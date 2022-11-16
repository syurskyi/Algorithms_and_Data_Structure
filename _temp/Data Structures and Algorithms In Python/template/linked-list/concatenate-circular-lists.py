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
        
        # for(i = 2  i <= n  i++)
        ___ i __ range(n-1
            data _ int(input("Enter the element to be inserted : "))
            insert_at_end(data)
            
    ___ concatenatelist2
        __ last __ N..:
            last _ list.last;
            r_

        __ list2.last __ N..:
            r_

        p _ last.link;
        last.link _ list2.last.link;
        list2.last.link _ p;
        last _ list2.last;
        
 
###############################################################
list1 _ CircularLinkedList()
list2 _ CircularLinkedList()

print("Enter first list :- ")
list1.create_list()

print("Enter second list :- ")
list2.create_list()

print("First ");   list1.display_list()
print("Second ");  list2.display_list()

list1.concatenate(list2)
print("First ")
list1.display_list()


                

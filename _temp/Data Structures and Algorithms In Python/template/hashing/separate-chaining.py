# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

##################################################################

c_ studentRecord:
    ___ - i,name
        studentId _ i
        studentName _ name

    ___ get_student_id 
        r_ studentId

    ___ set_student_idi
        studentId _ i
        
    ___ __str__ 
        r_ str(studentId) + " "  + studentName 

##################################################################
    
c_ Node:
    ___ - value
        info _ value 
        link _ N.. 
        
##################################################################

c_ SingleLinkedList:
    ___ -  
        start _ N..

    ___ display_list 
        __ start __ N..:
            print("___")
            r_
        p _ start 
        _____ p __ n.. N..:
            print(p.info , " ", end_'')
            p _ p.link 
        print()
    
    ___ searchx
        p _ start
        _____ p __ n.. N..:
            __ p.info.get_student_id() == x:
                r_ p.info
            p _ p.link
        ____
            r_ N..

    ___ insert_in_beginning data
        temp _ Node(data)
        temp.link _ start
        start _ temp
    
    ___ delete_nodex
        __ start __ N..:
            print("List is empty") 
            r_ 

        # Deletion of first node
        __ start.info.get_student_id() == x:
            start _ start.link   
            r_ 

        # Deletion in between or at the end
        p _ start 
        _____ p.link __ n.. N..:
            __ p.link.info.get_student_id() == x:
                break 	
            p _ p.link 

        __ p.link __ N..:
            print("Element ", x ,"not in list") 
        ____
            p.link _ p.link.link
            
##################################################################
   

c_ HashTable:

    ___ - tableSize
        m _ tableSize   
        array _ [N..] * m
        n _ 0  

    ___ hash key
        r_ (key % m)

    ___ display_table 
        ___ i __ range(m
            print( "[" , i , "]  -->  ", end _'' )
            __ array[i]!_ N..:
                array[i].display_list()
            ____
               print("___")
        
    
    ___ search key
        h _ hash(key)
        __ array[h] !_ N..:
            r_ array[h].search(key)
        r_ N..        
               
    ___ insert newRecord
        key _ newRecord.get_student_id()
        h _ hash(key)

        __ array[h] == N..:
            array[h] _ SingleLinkedList()
        array[h].insert_in_beginning(newRecord)
        n+_1
    
   
   
    ___ delete key
        h _ hash(key)
        __ array[h] !_ N..:
            array[h].delete_node(key)
            n-_1
        ____
            print("Value " , key , " not present")

    
                
##################################################################
               
size _ int(input("Enter size of table : "))
table _ HashTable(size)

_____ True:
    print("1.Insert a record")
    print("2.Search a record")
    print("3.Delete a record")
    print("4.Display table")
    print("5.Exit")

    choice _ int(input("Enter your choice : "))
    __ choice == 1:
        id _ int(input("Enter student id : "))
        name _ input("Enter student name : ")
        aRecord _ studentRecord(id,name)
        table.insert(aRecord)
    elif choice == 2:
        id _ int(input("Enter a key to be searched : "))
        aRecord _ table.search(id)
        __  aRecord __ N..:
            print("Key not found")
        ____
            print(aRecord)
    elif choice == 3:
          id _ int(input("Enter a key to be deleted :"))
          table.delete(id)
    elif choice == 4:
          table.display_table()
    elif choice == 5:
          break
    ____
          print("Wrong option") 
    print() 

        

                        

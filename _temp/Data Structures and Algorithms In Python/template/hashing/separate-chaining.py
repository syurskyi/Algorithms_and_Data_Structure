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
        
    ___ -s 
        r_ s..(studentId) + " "  + studentName 

##################################################################
    
c_ Node
    ___ - value
        info _ value 
        link _ N.. 
        
##################################################################

c_ SingleLinkedList:
    ___ -  
        start _ N..

    ___ display_list 
        __ start __ N..
            print("___")
            r_
        p _ start 
        _____ p __ n.. N..
            print(?.i.. , " ", e.._'')
            p _ ?.l.. 
        print()
    
    ___ searchx
        p _ start
        _____ p __ n.. N..
            __ ?.i...get_student_id() __ x:
                r_ ?.i..
            p _ ?.l..
        ____
            r_ N..

    ___ insert_in_beginning data
        temp _ ? ?
        ?.l.. _ start
        start _ temp
    
    ___ delete_nodex
        __ start __ N..
            print("List is empty") 
            r_ 

        # Deletion of first node
        __ start.i...get_student_id() __ x:
            start _ start.l..   
            r_ 

        # Deletion in between or at the end
        p _ start 
        _____ ?.l.. __ n.. N..
            __ ?.l...info.get_student_id() __ x:
                b.. 	
            p _ ?.l.. 

        __ ?.l.. __ N..
            print("Element ", x ,"not in list") 
        ____
            ?.l.. _ ?.l...link
            
##################################################################
   

c_ HashTable:

    ___ - tableSize
        m _ tableSize   
        array _ [N..] * m
        n _ 0  

    ___ hash key
        r_ (key % m)

    ___ display_table 
        ___ i __ r..(m
            print( "[" , i , "]  -->  ", end _'' )
            __ array[i]!_ N..
                array[i].display_list()
            ____
               print("___")
        
    
    ___ search key
        h _ hash(key)
        __ array[h] !_ N..
            r_ array[h].search(key)
        r_ N..        
               
    ___ i..  newRecord
        key _ newRecord.get_student_id()
        h _ hash(key)

        __ array[h] __ N..
            array[h] _ SingleLinkedList()
        array[h].insert_in_beginning(newRecord)
        n+_1
    
   
   
    ___ delete key
        h _ hash(key)
        __ array[h] !_ N..
            array[h].delete_node(key)
            n-_1
        ____
            print("Value " , key , " not present")

    
                
##################################################################
               
size _ i..(i..("Enter size of table : "))
table _ HashTable(size)

_____ T..:
    print("1.Insert a record")
    print("2.Search a record")
    print("3.Delete a record")
    print("4.Display table")
    print("5.Exit")

    choice _ i..(i..("Enter your choice : "))
    __ choice __ 1:
        id _ i..(i..("Enter student id : "))
        name _ i..("Enter student name : ")
        aRecord _ studentRecord(id,name)
        table.i.. (aRecord)
    ____ choice __ 2:
        id _ i..(i..("Enter a key to be searched : "))
        aRecord _ table.search(id)
        __  aRecord __ N..
            print("Key not found")
        ____
            print(aRecord)
    ____ choice __ 3:
          id _ i..(i..("Enter a key to be deleted :"))
          table.delete(id)
    ____ choice __ 4:
          table.display_table()
    ____ choice __ 5:
          b..
    ____
          print("Wrong option") 
    print() 

        

                        

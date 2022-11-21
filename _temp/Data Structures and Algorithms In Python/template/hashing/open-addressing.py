# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ InvalidOperationException E..
    p..

c_ studentRecord:
    ___ - i,Name
        studentId _ i
        studentName _ Name

    ___ get_student_id 
        r_ studentId

    ___ set_student_idi
        studentId _ i
        
    ___ -s 
        r_ s..(studentId) + " "  + studentName
        

c_ HashTable:

    ___ - tableSize_11
        m _ tableSize
        array _ [N..] * m
        n _ 0

    ___ hash1 key
        r_ (key % m)
    
    ___ i..  newRecord
        key _ newRecord.get_student_id()
        h _ hash1(key)

        location _ h

        ___ i __ r..(1,m
            __ array[location] __ N.. __ array[location].get_student_id() __ -1:
                array[location] _ newRecord
                n+_1
                r_
            
            __ array[location].get_student_id() __ key:
                r... InvalidOperationException("Duplicate key")

            location _ (h + i) % m
        
        print("Table is full : Record can't be inserted ")
    

    ___ searchkey
        h _ hash1(key)
        location _ h

        ___ i __ r..(1,m
            __ array[location] __ N.. :
                r_ N..
            __ array[location].get_student_id() __ key:
                r_ array[location]
            location _ (h + i) % m
        r_ N..
    

    ___ display_table 
    
        ___ i __ r..(m
            print("[",end_''); print(i,end_''); print("]",end_'');

            __ array[i] __ n.. N.. ___ array[i].get_student_id() !_ -1:
                print(array[i])
            ____
                print("___")
  
    ___ deletekey
        h _ hash1(key)
        location _ h

        ___ i __ r..(1,m
            __ array[location] __ N..
                r_ N..
            
            __ array[location].get_student_id() __ key:
                temp _ array[location]
                array[location].set_student_id(-1)
                n-_1
                r_ temp
            
            location _ (h + i) % m
        
        r_ N..

##################################################################################

   
size _ i..(i..("Enter initial size of table : "))
table _ HashTable(size)

_____ T..:
    print("1.Insert a record")
    print("2.Search a record")
    print("3.Delete a record")
    print("4.Display table")
    print("5.Exit")
    option _ i..(i..("Enter your option :  "))

    __ option __ 1:
        id _ i..(i..("Enter student id : "))
        name _ i..("Enter student name : ")
        aRecord _ studentRecord(id,name)
        table.i.. (aRecord)
    ____ option __ 2:
        id _ i..(i..("Enter a key to be searched : "))
        aRecord _ table.search(id)
        __  aRecord __ N..
            print("Key not found")
        ____
            print(aRecord)
    ____ option __ 3:
        id _ i..(i..("Enter a key to be deleted :"))
        table.delete(id)
    ____ option __ 4:
        table.display_table()
    ____ option __ 5:
        b..
    ____
        print("Wrong option") 
    print() 

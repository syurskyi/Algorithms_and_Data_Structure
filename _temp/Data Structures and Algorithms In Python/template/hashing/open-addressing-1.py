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

    ___ rehash new_size
        temp _ HashTable(new_size)

        ___ i __ r..(m
            __ array[i] !_ N.. ___ array[i].get_student_id() !_ -1:
                ?.i.. (array[i])
        array _ ?.array
        m _ new_size

    ___ insert1 newRecord
        __ n >_ m//2:
            rehash( next_prime(2*m) )
            print("New Table Size is : " , m )
        i.. (newRecord)

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

            
    ___ next_primex
        _____ is_prime(x) __ n.. T..:
            x_x+1
        r_ x
      
    ___ is_prime x
        ___ i __ r..(2,x
            __ x % i __ 0:
                r_ F..
        r_ T..
    
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
            print("[",e.._''); print(i,e.._''); print("]",e.._''); 

            __ array[i] __ n.. N.. ___ array[i].get_student_id() !_ -1:
                print(array[i])
            ____
                print("___")
  
    ___ deletekey
        h _ hash1(key)
        location _ h

        ___ i __ r..(1,m
            __ array[location] __ N..
                r_
            
            __ array[location].get_student_id() __ key:
                array[location].set_student_id(-1)
                n-_1
                __ n > 0 ___ n <_ m/8:
                    rehash(next_prime(m//2))
                    print( "New Table Size is : " ,m )

            location _ (h + i) % m
        
        
#################################################################################

   
size _ i..(i..("Enter initial size of table : "))
table _ HashTable(size)

_____ T..:
    print("1.Insert a record")
    print("2.search a record")
    print("3.delete a record")
    print("4.Display table")
    print("5.Exit")
    option _ i..(i..("Enter your option :  "))

    __ option __ 1:
        id _ i..(i..("Enter student id : "))
        name _ i..("Enter student name : ")
        aRecord _ studentRecord(id,name)
        table.insert1(aRecord)
    ____ option __ 2:
        idd _ i..(i..("Enter a key to be searched : "))
        aRecord _ table.search(id)
        __ aRecord __ N..
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

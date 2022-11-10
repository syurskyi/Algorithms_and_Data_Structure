c_ Node
    ___  -  value)
        ? _ ?
        n.. _ N..
        p.. _ N..
        

c_ DoublyLinkedList
    ___  -  value)
        n.. _ ? ?
        h.. _ ?
        t.. _ ?
        l.. _ 1

    ___ print_list
        t.. _ h..
        w__ ? __ n.. N..
            print ?.v..
            ? _ ?.n..
        
    ___ append  value)
        n.. _ ? ?
        __ ? __ N..
            h.. _ ?
            t.. _ ?
        ____
            t__.n.. _ ?
            ?.p.. _ t..
            t.. _ ?
        ? =_ 1
        r_ T..

    ___ pop
        __ ? __ 0
            r_ N..
        t.. _ t..
        __ ? __ 1
            h.. _ N..
            t.. _ N.. 
        ____       
            t.. _ t__.p..
            ?.n.. _ N.
            ?.p.. _ N..
        ? -_ 1
        r_ ?

    ___ prepend  value)
        n.. _ ? ?
        __ ? __ 0
            h.. _ ?
            t.. _ ?
        ____
            new_node.next = head
            head.prev = new_node
            h.. _ ?
        ? =_ 1
        r_ T..

    ___ pop_first
        __ ? __ 0
            r_ N..
        t.. _ h..
        __ ? __ 1
            h.. _ N..
            t.. _ N..
        ____
            head = head.next
            head.p.. _ N..
            temp.n.. _ N..      
        ? -_ 1
        r_ ?

    ___ get  index)
        __ index < 0 or index >= length
            r_ N..
        t.. _ h..
        __ index < length/2
            for _ in range(index)
                ? _ ?.n..
        ____
            t.. _ t..
            for _ in range(length - 1, index, -1)
                temp = temp.prev  
        r_ ?
        
    ___ set_value  index, value)
        temp = get(index)
        __ temp
            temp.? _ ?
            r_ T..
        r_ False
    
    ___ insert  index, value)
        __ index < 0 or index > length
            r_ False
        __ index == 0
            r_ prepend(value)
        __ index == length
            r_ append(value)

        n.. _ ? ?
        before = get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        ? =_ 1   
        r_ T..  

  


my_doubly_linked_list = ? 1)
?.append(3)


print('DLL before insert():')
?.print_list()


?.insert(1,2)

print('\nDLL after insert(2) in middle:')
?.print_list()


?.insert(0,0)

print('\nDLL after insert(0) at beginning:')
?.print_list()


?.insert(4,4)

print('\nDLL after insert(4) at end:')
?.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before insert():
    1
    3

    DLL after insert(2) in middle:
    1
    2
    3

    DLL after insert(0) at beginning:
    0
    1
    2
    3

    DLL after insert(4) at end:
    0
    1
    2
    3
    4

"""
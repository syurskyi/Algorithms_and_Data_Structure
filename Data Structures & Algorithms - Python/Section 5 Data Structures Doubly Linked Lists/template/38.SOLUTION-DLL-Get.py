
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




my_doubly_linked_list = ? 0)
?.append(1)
?.append(2)
?.append(3)

print('Get node from first half of DLL:')
print(?.get(1).value)

print('\nGet node from second half of DLL:')
print(?.get(2).value)


"""
    EXPECTED OUTPUT:
    ----------------
    Get node from first half of DLL:
    1

    Get node from second half of DLL:
    2

"""
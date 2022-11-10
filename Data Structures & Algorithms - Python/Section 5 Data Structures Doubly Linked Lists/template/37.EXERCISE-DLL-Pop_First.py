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

    ## WRITE POP_FIRST METHOD HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################




my_doubly_linked_list = ? 2)
?.append(1)


# (2) Items - Returns 2 Node
print(?.pop_first().value)
# (1) Item -  Returns 1 Node
print(?.pop_first().value)
# (0) Items - Returns None
print(?.pop_first())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
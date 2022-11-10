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

    ### WRITE POP METHOD HERE ###
    #                           #
    #                           #
    #                           #
    #                           #
    #############################
  

  

my_doubly_linked_list = ? 1)
?.append(2)


# (2) Items - Returns 2 Node
print(?.p__.v..
# (1) Item -  Returns 1 Node
print(?.p__.v..
# (0) Items - Returns None
print(?.pop())



"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
c_ Node
    ___  - value
        value _ value
        next _ N..
        

c_ LinkedList
    ___  - value
        new_node _ ? v..
        head _ new_node
        tail _ new_node
        length _ 1

    ___ print_list
        temp _ head
        w____ temp __ n.. N..
            print(temp.v..
            temp _ ?.n..
        
    ___ appendvalue
        new_node _ ? v..
        __ length == 0
            head _ new_node
            tail _ new_node
        ____
            t__.n.. _ new_node
            tail _ new_node
        length +_ 1
        return True

    ___ pop
        __ length == 0
            return N..
        temp _ head
        pre _ head
        w____(?.n..)
            pre _ temp
            temp _ ?.n..
        tail _ pre
        t__.n.. _ N..
        length -_ 1
        __ length == 0
            head _ N..
            tail _ N..
        return temp

    ___ prependvalue
        new_node _ ? v..
        __ length == 0
            head _ new_node
            tail _ new_node
        ____
            new_node.n.. _ head
            head _ new_node
        length +_ 1
        return True

    ___ pop_first
        __ length == 0
            return N..
        temp _ head
        head _ head.n..
        ?.n.. _ N..
        length -_ 1
        __ length == 0
            tail _ N..
        return temp

    ### WRITE GET METHOD HERE ###
    #                           #
    #                           #
    #                           #
    #                           #
    #############################
        



my_linked_list _ ? 0)
?.a.. 1)
?.a.. 2)
?.a.. 3)

print(?.get(3).v..


"""
    EXPECTED OUTPUT:
    ----------------
    3

"""
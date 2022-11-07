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

    ___ get(self, index)
        __ index < 0 or index >_ length
            return N..
        temp _ head
        for _ in range(index)
            temp _ ?.n..
        return temp
        
    ___ set_value(self, index, v..
        temp _ get(index)
        __ temp
            temp.value _ value
            return True
        return False
    



my_linked_list _ ? 11)
?.a.. 3)
?.a.. 23)
?.a.. 7)

print('LL before set_value():')
?.p..

?.set_value(1,4)

print('\nLL after set_value():')
?.p..



"""
    EXPECTED OUTPUT:
    ----------------
    LL before set_value():
    11
    3
    23
    7

    LL after set_value():
    11
    4
    23
    7
"""
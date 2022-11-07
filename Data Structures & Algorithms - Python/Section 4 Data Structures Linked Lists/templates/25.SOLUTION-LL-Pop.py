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

 


my_linked_list _ ? 1
?.a.. 2)

# (2) Items - Returns 2 Node
print(?.pop().v..
# (1) Item -  Returns 1 Node
print(?.pop().v..
# (0) Items - Returns None
print(?.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
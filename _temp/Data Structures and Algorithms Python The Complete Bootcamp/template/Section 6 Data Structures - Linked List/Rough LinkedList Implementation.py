c_ Node:
    ___ -  value_None, next_None, prev_None
        value _ value
        next _ next
        prev _ prev


c_ LinkedList:
    ___ -
        head _ N..

    ___ insert
        pass

    ___ delete
        pass

    # Traverse Method To Print All Elements #
    ___ traverse
        node _ head
        _____ node __ n.. N..:
            print(node.value)
            node _ node.next


n1 _ Node(3)
n2 _ Node(7)
n3 _ Node(2)
n4 _ Node(9)

LL _ LinkedList()
LL.head _ n1
n1.next _ n2
n2.next _ n3
n3.next _ n4

# Traverse Method To Print All Elements #
LL.traverse()
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            t.. _ ?.n..
        t.. _ p..
        t__.n.. _ N..
        l.. -_ 1
        __ l.. __ 0
            h.. _ N..
            t.. _ N..
        r_ ?

    ___ prependvalue
        n.. _ ? v..
        __ l.. __ 0
            h.. _ ?
            t.. _ ?
        ____
            ?.n.. _ h..
            h.. _ ?
        l.. +_ 1
        r_ T..

    ___ pop_first
        __ l.. __ 0
            r_ N..
        t.. _ h..
        h.. _ ?.n..
        ?.n.. _ N..
        l.. -_ 1
        __ l.. __ 0
            t.. _ N..
        r_ ?

    ___ get  index
         __  ? < 0 __ ? >_ l..
            r_ N..
        t.. _ h..
        ___ _ __ r.. ?
            t.. _ ?.n..
        r_ ?

    ___ set_value  index, v..
        t.. _ g.. ?
        __ ?
            ?.? _ ?
            r_ T..
        r_ F..




my_linked_list _ ? 11
?.a.. 3
?.a.. 23
?.a.. 7

print('LL before set_value():')
?.p..

?.s.. 1 4

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
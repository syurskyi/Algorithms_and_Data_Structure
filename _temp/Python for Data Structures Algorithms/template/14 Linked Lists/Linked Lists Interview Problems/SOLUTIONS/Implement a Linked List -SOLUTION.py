# Implement a Linked List - SOLUTION
# Problem Statement
# Implement a Linked List by using a Node class object. Show how you would implement a Singly Linked List and
# a Doubly Linked List!
# Solution
# Since this is asking the same thing as the implementation lectures, please refer to those video lectures and notes
# for a full explanation. The code from those lectures is displayed below:
# Singly Linked List
#
c_ LinkedListNode o..

    ___ - value

        value _ value
        nextnode _ N..

a _ LinkedListNode(1)
b _ LinkedListNode(2)
c _ LinkedListNode(3)

a.nextnode _ b
b.nextnode _ c

# Doubly Linked List
#
c_ DoublyLinkedListNode o..

    ___ - value

        value _ value
        next_node _ N..
        prev_node _ N..

a _ DoublyLinkedListNode(1)
b _ DoublyLinkedListNode(2)
c _ DoublyLinkedListNode(3)

# Setting b after a
b.prev_node _ a
a.next_node _ b

# Setting c after a
b.next_node _ c
c.prev_node _ b

# Good Job!
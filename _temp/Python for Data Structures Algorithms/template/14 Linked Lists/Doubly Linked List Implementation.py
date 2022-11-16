# Doubly Linked List Implementation
#
# In this lecture we will implement a Doubly Linked List
#
c_ DoublyLinkedListNode o..

    ___ - value

        value _ value
        next_node _ N..
        prev_node _ N..

# Now that we have our node that can reference next and previous values, let's begin to build out our linked list!

a _ DoublyLinkedListNode(1)
b _ DoublyLinkedListNode(2)
c _ DoublyLinkedListNode(3)

# Setting b after a
b.prev_node _ a
a.next_node _ b

# Setting c after a
b.next_node _ c
c.prev_node _ b

# Having a Doubly Linked list allows us to go though our Linked List forwards and backwards.
# Doubly Linked List Implementation
#
# In this lecture we will implement a Doubly Linked List
#
class DoublyLinkedListNode(object):

    def __init__(self,value):

        self.value = value
        self.next_node = None
        self.prev_node = None

# Now that we have our node that can reference next and previous values, let's begin to build out our linked list!

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

# Setting b after a
b.prev_node = a
a.next_node = b

# Setting c after a
b.next_node = c
c.prev_node = b

# Having a Doubly Linked list allows us to go though our Linked List forwards and backwards.
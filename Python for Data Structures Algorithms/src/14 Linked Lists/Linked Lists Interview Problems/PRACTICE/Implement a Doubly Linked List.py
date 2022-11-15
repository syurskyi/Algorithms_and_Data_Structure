# Implement a Doubly Linked List
#
# For this interview problem, implement a node class and show how it can be used to create a doubly linked list.
#
class Node(object):
    def __init__(self, value):
        self.prev = None
        self.val = value
        self.next = None
    pass
#
# # Create a Doubly Linked List here
#
# Test Your Solution
#
# Note that there is no test for this solution (because it would give away the answer structure).
#
# Check out the Implement a Linked List Solution Notebook for the answer to this interview problem, as well as
# the answer for the implementation of a singly linked list.
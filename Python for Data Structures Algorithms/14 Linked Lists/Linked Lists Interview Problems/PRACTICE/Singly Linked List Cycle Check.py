# Singly Linked List Cycle Check
# Problem
# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns
# a boolean indicating if the linked list contains a "cycle".
# A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known
# as a circularly linked list.
# You've been given the Linked List Node class code:
#
class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

# Solution
# Fill out your solution:
#
def cycle_check(node):
#     Use fast and slow pointer
    fast, slow = node, node
    while fast and fast.nextnode:
        fast = fast.nextnode
        if fast == slow:
            return True
        fast = fast.nextnode
        slow = slow.nextnode
    return False
    pass #Your function should return a boolean

# Test Your Solution

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):

    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)

        print ("ALL TEST CASES PASSED")

# Run Tests

t = TestCycleCheck()
t.test(cycle_check)
#
# ALL TEST CASES PASSED
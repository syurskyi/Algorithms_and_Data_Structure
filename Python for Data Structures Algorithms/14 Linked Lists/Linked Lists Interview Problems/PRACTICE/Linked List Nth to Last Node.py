# Linked List Nth to Last Node
# Problem Statement
#
# Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

# Example Input and Output:

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# # This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)

target_node.value#
# 4
#
# Solution
#
# Fill out your solution below:
#
def nth_to_last_node(n, head):
    slow, fast = head, head
    while n > 0 and fast:
        fast=fast.nextnode
        n-=1
    if not fast:
        return head
    while fast:
        fast=fast.nextnode
        slow=slow.nextnode
    return slow
    pass
#
# Test Your Solution
#
# """
# RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE
#
# PLEASE NOTE THIS IS JUST ONE CASE
# """
#
from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):

    def test(self,sol):

        assert_equal(sol(2,a),d)
        print ('ALL TEST CASES PASSED')

# Run tests
t = TestNLast()
t.test(nth_to_last_node)

# ALL TEST CASES PASSED
# Linked List Nth to Last Node - SOLUTION
# Problem Statement
#
# Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:
#
c_ Node:

    ___ -  value
        value _ value
        nextnode  _ N..

a _ Node(1)
b _ Node(2)
c _ Node(3)
d _ Node(4)
e _ Node(5)

a.nextnode _ b
b.nextnode _ c
c.nextnode _ d
d.nextnode _ e

# # This would return the node d with a value of 4, because its the 2nd to last node.
target_node _ nth_to_last_node(2, a)
#
target_node.value
# 4
#
# Solution
# One approach to this problem is this:
# Imagine you have a bunch of nodes and a "block" which is n-nodes wide. We could walk this "block" all the way down
# the list, and once the front of the block reached the end, then the other end of the block would be a the Nth node!
# So to implement this "block" we would just have two pointers a left and right pair of pointers. Let's mark out
# the steps we will need to take:
#
#     Walk one pointer n nodes from the head, this will be the right_point
#     Put the other pointer at the head, this will be the left_point
#     Walk/traverse the block (both pointers) towards the tail, one node at a time, keeping a distance n between them.
#     Once the right_point has hit the tail, we know that the left point is at the target.
#
# Let's see the code for this!
#
___ nth_to_last_node(n, head

    left_pointer  _ head
    right_pointer _ head

    # Set right pointer at n nodes away from head
    ___ i __ xrange(n-1

        # Check for edge case of not having enough nodes!
        __ n.. right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer _ right_pointer.nextnode

    # Move the block down the linked list
    _____ right_pointer.nextnode:
        left_pointer  _ left_pointer.nextnode
        right_pointer _ right_pointer.nextnode

    # Now return left pointer, its at the nth to last element!
    r_ left_pointer

# Test Your Solution
#
# """
# RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE
#
# PLEASE NOTE THIS IS JUST ONE CASE
# """
#
from nose.tools import assert_equal

a _ Node(1)
b _ Node(2)
c _ Node(3)
d _ Node(4)
e _ Node(5)

a.nextnode _ b
b.nextnode _ c
c.nextnode _ d
d.nextnode _ e

####

c_ TestNLast o..

    ___ testsol

        assert_equal(sol(2,a),d)
        print 'ALL TEST CASES PASSED'

# Run tests
t _ TestNLast()
t.test(nth_to_last_node)
#
# ALL TEST CASES PASSED
#
# Good Job!
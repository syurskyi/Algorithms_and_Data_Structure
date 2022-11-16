# Singly Linked List Cycle Check
# Problem
# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns
# a boolean indicating if the linked list contains a "cycle".
# A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known
# as a circularly linked list.
# You've been given the Linked List Node class code:
#
c_ Node o..

    ___ - value

        value _ value
        nextnode _ N..

# Solution
# Fill out your solution:
#
___ cycle_check(node
#     Use fast and slow pointer
    fast, slow _ node, node
    _____ fast and fast.nextnode:
        fast _ fast.nextnode
        __ fast __ slow:
            r_ True
        fast _ fast.nextnode
        slow _ slow.nextnode
    r_ False
    pass #Your function should return a boolean

# Test Your Solution

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a _ Node(1)
b _ Node(2)
c _ Node(3)

a.nextnode _ b
b.nextnode _ c
c.nextnode _ a # Cycle Here!


# CREATE NON CYCLE LIST
x _ Node(1)
y _ Node(2)
z _ Node(3)

x.nextnode _ y
y.nextnode _ z


#############
c_ TestCycleCheck o..

    ___ testsol
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)

        print ("ALL TEST CASES PASSED")

# Run Tests

t _ TestCycleCheck()
t.test(cycle_check)
#
# ALL TEST CASES PASSED
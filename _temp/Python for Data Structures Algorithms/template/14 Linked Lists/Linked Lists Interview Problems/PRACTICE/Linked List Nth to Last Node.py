# Linked List Nth to Last Node
# Problem Statement
#
# Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:

c_ Node:

    ___ -  value
        value _ value
        nextnode  _ N..

# Example Input and Output:

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

target_node.value#
# 4
#
# Solution
#
# Fill out your solution below:
#
___ nth_to_last_node(n, head
    slow, fast _ head, head
    _____ n > 0 ___ fast:
        fast_fast.nextnode
        n-_1
    __ n.. fast:
        r_ head
    _____ fast:
        fast_fast.nextnode
        slow_slow.nextnode
    r_ slow
    p..
#
# Test Your Solution
#
# """
# RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE
#
# PLEASE NOTE THIS IS JUST ONE CASE
# """
#
____ n___.t.. ______ assert_equal

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

        ? ? 2,a),d)
        print ('ALL TEST CASES PASSED')

# Run tests
t _ TestNLast()
t.test(nth_to_last_node)

# ALL TEST CASES PASSED
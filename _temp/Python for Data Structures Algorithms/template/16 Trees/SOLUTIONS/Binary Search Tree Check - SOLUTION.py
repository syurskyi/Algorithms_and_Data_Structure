# Binary Search Tree Check - SOLUTION
# Problem Statement
# Given a binary tree, check whether its a binary search tree or not.
# ** Again, no solution cell, just worry about your code making sense logically. Hint: Think about tree traversals. **
# Solution
# Here is a simple solution- If a tree is a binary search tree, then traversing the tree inorder should lead
# to sorted order of the values in the tree. So, we can perform an inorder traversal and check whether the node values
# are sorted or not.

tree_vals _    # list

___ inorder(tree
    __ tree !_ N..:
        inorder(tree.getLeftChild())
        tree_vals.a..(tree.getRootVal())
        inorder(tree.getRightChild())

___ sort_check(tree_vals
    r_ tree_vals __ sorted(tree_vals)

inorder(tree)
sort_check(tree_vals)
# True
#
# Another classic solution is to keep track of the minimum and maximum values a node can take. And at each node we will
# check whether its value is between the min and max values its allowed to take. The root can take any value between
# negative infinity and positive infinity. At any node, its left child should be smaller than or equal than
# its own value, and similarly the right child should be larger than or equal to. So during 001_recursion, we send
# the current value as the new max to our left child and send the min as it is without changing. And to the right child,
# we send the current value as the new min and send the max without changing.

c_ Node:
    ___ -  k, val
        key _ k
        value _ val
        left _ N..
        right _ N..

___ tree_max(node
    __ n.. node:
        r_ float("-inf")
    maxleft  _ tree_max(node.left)
    maxright _ tree_max(node.right)
    r_ max(node.key, maxleft, maxright)

___ tree_min(node
    __ n.. node:
        r_ float("inf")
    minleft  _ tree_min(node.left)
    minright _ tree_min(node.right)
    r_ min(node.key, minleft, minright)

___ verify(node
    __ n.. node:
        r_ True
    __ (tree_max(node.left) <_ node.key <_ tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        r_ True
    ____
        r_ False

root_ Node(10, "Hello")
root.left _ Node(5, "Five")
root.right_ Node(30, "Thirty")

print(verify(root)) # prints True, since this tree is valid

root _ Node(10, "Ten")
root.right _ Node(20, "Twenty")
root.left _ Node(5, "Five")
root.left.right _ Node(15, "Fifteen")

print(verify(root)) # prints False, since 15 is to the left of 10
# True
# False
#
# This is a classic interview problem, so feel free to just Google search "Validate BST" for more information
# on this problem!
# Good Job!
# Tree Level Order Print
#
# Given a binary tree of integers, print it in level order. The output will contain space between the numbers in
# the same level, and new line between different levels. For example, if the tree is:
#
# title
#
# The output should be:
#
# 1
# 2 3
# 4 5 6
#
# Solution
#
# Fill out your solution below:

c_ Node:
    ___ -  val_None
        left _ N..
        right _ N..
        val _  val

from collections import deque
___ levelOrderPrint(tree
    __ tree __ N..
        r_

    queue _ deque()
    queue.a..(tree)
    _____ l..(queue) !_ 0:
        temp _ deque()
        _____ l..(queue) !_ 0:
            node _ queue.p.. 
            print(s..(node.val) + ' ')
            __ node.left __ n.. N..
                ?.a..(tree.left)
            __ node.right __ n.. N..
                ?.a..(tree.right)
            queue _ temp

root _ Node(2)
root.left _ Node(1)
root.right _ Node(3)

levelOrderPrint(root)
#
# 2
# 3
# 1
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

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val

from collections import deque
def levelOrderPrint(tree):
    if tree is None:
        return

    queue = deque()
    queue.append(tree)
    while len(queue) != 0:
        temp = deque()
        while len(queue) != 0:
            node = queue.pop()
            print(str(node.val) + ' ')
            if node.left is not None:
                temp.append(tree.left)
            if node.right is not None:
                temp.append(tree.right)
            queue = temp

root = Node(2)
root.left = Node(1)
root.right = Node(3)

levelOrderPrint(root)
#
# 2
# 3
# 1
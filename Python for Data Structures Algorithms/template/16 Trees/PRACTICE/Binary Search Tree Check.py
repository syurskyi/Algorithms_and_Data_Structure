# Binary Search Tree Check
# Problem Statement
# Given a binary tree, check whether its a binary search tree or not.
# ** Again, no solution cell, just worry about your code making sense logically. Hint: Think about tree traversals. **
# Solution
# Fill out your solution below:
# # Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        return self.is_valid(root, -math.inf, math.inf)

    def is_valid(self, root, min_val, max_val):
        if root is None:
            return True
        else:
            return ( root.val > min_val and root.val < max_val and
                self.is_valid(root.left, min_val, root.val) and
                self.is_valid(root.right, root.val, max_val) )

# This is a classic interview problem, so feel free to just Google search "Validate BST" for more information on this
# problem!
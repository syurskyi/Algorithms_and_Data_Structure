'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return root
        stack = [root]
        prev = TreeNode(-1)
        while stack:
            node = stack.pop()
            prev.right = node
            if node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                stack.append(node.left)
                node.left = None
            prev = node

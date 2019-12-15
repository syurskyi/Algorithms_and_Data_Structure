'''
Created on Oct 3, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        return self.getLeaves(root1) == self.getLeaves(root2)
        
    
    def getLeaves(self, root):
        res = []
        node = root
        stack = []
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
            if node.right:
                node0 = node.right
                while node0:
                    stack.append(node0)
                    node0 = node0.left
        return res

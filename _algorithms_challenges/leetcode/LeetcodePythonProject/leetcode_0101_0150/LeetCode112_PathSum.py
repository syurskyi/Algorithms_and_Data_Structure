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
    def hasPathSum(self, root, sumVal):
        """
        :type root: TreeNode
        :type sumVal: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val == sumVal and not root.left and not root.right:
            return True
        else:
            return self.hasPathSum(root.left, sumVal-root.val) or\
                self.hasPathSum(root.right, sumVal-root.val)
    
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        else:
            return abs(self.getHeight(root.left)-self.getHeight(root.right)) <= 1 and\
                self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, root):
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        return max(leftHeight, rightHeight) + 1
    
    def test(self):
        pass
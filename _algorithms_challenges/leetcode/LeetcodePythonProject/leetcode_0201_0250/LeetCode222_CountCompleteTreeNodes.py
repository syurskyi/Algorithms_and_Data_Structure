'''
Created on Feb 21, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import math
        if not root: return 0
        leftHeight = self.getLeftHeight(root)
        rightHeight = self.getRightHeight(root)
        if leftHeight == rightHeight:
            return int(math.pow(2, leftHeight)) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
    def getLeftHeight(self, root):
        height = 0
        node = root
        while node:
            node = node.left
            height += 1
        return height
    
    def getRightHeight(self, root):
        height = 0
        node = root
        while node:
            node = node.right
            height += 1
        return height

'''
Created on Apr 9, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root: return 0
        sumVal = 0
        if root.left:
            if not root.left.left and not root.left.right:
                sumVal += root.left.val
            else:
                sumVal += self.sumOfLeftLeaves(root.left)
        if root.right:
            sumVal += self.sumOfLeftLeaves(root.right)
        return sumVal
    
    
'''
Created on Mar 4, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result= root.val
        while root:
            if abs(target - root.val) < abs(target-result):
                result = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return result

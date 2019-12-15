'''
Created on Mar 19, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        return self.helper(root)[-1]
    
    #isBST, lower, upper, count
    def helper(self, root):
        if not root:
            return True, float('inf'), float('-inf'), 0
        leftBST, leftLower, leftUpper, leftCount = self.helper(root.left)
        rightBST, rightLower, rightUpper, rightCount = self.helper(root.right)
        lower = min(leftLower, root.val)
        upper = max(rightUpper, root.val)
        if leftBST and rightBST and leftUpper < root.val < rightLower:
            return True, lower, upper, 1+leftCount+rightCount
        else:
            return False, lower, upper, max(leftCount, rightCount)
    
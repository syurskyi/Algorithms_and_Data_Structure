'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, l, r):
        if l > r: return None
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, l, mid-1)
        root.right = self.helper(nums, mid+1, r)
        return root

'''
Created on May 9, 2018

@author: tongq
'''
class TreeNode(object):
    def __init__(self, start, end, sumVal=0):
        self.sumVal = sumVal
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            self.root = None
        else:
            self.root = self.buildTree(nums, 0, len(nums)-1)
    
    def buildTree(self, nums, i, j):
        if not nums or i > j:
            return None
        if i == j:
            return TreeNode(i, j, nums[i])
        root = TreeNode(i, j, -1)
        mid = (i+j)//2
        root.left = self.buildTree(nums, i, mid)
        root.right = self.buildTree(nums, mid+1, j)
        root.sumVal = root.left.sumVal+root.right.sumVal
        return root

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateHelper(self.root, i, val)
    
    def updateHelper(self, root, i, val):
        if not root: return
        if i == root.start and i == root.end:
            root.sumVal = val
            return
        mid = (root.start+root.end)//2
        if i <= mid:
            self.updateHelper(root.left, i, val)
        else:
            self.updateHelper(root.right, i, val)
        root.sumVal = root.left.sumVal+root.right.sumVal
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRangeHelper(self.root, i, j)
    
    def sumRangeHelper(self, root, i, j):
        if not root or i > j or j < root.start or i > root.end:
            return 0
        if i == root.start and j == root.end:
            return root.sumVal
        mid = (root.start+root.end)//2
        res = self.sumRangeHelper(root.left, i, min(j, mid))+\
            self.sumRangeHelper(root.right, max(i, mid+1), j)
        return res

'''
Created on Mar 11, 2017

@author: MT
'''

class STreeNode(object):
    def __init__(self, left, right, sumVal=0):
        self.start = left
        self.end = right
        self.sumVal = sumVal
        self.leftChild = None
        self.rightChild = None

class NumArray(object):
    def __init__(self, nums):
        if not nums:
            self.root = None
        else:
            self.root = self.buildTree(nums, 0, len(nums)-1)
    
    def buildTree(self, nums, i, j):
        if not nums or i > j:
            return None
        if i == j:
            return STreeNode(i, j, nums[i])
        curr = STreeNode(i, j)
        mid = i+(j-i)//2
        curr.leftChild = self.buildTree(nums, i, mid)
        curr.rightChild = self.buildTree(nums, mid+1, j)
        curr.sumVal = curr.leftChild.sumVal + curr.rightChild.sumVal
        return curr
    
    def update(self, i, val):
        self.updateHelper(self.root, i, val)
    
    def updateHelper(self, root, i, val):
        if not root:
            return
        mid = root.start+(root.end-root.start)//2
        if i <= mid:
            self.updateHelper(root.leftChild, i, val)
        else:
            self.updateHelper(root.rightChild, i, val)
        if root.start == i and root.end == i:
            root.sumVal = val
            return
        root.sumVal = root.leftChild.sumVal + root.rightChild.sumVal
    
    def sumRange(self, i, j):
        return self.sumRangeHelper(self.root, i, j)
    
    def sumRangeHelper(self, root, i, j):
        if not root or i > j or j < root.start or i > root.end:
            return 0
        if i == root.start and j == root.end:
            return root.sumVal
        mid = root.start + (root.end-root.start)//2
        result = self.sumRangeHelper(root.leftChild, i, min(j, mid)) +\
            self.sumRangeHelper(root.rightChild, max(i, mid+1), j)
        return result
    
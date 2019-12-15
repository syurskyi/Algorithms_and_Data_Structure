'''
Created on Oct 5, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        maxVal = max(nums)
        ind = nums.index(maxVal)
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(nums[:ind])
        root.right = self.constructMaximumBinaryTree(nums[ind+1:])
        return root
    
    def test(self):
        testCases = [
            [3, 2, 1, 6, 0, 5]
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            newNode = self.constructMaximumBinaryTree(nums)
            if newNode:
                print(newNode.val)
            else:
                print(None)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Oct 22, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLen = 0
        self.helper(root)
        return self.maxLen
    
    def helper(self, root):
        if not root: return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0
        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0
        self.maxLen = max(self.maxLen, left+right)
        return max(left, right)
    
    def test(self):
        testCases = [
            TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5))),
            TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5))),
        ]
        for root in testCases:
            result = self.longestUnivaluePath(root)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

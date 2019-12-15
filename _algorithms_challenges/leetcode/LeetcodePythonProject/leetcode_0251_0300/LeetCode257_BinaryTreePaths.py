'''
Created on Mar 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root: return []
        res = []
        self.helper(root, res, str(root.val))
        return res
    
    def helper(self, root, res, curr):
        if not root.left and not root.right:
            res.append(curr)
            return
        if root.left:
            self.helper(root.left, res, curr+('->%s' % root.left.val))
        if root.right:
            self.helper(root.right, res, curr+('->%s' % root.right.val))
    
    def test(self):
        testCases = [
            TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3)),
        ]
        for root in testCases:
            result = self.binaryTreePaths(root)
            print('result: %s' % (result))

if __name__ == '__main__':
    Solution().test()

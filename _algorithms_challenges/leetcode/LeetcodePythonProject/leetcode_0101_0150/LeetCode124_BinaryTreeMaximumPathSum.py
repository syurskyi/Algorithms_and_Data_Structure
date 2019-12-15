'''
Created on Feb 6, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.helper(root)[1]
    
    def helper(self, root):
        if not root:
            return 0, float('-inf')
        left  = self.helper(root.left)
        right = self.helper(root.right)
        single = max([left[0]+root.val, right[0]+root.val, 0])
        gbl = max([left[1], right[1], left[0]+right[0]+root.val])
        return single, gbl
    
    def test(self):
        pass
    
if __name__ == '__main__':
    Solution().test()

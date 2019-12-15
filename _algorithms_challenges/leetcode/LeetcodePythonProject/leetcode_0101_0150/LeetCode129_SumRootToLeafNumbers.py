'''
Created on Feb 8, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = []
        self.helper(root, str(root.val), res)
        resNum = sum([int(val) for val in res])
        return resNum
        
    def helper(self, root, curr, res):
        if not root.left and not root.right:
            res.append(curr)
        if root.left:
            self.helper(root.left, curr+str(root.left.val), res)
        if root.right:
            self.helper(root.right, curr+str(root.right.val), res)
    
    def test(self):
#         root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        result = self.sumNumbers(root)
        print(result)

if __name__ == '__main__':
    Solution().test()
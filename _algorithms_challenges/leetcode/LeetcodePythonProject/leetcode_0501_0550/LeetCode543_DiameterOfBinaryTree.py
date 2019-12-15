'''
Created on Aug 20, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.helper(root)[-1]-1
    
    # returns include, exclude
    def helper(self, root):
        if not root:
            return 0, 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        include = max(1+left[0], 1+right[0])
        exclude = max([left[1], right[1], left[0]+right[0]+1])
        return include, exclude
    
    def test(self):
        testCases = [
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        ]
        for root in testCases:
            result = self.diameterOfBinaryTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

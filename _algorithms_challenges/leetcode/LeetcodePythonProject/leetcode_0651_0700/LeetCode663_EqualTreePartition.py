'''
Created on Oct 8, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return False
        return self.helper(root, 0, True)
    
    def helper(self, root, sumVal, firstLevel):
        if not root:
            return False
        if sumVal == self.sum(root) and not firstLevel:
            return True
        if (root.left and self.helper(root.left, sumVal+root.val+self.sum(root.right), False)) or\
            (root.right and self.helper(root.right, sumVal+root.val+self.sum(root.left), False)):
            return True
        return False
    
    def sum(self, root):
        if not root: return 0
        res = root.val
        res += self.sum(root.left)
        res += self.sum(root.right)
        return res
    
    def sumVal(self, root):
        if not root: return 0
        return root.val +\
            self.sumVal(root.left)+\
            self.sumVal(root.right)
    
    def test(self):
        testCases = [
            TreeNode(5, TreeNode(10), TreeNode(10, TreeNode(2), TreeNode(3))),
            TreeNode(1, TreeNode(2), TreeNode(10, TreeNode(2), TreeNode(20))),
            TreeNode(1, TreeNode(-1)),
            TreeNode(1, None, TreeNode(2)),
            TreeNode(2, TreeNode(1, TreeNode(0), TreeNode(2, TreeNode(3))), TreeNode(3)),
        ]
        for root in testCases:
            result = self.checkEqualTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

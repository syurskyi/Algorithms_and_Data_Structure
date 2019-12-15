'''
Created on Sep 7, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        root = TreeNode(-1)
        if t1 and not t2:
            root.val = t1.val
            root.left = self.mergeTrees(t1.left, t2)
            root.right = self.mergeTrees(t1.right, t2)
        elif not t1 and t2:
            root.val = t2.val
            root.left = self.mergeTrees(t1, t2.left)
            root.right = self.mergeTrees(t1, t2.right)
        elif t1 and t2:
            root.val = t1.val + t2.val
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        else:
            root = None
        return root
    
    def test(self):
        testCases = [
            [
                TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
                TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7))),
            ],
        ]
        for t1, t2 in testCases:
            root = self.mergeTrees(t1, t2)
            print(root.val)

if __name__ == '__main__':
    Solution().test()

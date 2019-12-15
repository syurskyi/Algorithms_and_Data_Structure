'''
Created on Jan 31, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.first = None
        self.second = None
        self.prev = None
        self.inOrder(root)
        if self.second and self.first:
            val = self.second.val
            self.second.val = self.first.val
            self.first.val = val
    
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.prev:
            if root.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = root
        self.prev = root
        self.inOrder(root.right)
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()
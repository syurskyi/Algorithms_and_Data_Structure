'''
Created on Sep 6, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = ''
        if t:
            res += str(t.val)
            if t.right:
                res += '(%s)' % self.tree2str(t.left)
                res += '(%s)' % self.tree2str(t.right)
            elif t.left:
                res += '(%s)' % self.tree2str(t.left)
        return res

'''
Created on Oct 11, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        l, r = L, R
        if not root or l > r:
            return None
        val = root.val
        if l <= val <= r:
            newRoot = TreeNode(val)
            newRoot.left = self.trimBST(root, l, val-1)
            newRoot.right = self.trimBST(root, val+1, r)
            return newRoot
        elif val < l:
            return self.trimBST(root.right, l, r)
        else:
            return self.trimBST(root.left, l, r)
    
    def test(self):
        testCases = [
        ]
        for root, l, r in testCases:
            newRoot = self.trimBST(root, l, r)
            print(newRoot)

if __name__ == '__main__':
    Solution().test()

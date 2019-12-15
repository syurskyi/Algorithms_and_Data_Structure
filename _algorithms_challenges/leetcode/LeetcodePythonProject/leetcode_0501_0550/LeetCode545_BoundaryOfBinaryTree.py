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
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        if not root.left and not root.right: return [root.val]
        leftBoundary = self.getLeft(root)
        leaves = []
        self.getLeaves(root, leaves)
        rightBoundary = self.getRight(root)
        return leftBoundary + leaves + rightBoundary
    
    def getLeft(self, root):
        result = [root.val]
        root = root.left
        while root:
            if root.left or root.right:
                result.append(root.val)
            if root.left:
                root = root.left
            else:
                root = root.right
        return result
    
    def getLeaves(self, root, leaves):
        if not root: return
        if not root.left and not root.right:
            leaves.append(root.val)
            return
        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)
    
    def getRight(self, root):
        result = []
        root = root.right
        while root:
            if root.left or root.right:
                result.append(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left
        result.reverse()
        return result
    
    def test(self):
        testCases = [
            TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4))),
        ]
        for root in testCases:
            res = self.boundaryOfBinaryTree(root)
            print('result: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

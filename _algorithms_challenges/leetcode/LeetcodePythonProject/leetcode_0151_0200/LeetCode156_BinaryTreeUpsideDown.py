'''
Created on Feb 11, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        root = stack.pop()
        node = root
        while stack:
            newNode = stack.pop()
            right = newNode.right
            node.left = right
            node.right = newNode
            newNode.left = None
            newNode.right = None
            node = newNode
        return root
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()
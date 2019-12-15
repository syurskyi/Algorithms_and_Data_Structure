'''
Created on Feb 14, 2017

@author: MT
'''

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root:
            self.stack.append(root)
            while root.left:
                root = root.left
                self.stack.append(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0
    
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        val = node.val
        if node.right:
            node = node.right
            self.stack.append(node)
            while node.left:
                node = node.left
                self.stack.append(node)
        return val

'''
Created on Mar 6, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def inorderSuccessor(self, root, p):
        if not root: return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            if left:
                return left
            else:
                return root
    
    def inorderSuccessorNonRec(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node.val
        stack = []
        node = root
        while node != p:
            stack.append(node)
            if node.val > p.val:
                node = node.left
            elif node.val < p.val:
                node = node.right
            else:
                break
        while stack and stack[-1].val < p.val:
            stack.pop()
        if not stack:
            return None
        node = stack[-1]
        return node

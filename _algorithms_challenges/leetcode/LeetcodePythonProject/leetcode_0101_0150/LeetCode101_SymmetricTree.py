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
    def isSymmetricRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.helper(root.left, root.left)
    
    def helper(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.helper(left.left, right.right) and\
                self.helper(left.right, right.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        stack = []
        if root.left:
            if not root.right: return False
            stack.append(root.left)
            stack.append(root.right)
        elif root.right:
            return False
        while stack:
            if len(stack)%2 != 0:
                return False
            right = stack.pop()
            left = stack.pop()
            if right.val != left.val:
                return False
            if left.left:
                if not right.right:
                    return False
                stack.append(left.left)
                stack.append(right.right)
            elif right.right:
                return False
            if left.right:
                if not right.left:
                    return False
                stack.append(left.right)
                stack.append(right.left)
            elif right.left:
                return False
        return True
        
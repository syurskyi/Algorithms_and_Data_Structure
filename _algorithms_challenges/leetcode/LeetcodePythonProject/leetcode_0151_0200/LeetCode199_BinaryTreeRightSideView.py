'''
Created on May 17, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        queue = [root]
        nextQueue = []
        res = [root.val]
        while queue:
            node = queue.pop(0)
            if node.left:
                nextQueue.append(node.left)
            if node.right:
                nextQueue.append(node.right)
            if not queue:
                if nextQueue:
                    res.append(nextQueue[-1].val)
                    queue = nextQueue
                    nextQueue = []
        return res

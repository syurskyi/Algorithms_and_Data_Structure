'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        queue, nextQueue, elem = [root], [], []
        order = True
        while queue:
            node = queue.pop(0)
            elem.append(node.val)
            if node.left:
                nextQueue.append(node.left)
            if node.right:
                nextQueue.append(node.right)
            if not queue:
                if not order:
                    res.append(elem[::-1])
                else:
                    res.append(elem)
                elem = []
                queue = nextQueue
                nextQueue = []
                order = not order
        return res

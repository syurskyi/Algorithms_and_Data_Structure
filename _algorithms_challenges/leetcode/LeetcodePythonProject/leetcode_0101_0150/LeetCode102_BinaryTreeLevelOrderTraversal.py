'''
Created on Feb 1, 2017

@author: MT
'''

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root: return result
        queue = []
        nextQueue = []
        elem = []
        queue.append(root)
        while queue:
            first = queue[0]
            elem.append(first.val)
            del queue[0]
            if first.left:
                nextQueue.append(first.left)
            if first.right:
                nextQueue.append(first.right)
            if not queue:
                result.append(elem)
                elem = []
                queue = nextQueue
                nextQueue = []
        return result

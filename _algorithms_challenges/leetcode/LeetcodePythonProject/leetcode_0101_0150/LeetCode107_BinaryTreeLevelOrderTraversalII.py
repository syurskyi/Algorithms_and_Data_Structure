'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = []
        nextQueue = []
        elem = []
        if not root:
            return result
        queue.append(root)
        while queue:
            node = queue.pop(0)
            elem.append(node.val)
            if node.left:
                nextQueue.append(node.left)
            if node.right:
                nextQueue.append(node.right)
            if not queue:
                result.insert(0, elem)
                queue = nextQueue
                nextQueue = []
                elem = []
        return result
    
    def test(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        result = self.levelOrderBottom(root)
        print('result: %s' % (result))

if __name__ == '__main__':
    Solution().test()

    
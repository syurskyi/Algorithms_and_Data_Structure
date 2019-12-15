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
    def pathSum(self, root, sumVal):
        """
        :type root: TreeNode
        :type sumVal: int
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        elem = [root.val]
        self.dfs(result, elem, root, sumVal-root.val)
        return result
    
    def dfs(self, result, elem, root, sumVal):
        if not root:
            return
        if sumVal == 0 and not root.left and not root.right:
            result.append(list(elem))
            return
        if root.left:
            elem.append(root.left.val)
            self.dfs(result, elem, root.left, sumVal-root.left.val)
            elem.pop()
        if root.right:
            elem.append(root.right.val)
            self.dfs(result, elem, root.right, sumVal-root.right.val)
            elem.pop()
    
    def test(self):
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
        sumVal = 22
        result = self.pathSum(root, sumVal)
        print('result: %s' % (result))

if __name__ == '__main__':
    Solution().test()
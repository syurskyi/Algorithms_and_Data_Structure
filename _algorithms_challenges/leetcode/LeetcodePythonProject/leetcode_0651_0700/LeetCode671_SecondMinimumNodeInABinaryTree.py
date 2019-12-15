'''
Created on Oct 12, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1
        first = float('inf')
        second = float('inf')
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val < first:
                second = first
                first = node.val
            elif first < node.val < second:
                second = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return second if second != float('inf') else -1
    
    def test(self):
        testCases = [
            TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7))),
        ]
        for root in testCases:
            result = self.findSecondMinimumValue(root)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

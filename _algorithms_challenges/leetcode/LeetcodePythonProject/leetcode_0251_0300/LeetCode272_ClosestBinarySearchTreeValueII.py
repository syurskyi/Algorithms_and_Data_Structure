'''
Created on Mar 5, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        stack1, stack2 = [], []
        res = []
        self.inOrderReg(root, target, stack1)
        self.inOrderRev(root, target, stack2)
        print('stack1: %s' % stack1)
        print('stack2: %s' % stack2)
        for _ in range(k):
            if not stack1:
                res.append(stack2.pop())
            elif not stack2:
                res.append(stack1.pop())
            elif abs(stack1[-1]-target) <= abs(stack2[-1]-target):
                res.append(stack1.pop())
            else:
                res.append(stack2.pop())
        return res
    
    def inOrderReg(self, root, target, stack):
        if not root: return
        self.inOrderReg(root.left, target, stack)
        if root.val > target: return
        stack.append(root.val)
        self.inOrderReg(root.right, target, stack)
    
    def inOrderRev(self, root, target, stack):
        if not root: return
        self.inOrderRev(root.right, target, stack)
        if root.val <= target: return
        stack.append(root.val)
        self.inOrderRev(root.left, target, stack)
    
    def test(self):
        root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(7)), TreeNode(15, TreeNode(13), TreeNode(20)))
        target = 13.5
        k = 5
        result = self.closestKValues(root, target, k)
        print('result: %s' % (result))
        print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

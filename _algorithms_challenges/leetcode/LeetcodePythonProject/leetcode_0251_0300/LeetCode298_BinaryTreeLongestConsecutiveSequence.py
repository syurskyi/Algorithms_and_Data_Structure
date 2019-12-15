'''
Created on Mar 9, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def longestConsecutive(self, root):
        if not root: return 0
        result = [1]
        self.helper(root, 1, result)
        return result[0]
    
    def helper(self, root, length, result):
        if not root.left and not root.right:
            result[0] = max(result[0], length)
            return
        if root.left:
            if root.left.val == root.val+1:
                self.helper(root.left, length+1, result)
            else:
                result[0] = max(result[0], length)
                self.helper(root.left, 1, result)
        if root.right:
            if root.right.val == root.val+1:
                self.helper(root.right, length+1, result)
            else:
                result[0] = max(result[0], length)
                self.helper(root.right, 1, result)
    
    def test(self):
        root = TreeNode(1, None, TreeNode(3, TreeNode(2), TreeNode(4, None, TreeNode(5))))
        result = self.longestConsecutive(root)
        print('result: %s' % (result))

if __name__ == '__main__':
    Solution().test()

    
'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack, result = [root], []
        while stack:
            node = stack[-1] # peek
            if not node.left and not node.right:
                pop = stack.pop()
                result.append(pop.val)
            else:
                if node.right:
                    stack.append(node.right)
                    node.right = None
                if node.left:
                    stack.append(node.left)
                    node.left = None
        return result
    
    def test(self):
        testCases = [
            TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, None, TreeNode(9)))
        ]
        for root in testCases:
            result = self.postorderTraversal(root)
            print('result: %s' % (result))

if __name__ == '__main__':
    Solution().test()

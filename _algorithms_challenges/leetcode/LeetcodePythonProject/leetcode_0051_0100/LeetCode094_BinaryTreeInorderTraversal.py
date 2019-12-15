'''
Created on Jan 29, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return result
    
    def test(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        result = self.inorderTraversal(root)
        print(result)

def main():
    Solution().test()

if __name__ == '__main__':
    main()
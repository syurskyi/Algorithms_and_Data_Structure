'''
Created on Apr 8, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root: return [None, None]
        stack = []
        root0 = root
        while root0:
            stack.append(root0)
            root0 = root0.left
        preNode = None
        while stack:
            node = stack.pop()
            if (not preNode and V < node.val)\
                or (preNode and preNode.val <= V < node.val):
                return self.getRes(root, preNode)
            else:
                preNode = node
                node0 = node.right
                while node0:
                    stack.append(node0)
                    node0 = node0.left
        return [root, None]
    
    def getRes(self, root, node):
        root0 = root
        if not node:
            return [root0, None]
        stack = []
        while node != root0:
            stack.append(root0)
            if root0.val > node.val:
                root0 = root0.left
            else:
                root0 = root0.right
        cand = node
        while stack and stack[-1].val < node.val:
            cand = stack.pop()
        if not stack:
            right = node.right
            node.right = None
            return [root, right]
        else:
            right = node.right
            node.right = None
            stack[-1].left = right
            return [root, cand]
    
    def test(self):
        testCases = [
            [
                TreeNode(4,
                         TreeNode(2, TreeNode(1), TreeNode(3)),
                         TreeNode(6, TreeNode(5), TreeNode(7)),
                        ),
                2,
            ],
            [
                TreeNode(4,
                         TreeNode(2, TreeNode(1), TreeNode(3)),
                         TreeNode(6, TreeNode(5), TreeNode(7)),
                        ),
                3,
            ],
        ]
        for root, v in testCases:
            result = self.splitBST(root, v)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

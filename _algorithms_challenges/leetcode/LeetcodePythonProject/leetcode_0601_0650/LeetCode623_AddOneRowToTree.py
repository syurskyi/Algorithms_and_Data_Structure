'''
Created on Sep 10, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        level = 1
        queue = [root]
        while queue:
            num = len(queue)
            for _ in range(num):
                node = queue.pop(0)
                if node.left:
                    if level == d-1:
                        newNode = TreeNode(v)
                        node0 = node.left
                        node.left = newNode
                        newNode.left = node0
                        queue.append(newNode)
                    else:
                        queue.append(node.left)
                elif level == d-1:
                    node.left = TreeNode(v)
                    queue.append(node.left)
                if node.right:
                    if level == d-1:
                        newNode = TreeNode(v)
                        node0 = node.right
                        node.right = newNode
                        newNode.right = node0
                        queue.append(newNode)
                    else:
                        queue.append(node.right)
                elif level == d-1:
                    node.right = TreeNode(v)
                    queue.append(node.right)
            level += 1
        return root
    
    def test(self):
        testCases = [
            [
                TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5))),
                1,
                2
            ],
            [
                TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1))),
                1,
                3
            ],
        ]
        for root, v, d in testCases:
            newRoot = self.addOneRow(root, v, d)
            print(newRoot.val)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

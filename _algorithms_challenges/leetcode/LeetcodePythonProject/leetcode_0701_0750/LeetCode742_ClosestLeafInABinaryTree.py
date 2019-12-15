'''
Created on Mar 21, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        backMap = {}
        kNode = self.dfs(root, k, backMap)
        queue = [kNode]
        visited = set([kNode])
        while queue:
            curr = queue.pop(0)
            if not curr.left and not curr.right:
                return curr.val
            if curr.left and curr.left not in visited:
                queue.append(curr.left)
                visited.add(curr.left)
            if curr.right and curr.right not in visited:
                queue.append(curr.right)
                visited.add(curr.right)
            if curr in backMap and backMap[curr] not in visited:
                queue.append(backMap[curr])
                visited.add(backMap[curr])
        return -1
    
    def dfs(self, root, k, backMap):
        if root.val == k:
            return root
        if root.left:
            backMap[root.left] = root
            left = self.dfs(root.left, k, backMap)
            if left:
                return left
        if root.right:
            backMap[root.right] = root
            right = self.dfs(root.right, k, backMap)
            if right:
                return right
        return None
    
    def test(self):
        testCases = [
            
        ]
        for root, k in testCases:
            result = self.findClosestLeaf(root, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Sep 18, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        hashmap = {}
        self.find(root, target, hashmap)
        res = []
        self.dfs(root, target, K, hashmap[root], res, hashmap)
        return res
    
    def find(self, root, target, hashmap):
        if not root: return -1
        if root == target:
            hashmap[root] = 0
            return 0
        left = self.find(root.left, target, hashmap)
        if left >= 0:
            hashmap[root] = left+1
            return left+1
        right = self.find(root.right, target, hashmap)
        if right >= 0:
            hashmap[root] = right+1
            return right+1
        return -1
    
    def dfs(self, root, target, k, length, res, hashmap):
        if not root: return
        if root in hashmap:
            length = hashmap[root]
        if length == k:
            res.append(root.val)
        self.dfs(root.left, target, k, length+1, res, hashmap)
        self.dfs(root.right, target, k, length+1, res, hashmap)

if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    
    res = Solution().distanceK(root, root.left.right, 1)
    print('res: %s' % res)

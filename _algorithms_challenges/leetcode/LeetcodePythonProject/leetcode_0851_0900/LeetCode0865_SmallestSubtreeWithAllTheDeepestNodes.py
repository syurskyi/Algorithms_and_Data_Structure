'''
Created on Sep 29, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.deep(root)[1]
    
    def deep(self, root):
        if not root:
            return 0, None
        l, r = self.deep(root.left), self.deep(root.right)
        if l[0] > r[0]:
            return l[0]+1, l[1]
        elif l[0] < r[0]:
            return r[0]+1, r[1]
        else:
            return l[0]+1, root
    
    def subtreeWithAllDeepest_own_twoPass(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        hashmap = {}
        self.gatherDepths(root, 0, hashmap)
        maxDepth = max(hashmap.keys())
        nodes = hashmap[maxDepth]
        return self.getCommonParent(root, nodes)
    
    def gatherDepths(self, root, depth, hashmap):
        if not root:
            return
        if depth in hashmap:
            hashmap[depth].append(root)
        else:
            hashmap[depth] = [root]
        self.gatherDepths(root.left, depth+1, hashmap)
        self.gatherDepths(root.right, depth+1, hashmap)
    
    def getCommonParent(self, root, nodes):
        if not root:
            return None
        isLeft = True
        for node in nodes:
            if not self.isSubTree(root.left, node):
                isLeft = False
                break
        if isLeft:
            return self.getCommonParent(root.left, nodes)
        isRight = True
        for node in nodes:
            if not self.isSubTree(root.right, node):
                isRight = False
                break
        if isRight:
            return self.getCommonParent(root.right, nodes)
        else:
            return root
    
    def isSubTree(self, root, node):
        if not root:
            return False
        if root == node:
            return True
        if self.isSubTree(root.left, node) or self.isSubTree(root.right, node):
            return True

if __name__ == '__main__':
    Solution().test()

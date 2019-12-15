'''
Created on Mar 15, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        if not root: return []
        hashmap = {}
        result = []
        queue = [(0, root)]
        minLevel, maxLevel = 0, 0
        while queue:
            level, node = queue.pop(0)
            maxLevel = max(maxLevel, level)
            minLevel = min(minLevel, level)
            if level not in hashmap:
                hashmap[level] = [node.val]
            else:
                hashmap[level].append(node.val)
            if node.left:
                queue.append((level-1, node.left))
            if node.right:
                queue.append((level+1, node.right))
        for i in range(minLevel, maxLevel+1):
            result.append(hashmap[i])
        return result
    
    
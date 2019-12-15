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

class Codec:
    def serialize(self, root):
        stack = [root]
        result = ''
        while stack:
            node = stack.pop()
            if node:
                result += '%s,' % (node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                result += '#,'
        return result[:-1]
    
    def deserialize(self, data):
        arr = data.split(',')
        ind = [0]
        root = self.helper(arr, ind)
        return root
    
    def helper(self, arr, ind):
        if arr[ind[0]] == '#':
            return None
        root = TreeNode(arr[ind[0]])
        ind[0]+=1
        root.left = self.helper(arr, ind)
        ind[0]+=1
        root.right = self.helper(arr, ind)
        return root

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    codec = Codec()
    s = codec.serialize(root)
    print('s: %s' % (s))
    root = codec.deserialize(s)
    
    queue = [root]
    line = []
    nextQueue= []
    while queue:
        node = queue.pop(0)
        line.append(node.val)
        if node.left:
            nextQueue.append(node.left)
        if node.right:
            nextQueue.append(node.right)
        if not queue:
            print(line)
            line = []
            queue = nextQueue
            nextQueue = []
        
    
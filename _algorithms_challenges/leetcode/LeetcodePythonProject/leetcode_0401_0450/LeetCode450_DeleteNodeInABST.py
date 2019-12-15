'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object):
    def deleteNode(self, root, key):
        if not root: return None
        parent, node = self.findNode(key, root, None)
        if not node: return root
        if not parent:
            return self.removeNode(node)
        else:
            newNode = self.removeNode(node)
            if node == parent.left:
                parent.left = newNode
            else:
                parent.right = newNode
            return root
    
    def removeNode(self, node):
        if node.right:
            newRoot = node.right
            left = node.left
            node = newRoot
            while node.left:
                node = node.left
            node.left = left
            return newRoot
        elif node.left:
            newRoot = node.left
            right = node.right
            node = newRoot
            while node.right:
                node = node.right
            node.right = right
            return newRoot
        else:
            return None
    
    def findNode(self, key, root, parent):
        if not root:
            return None, None
        if root.val == key:
            return parent, root
        elif root.val > key:
            return self.findNode(key, root.left, root)
        else:
            return self.findNode(key, root.right, root)

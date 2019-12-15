'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
    
    def helper(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd or postStart > postEnd:
            return None
        val = postorder[postEnd]
        root = TreeNode(val)
        
        k = inorder.index(val)
        
        newInStart = inStart
        newInEnd = k-1
        newPostStart = postStart
        newPostEnd = postStart+k-inStart-1
        
        root.left = self.helper(inorder, newInStart, newInEnd,\
                                postorder, newPostStart, newPostEnd)
        
        newInStart = k+1
        newInEnd = inEnd
        newPostStart = postStart+k-inStart
        newPostEnd = postEnd-1
        
        root.right = self.helper(inorder, newInStart, newInEnd,\
                                 postorder, newPostStart, newPostEnd)
        
        return root

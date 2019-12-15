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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
    
    def helper(self, preorder, pstart, pend, inorder, istart, iend):
        if pstart > pend or istart > iend:
            return None
        val = preorder[pstart]
        root = TreeNode(val)
        k = inorder.index(val)
        
        new_pstart = pstart+1
        new_pend = pstart+k-istart
        new_istart = istart
        new_iend = k-1
        
        root.left = self.helper(preorder, new_pstart, new_pend,\
                                inorder, new_istart, new_iend)
        
        new_pstart = pstart+k-istart+1
        new_pend = pend
        new_istart = k+1
        new_iend = iend
        
        root.right = self.helper(preorder, new_pstart, new_pend,\
                                inorder, new_istart, new_iend)
        
        return root

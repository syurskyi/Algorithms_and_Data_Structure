# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ lowestCommonAncestor root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        __(root __ N..
            r_ N..
        __(root.val__p.val or root.val__q.val
            r_ root
        
        left _ lowestCommonAncestor(root.left,p,q)
        right _ lowestCommonAncestor(root.right,p,q)

        __(left __ N.. and right __ N..
            r_ N..
        __(left __ n.. N.. and right __ n.. N..
            r_ root
        __(left __ N..
            r_ right
        r_ left
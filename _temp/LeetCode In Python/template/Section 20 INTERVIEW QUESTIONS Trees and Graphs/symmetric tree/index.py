# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution
    ___ isMirrort1,t2
        __(t1 __ N.. ___ t2 __ N..
            r_ T..
        __(t1 __ N.. __ t2 __ N..
            r_ F..
        r_ (t1.val__t2.v..) ___ isMirror(t1.right,t2.left) ___ isMirror(t1.left,t2.right)
    ___ isSymmetric root: TreeNode) __ b..:
        r_ isMirror(root,root)
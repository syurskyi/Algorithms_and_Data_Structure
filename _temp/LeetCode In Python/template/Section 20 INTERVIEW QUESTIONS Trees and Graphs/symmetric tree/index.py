# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ isMirrort1,t2
        __(t1 __ N.. and t2 __ N..
            r_ True
        __(t1 __ N.. or t2 __ N..
            r_ False
        r_ (t1.val__t2.val) and isMirror(t1.right,t2.left) and isMirror(t1.left,t2.right)
    ___ isSymmetric root: TreeNode) -> bool:
        r_ isMirror(root,root)
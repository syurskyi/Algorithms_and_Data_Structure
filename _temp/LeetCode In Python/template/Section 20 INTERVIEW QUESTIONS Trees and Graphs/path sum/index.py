# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution
    ___ hasSumroot,sum,cur
        __(root __ N..
            r_ F..
        cur+_root.v..
        __(cur__sum ___ root.left __ N.. ___ root.right __ N..
            r_ T..
        r_ (hasSum(root.right,sum,cur) __ hasSum(root.left,sum,cur))
    ___ hasPathSum root: TreeNode, sum: i..) __ b..:
        r_ hasSum(root,sum, 0)
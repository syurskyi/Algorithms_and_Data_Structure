# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ hasSumroot,sum,cur
        __(root __ N..
            r_ False
        cur+_root.val
        __(cur==sum and root.left __ N.. and root.right __ N..
            r_ True
        r_ (hasSum(root.right,sum,cur) or hasSum(root.left,sum,cur))
    ___ hasPathSum root: TreeNode, sum: int) -> bool:
        r_ hasSum(root,sum, 0)
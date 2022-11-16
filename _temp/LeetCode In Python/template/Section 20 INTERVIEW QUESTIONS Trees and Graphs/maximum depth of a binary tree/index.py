# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ maxDepth root: TreeNode) -> int:
        __(root __ N..
            r_ 0
        __(root.left __ N.. and  root.right __ N..
            r_ 1
        
        left _ maxDepth(root.left)
        right _ maxDepth(root.right)

        r_ max(left,right)+1

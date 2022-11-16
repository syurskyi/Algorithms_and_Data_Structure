# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution:
    ans _ -float("inf")
    ___ solutionnode
        __(node __ N..
            r_ 0
        left _ solution(node.left)
        right _ solution(node.right)

        mxSide _ max(node.val,max(left,right)+node.val)
        mxTop _ max(mxSide,left+right+node.val)
        ans _ max(ans,mxTop)
        r_ mxSide

    ___ maxPathSum root: TreeNode) -> int:
        solution(root)
        r_ ans

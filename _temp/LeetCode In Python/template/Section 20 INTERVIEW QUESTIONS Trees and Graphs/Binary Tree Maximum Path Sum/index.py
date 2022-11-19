# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution
    ans _ -float("inf")
    ___ solutionnode
        __(node __ N..
            r_ 0
        left _ solution(node.left)
        right _ solution(node.right)

        mxSide _ m__(node.v..,m__(left,right)+node.v..)
        mxTop _ m__(mxSide,left+right+node.v..)
        ans _ m__(ans,mxTop)
        r_ mxSide

    ___ maxPathSum root: TreeNode) __ i..:
        solution(root)
        r_ ans

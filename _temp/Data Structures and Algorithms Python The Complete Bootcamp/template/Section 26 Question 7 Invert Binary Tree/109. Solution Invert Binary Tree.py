# Definition for a binary tree node.
c_ TreeNode:
    ___ -  val_0, left_None, right_None
        ? _ ?
        left _ left
        right _ right


c_ Solution
    ___ invertTree root
        __ root __ N..
            r_ N..

        root.left, root.right _ root.right, root.left

        invertTree(root.left)
        invertTree(root.right)

        r_ root
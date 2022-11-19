# Trim a Binary Search Tree
# Problem Statement
# Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the new
# tree are between min and max (inclusive). The resulting tree should still be a valid binary search tree.
# So, if we get this tree as input:
# title
# and we are given min value as 5 and max value as 13, then the resulting binary search tree should be:
# title
# We should remove all the nodes whose value is not between min and max.
# ** Feel free to reference the lecture on Binary Search Tree for the node class, but what it more important here is
# the logic of your function. In which case your function should be in the form:**
#
# # 669. Trim a Binary Search Tree
c_ Solution
    ___ trimBST root, min_val, max_val
        """
        :type root: TreeNode
        :type min_val: int
        :type max_val: int
        :rtype: TreeNode
        """
        __ n.. root:
            r_ N..
        __ root.v.. < min_val:
            r_ trimBST(root.right, min_val, max_val)
        __ root.v.. > max_val:
            r_ trimBST(root.left, min_val, max_val)
        root.left _ trimBST(root.left, min_val, max_val)
        root.right _ trimBST(root.right, min_val, max_val)
        r_ root

# ** There is no solution cell because the nature of the code should be more logical and a test would essentially give
# away the answer. Just focus your answer to fill out the logic of the solution using the methods described above **
# Best of luck!
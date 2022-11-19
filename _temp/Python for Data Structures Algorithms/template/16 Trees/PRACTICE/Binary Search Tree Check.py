# Binary Search Tree Check
# Problem Statement
# Given a binary tree, check whether its a binary search tree or not.
# ** Again, no solution cell, just worry about your code making sense logically. Hint: Think about tree traversals. **
# Solution
# Fill out your solution below:
# # Definition for a binary tree node.

c_ TreeNode o..
    ___ -  x
        val _ x
        left _ N..
        right _ N..

c_ Solution o..
    ___ isValidBST root
        r_ is_valid(root, -math.inf, math.inf)

    ___ is_valid root, min_val, max_val
        __ root __ N..
            r_ T..
        ____
            r_ ( root.val > min_val ___ root.val < max_val ___
                is_valid(root.left, min_val, root.val) ___
                is_valid(root.right, root.val, max_val) )

# This is a classic interview problem, so feel free to just Google search "Validate BST" for more information on this
# problem!
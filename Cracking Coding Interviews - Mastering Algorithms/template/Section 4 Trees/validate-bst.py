# c_ Node
# 	___ -  val, left_N.. right_N..
# 		? _ ?
# 		? _ ?
# 		? _ ?
#
# # Given a binary tree, determine if it is a valid binary search tree (BST).
#
# # 1. Everything on the left side needs to be less than the current node value
# # 2. Everything on the right side needs to be greater than the current node value
#
# # Example 1:
#
# # Input:
# #     2
# #    / \
# #   1   3
# # Output: true
# root1 _ Node(2, Node(1), Node(3))
#
#
# # Example 2:
#
# #     5
# #    / \
# #   1   4
# #      / \
# #     3   6
# # Output: false
# root2 _ Node(5, Node(1), Node(4, Node(3), Node(6)))
#
# ___ is_valid_bst_helper root, low, high
# 	__ ? __ N..
# 		r_ T..
# 	____ h.. !_ N.. ___ ?.v.. >_ h.. __ l.. !_ N.. ___ ?.v.. <_ l..
# 		r_ F..
#
# 	r_ ? ?.l.. l.. ?.v.. ___ ? ?.r.. ?.v.. h..
#
# ___ is_valid_bst root
# 	r_ ? ? N.., N..
#
# print(is_valid_bst(root1))
# print(is_valid_bst(root2))
#

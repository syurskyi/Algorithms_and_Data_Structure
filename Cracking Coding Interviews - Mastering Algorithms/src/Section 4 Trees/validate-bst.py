class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# Given a binary tree, determine if it is a valid binary search tree (BST).

# 1. Everything on the left side needs to be less than the current node value
# 2. Everything on the right side needs to be greater than the current node value

# Example 1:

# Input:
#     2
#    / \
#   1   3
# Output: true
root1 = Node(2, Node(1), Node(3))


# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
root2 = Node(5, Node(1), Node(4, Node(3), Node(6)))

def is_valid_bst_helper(root, low, high):
	if root == None:
		return True
	elif high != None and root.val >= high or low != None and root.val <= low:
		return False

	return is_valid_bst_helper(root.left, low, root.val) and is_valid_bst_helper(root.right, root.val, high)

def is_valid_bst(root):
	return is_valid_bst_helper(root, None, None)

print(is_valid_bst(root1))
print(is_valid_bst(root2))


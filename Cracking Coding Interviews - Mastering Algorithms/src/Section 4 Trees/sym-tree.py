class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# Given a binary tree, check whether it is a mirror of itself
# (ie, symmetric around its center).

# Example 1

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# => True

# Example 2

#   1
#  / \
# 2   2
#  \   \
#  3    3

# => False

def sym_tree_helper(root1, root2):
	if root1 == None and root2 == None:
		return True
	elif root1 == None or root2 == None:
		return False
	elif root1.val != root2.val:
		return False

	return sym_tree_helper(root1.right, root2.left) and sym_tree_helper(root1.left, root2.right)

def sym_tree(root):
	if root == None:
		return True

	return sym_tree_helper(root.left, root.right)

root1 = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))

print(sym_tree(root1))

root2 = Node(1, Node(2, None, Node(3)), Node(2, None, Node(3)))
print(sym_tree(root2))















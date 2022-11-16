c_ Node:
	___ -  val, left_None, right_None
		val _ val
		left _ left
		right _ right

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

___ sym_tree_helper(root1, root2
	__ root1 == N.. and root2 == N..:
		r_ True
	elif root1 == N.. or root2 == N..:
		r_ False
	elif root1.val !_ root2.val:
		r_ False

	r_ sym_tree_helper(root1.right, root2.left) and sym_tree_helper(root1.left, root2.right)

___ sym_tree(root
	__ root == N..:
		r_ True

	r_ sym_tree_helper(root.left, root.right)

root1 _ Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))

print(sym_tree(root1))

root2 _ Node(1, Node(2, N.., Node(3)), Node(2, N.., Node(3)))
print(sym_tree(root2))















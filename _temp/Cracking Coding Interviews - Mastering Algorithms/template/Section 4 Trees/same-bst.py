c_ Node:
	___ -  val, left_None, right_None
		val _ val
		left _ left
		right _ right

# Given two binary trees, write a function to check
# if they are the same or not.

# Two binary trees are considered the same if they are
# structurally identical and the nodes have the same value.


# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

# Output: true

root1 _ Node(1, Node(2), Node(3))
root2 _ Node(1, Node(2), Node(3))


# Example 2:

# Input:     1         1
#           /           \
#          2             2

# Output: false

root3 _ Node(1, Node(2), N..)
root4 _ Node(1, N.., Node(2))

# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

# Output: false

root5 _ Node(1, Node(2), Node(1))
root6 _ Node(1, Node(1), Node(2))

___ same_tree(root1, root2
	__ root1 __ N.. and root2 __ N..:
		r_ True
	elif root1 __ Node or root2 __ N..:
		r_ False
	elif root1.val !_ root2.val:
		r_ False

	r_ same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)


print(same_tree(root1, root2))
print(same_tree(root3, root4))
print(same_tree(root5, root6))










class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# Given two binary trees, write a function to check
# if they are the same or not.

# Two binary trees are considered the same if they are
# structurally identical and the nodes have the same value.


# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

# Output: true

root1 = Node(1, Node(2), Node(3))
root2 = Node(1, Node(2), Node(3))


# Example 2:

# Input:     1         1
#           /           \
#          2             2

# Output: false

root3 = Node(1, Node(2), None)
root4 = Node(1, None, Node(2))

# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

# Output: false

root5 = Node(1, Node(2), Node(1))
root6 = Node(1, Node(1), Node(2))

def same_tree(root1, root2):
	if root1 == None and root2 == None:
		return True
	elif root1 == Node or root2 == None:
		return False
	elif root1.val != root2.val:
		return False

	return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)


print(same_tree(root1, root2))
print(same_tree(root3, root4))
print(same_tree(root5, root6))










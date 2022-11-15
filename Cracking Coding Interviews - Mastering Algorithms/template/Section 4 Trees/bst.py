class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def inorder(root):
	if root == None:
		return

	inorder(root.left)
	print(root.val)
	inorder(root.right)


#               15
#            /      \
#        10          32
#       /  \         /  \
#     1      12     17   39
#      \    /  \         /
#       5  11  14      37
#      / \
#     4   7


leaf1 = Node(4)
leaf2 = Node(7)

leaf3 = Node(11)
leaf4 = Node(14)

leaf5 = Node(37)

leaf6 = Node(17)

node1 = Node(5, leaf1, leaf2)
node2 = Node(12, leaf3, leaf4)
node3 = Node(39, leaf5, None)

node4 = Node(32, leaf6, node3)

node5 = Node(1, None, node1)

node6 = Node(10, node5, node2)


root = Node(15, node6, node4)

inorder(root)

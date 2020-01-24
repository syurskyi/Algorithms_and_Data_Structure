# Definition for a binary tree node.
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def convert(root):
	if root == None:
		return None
	elif root.left == None and root.right == None:
		return [root, root]

	left = convert(root.left)
	right = convert(root.right)

	out = [None, None]

	if left != None:
		left[1].right = root
		root.left = left[1]

		out[0] = left[0]
	else:
		out[0] = root

	if right != None:
		right[0].left = root
		root.right = right[0]

		out[1] = right[1]
	else:
		out[1] = root

	return out

#               15
#            /      \
#        10          32
#       /  \         /  \
#     1      12     17   39
#      \    /  \         /
#       5  11  14      37
#      / \
#     4   7

# Output:
# <-1 <-> 4 <-> 5 <-> 7 <-> 10 <-> 11 <-> 12 <-> 14 <-> 15 <-> 17 <-> 32 <-> 37 <-> 39->

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


output = convert(root)

head = output[0]

while head:
	print(head.val)
	head = head.right

print("==============")

tail = output[1]

while tail:
	print(tail.val)
	tail = tail.left

















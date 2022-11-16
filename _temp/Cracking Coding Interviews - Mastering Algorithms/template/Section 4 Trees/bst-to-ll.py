# Definition for a binary tree node.
c_ Node:
	___ -  val, left_None, right_None
		val _ val
		left _ left
		right _ right

___ convert(root
	__ root __ N..:
		r_ N..
	elif root.left __ N.. and root.right __ N..:
		r_ [root, root]

	left _ convert(root.left)
	right _ convert(root.right)

	out _ [N.., N..]

	__ left !_ N..:
		left[1].right _ root
		root.left _ left[1]

		out[0] _ left[0]
	____
		out[0] _ root

	__ right !_ N..:
		right[0].left _ root
		root.right _ right[0]

		out[1] _ right[1]
	____
		out[1] _ root

	r_ out

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

leaf1 _ Node(4)
leaf2 _ Node(7)

leaf3 _ Node(11)
leaf4 _ Node(14)

leaf5 _ Node(37)

leaf6 _ Node(17)

node1 _ Node(5, leaf1, leaf2)
node2 _ Node(12, leaf3, leaf4)
node3 _ Node(39, leaf5, N..)

node4 _ Node(32, leaf6, node3)

node5 _ Node(1, N.., node1)

node6 _ Node(10, node5, node2)


root _ Node(15, node6, node4)


output _ convert(root)

head _ output[0]

_____ head:
	print(head.val)
	head _ head.right

print("==============")

tail _ output[1]

_____ tail:
	print(tail.val)
	tail _ tail.left

















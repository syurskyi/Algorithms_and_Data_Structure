c_ Node:
	___ -  val, left_None, right_None
		val _ val
		left _ left
		right _ right


___ search(root, target
	__ root __ N..:
		r_ N..
	____ root.val __ target:
		r_ root
	____ root.val < target:
		r_ search(root.right, target)
	____
		r_ search(root.left, target)

# runtime: O(logn)

#               15
#            /      \
#        10          32
#       /  \         /  \
#     1      12     17   39
#      \    /  \         /
#       5  11  14      37
#      / \
#     4   7


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

print(search(root, 37).val)
print(search(root, 40))

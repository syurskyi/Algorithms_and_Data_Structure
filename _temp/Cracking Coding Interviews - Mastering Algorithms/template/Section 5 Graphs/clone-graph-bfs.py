# c_ Node
# 	___ -  val, neighbors
# 		? _ ?
# 		? _ ?
#
# # Example Input:
#
# # 1 <---> 2
# # ^       ^
# # |       |
# # v       v
# # 4 <---> 3
#
# # Example Output:
#
# # 1 <---> 2
# # ^       ^
# # |       |
# # v       v
# # 4 <---> 3
#
# ___ clone node
# 	queue _    # list
#
# 	visited _     # dict
#
# 	?.a.. ?
#
# 	_____ l.. ? > 0
# 		cur _ ?.p.. 0
#
# 		new_node _ N..
#
# 		__ c.. __ v__.k..
# 			new_node _ ? ?
# 		____
# 			new_node _ ? ?.v..    # list)
#
# 		n.. _ ?.n..
#
# 		v.. ? _ ?
#
# 		___ i __ r.. l.. ?.n..
# 			__ ?.n.. ? __ v__.k..
# 				n__.a.. v.. ?.n.. ?
# 			____
# 				q__.a..(?.n.. ?
# 				new_neighbor_node _ ? ?.n.. ?.v..    # list)
# 				n__.a.. ?
# 				v.. ?.n.. ? _ ?
#
# 	r_ v.. ?
#
#
#
#
# node _ Node(1,    # list)
# node2 _ Node(2,    # list)
# node3 _ Node(3,    # list)
# node4 _ Node(4,    # list)
#
# ?.neighbors.a..(node2)
# ?.neighbors.a..(node4)
#
# node2.neighbors.a..(node)
# node2.neighbors.a..(node3)
#
# node3.neighbors.a..(node2)
# node3.neighbors.a..(node4)
#
# node4.neighbors.a..(node)
# node4.neighbors.a..(node3)

c_ Node:
	___ -  val, neighbors
		val _ val
		neighbors _ neighbors

# Example Input:

# 1 <---> 2
# ^       ^
# |       |
# v       v
# 4 <---> 3

# Example Output:

# 1 <---> 2
# ^       ^
# |       |
# v       v
# 4 <---> 3

___ clone(node
	queue _    # list

	visited _ {}

	queue.a..(node)

	_____ l..(queue) > 0:
		cur _ queue.pop(0)

		new_node _ N..

		__ cur __ visited.keys(
			new_node _ visited[cur]
		____
			new_node _ Node(cur.val,    # list)

		neighbors _ new_node.neighbors

		visited[cur] _ new_node

		___ i __ r..(l..(cur.neighbors
			__ cur.neighbors[i] __ visited.keys(
				neighbors.a..(visited[cur.neighbors[i]])
			____
				queue.a..(cur.neighbors[i])
				new_neighbor_node _ Node(cur.neighbors[i].val,    # list)
				neighbors.a..(new_neighbor_node)
				visited[cur.neighbors[i]] _ new_neighbor_node

	r_ visited[node]




node _ Node(1,    # list)
node2 _ Node(2,    # list)
node3 _ Node(3,    # list)
node4 _ Node(4,    # list)

node.neighbors.a..(node2)
node.neighbors.a..(node4)

node2.neighbors.a..(node)
node2.neighbors.a..(node3)

node3.neighbors.a..(node2)
node3.neighbors.a..(node4)

node4.neighbors.a..(node)
node4.neighbors.a..(node3)

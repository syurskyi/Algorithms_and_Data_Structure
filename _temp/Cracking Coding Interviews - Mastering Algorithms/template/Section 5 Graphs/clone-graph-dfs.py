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

# Visited nodes as we traverse
# DFS - Depth First Search
# apply 001_recursion

___ clone_helper(node, visited
	__ node __ N..
		r_ N..
	____ node __ visited.keys(
		r_ visited[node]

	neighbors _    # list
	new_node _ Node(node.val, neighbors)

	visited[node] _ new_node

	___ i __ r..(l..(node.neighbors
		neighbor_node _ clone_helper(node.neighbors[i], visited)
		neighbors.a..(neighbor_node)

	r_ new_node

___ clone(node
	r_ clone_helper(node, dict())


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

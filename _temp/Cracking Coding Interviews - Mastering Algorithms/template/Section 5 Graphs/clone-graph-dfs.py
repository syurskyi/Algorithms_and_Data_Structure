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
	__ node == N..:
		r_ N..
	elif node __ visited.keys(
		r_ visited[node]

	neighbors _ []
	new_node _ Node(node.val, neighbors)

	visited[node] _ new_node

	___ i __ range(len(node.neighbors)):
		neighbor_node _ clone_helper(node.neighbors[i], visited)
		neighbors.append(neighbor_node)

	r_ new_node

___ clone(node
	r_ clone_helper(node, dict())


node _ Node(1, [])
node2 _ Node(2, [])
node3 _ Node(3, [])
node4 _ Node(4, [])

node.neighbors.append(node2)
node.neighbors.append(node4)

node2.neighbors.append(node)
node2.neighbors.append(node3)

node3.neighbors.append(node2)
node3.neighbors.append(node4)

node4.neighbors.append(node)
node4.neighbors.append(node3)

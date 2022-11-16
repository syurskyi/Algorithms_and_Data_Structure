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
	queue _ []

	visited _ {}

	queue.append(node)

	_____ len(queue) > 0:
		cur _ queue.pop(0)

		new_node _ N..

		__ cur __ visited.keys(
			new_node _ visited[cur]
		____
			new_node _ Node(cur.val, [])

		neighbors _ new_node.neighbors

		visited[cur] _ new_node

		___ i __ range(len(cur.neighbors)):
			__ cur.neighbors[i] __ visited.keys(
				neighbors.append(visited[cur.neighbors[i]])
			____
				queue.append(cur.neighbors[i])
				new_neighbor_node _ Node(cur.neighbors[i].val, [])
				neighbors.append(new_neighbor_node)
				visited[cur.neighbors[i]] _ new_neighbor_node

	r_ visited[node]




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

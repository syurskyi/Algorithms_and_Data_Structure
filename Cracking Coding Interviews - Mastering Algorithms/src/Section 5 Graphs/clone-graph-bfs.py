class Node:
	def __init__(self, val, neighbors):
		self.val = val
		self.neighbors = neighbors

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

def clone(node):
	queue = []

	visited = {}

	queue.append(node)

	while len(queue) > 0:
		cur = queue.pop(0)

		new_node = None

		if cur in visited.keys():
			new_node = visited[cur]
		else:
			new_node = Node(cur.val, [])

		neighbors = new_node.neighbors

		visited[cur] = new_node

		for i in range(len(cur.neighbors)):
			if cur.neighbors[i] in visited.keys():
				neighbors.append(visited[cur.neighbors[i]])
			else:
				queue.append(cur.neighbors[i])
				new_neighbor_node = Node(cur.neighbors[i].val, [])
				neighbors.append(new_neighbor_node)
				visited[cur.neighbors[i]] = new_neighbor_node

	return visited[node]




node = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [])

node.neighbors.append(node2)
node.neighbors.append(node4)

node2.neighbors.append(node)
node2.neighbors.append(node3)

node3.neighbors.append(node2)
node3.neighbors.append(node4)

node4.neighbors.append(node)
node4.neighbors.append(node3)

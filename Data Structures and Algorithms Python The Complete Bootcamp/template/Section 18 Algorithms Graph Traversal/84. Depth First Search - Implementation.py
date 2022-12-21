c_ Node():

    ___  -  value):
        value = value
        adjacentlist   # list
        visited = False


c_ Graph():

    ___ DFS  node, traversal):
        node.visited = True
        traversal.a.. node.value)

        ___ element __ node.adjacentlist:
            __ element.visited __ False:
                DFS(element, traversal)

        r_ traversal


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

node1.adjacentlist.a.. node2)
node1.adjacentlist.a.. node3)
node1.adjacentlist.a.. node4)
node2.adjacentlist.a.. node5)
node2.adjacentlist.a.. node6)
node4.adjacentlist.a.. node7)
node6.adjacentlist.a.. node8)

graph = Graph()
print(graph.DFS(node1, []))
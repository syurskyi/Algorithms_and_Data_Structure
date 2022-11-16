c_ Node(

    ___ -  value
        value _ value
        adjacentlist _ []
        visited _ False


c_ Graph(

    ___ DFS node, traversal
        node.visited _ True
        traversal.append(node.value)

        ___ element __ node.adjacentlist:
            __ element.visited __ False:
                DFS(element, traversal)

        r_ traversal


node1 _ Node("A")
node2 _ Node("B")
node3 _ Node("C")
node4 _ Node("D")
node5 _ Node("E")
node6 _ Node("F")
node7 _ Node("G")
node8 _ Node("H")

node1.adjacentlist.append(node2)
node1.adjacentlist.append(node3)
node1.adjacentlist.append(node4)
node2.adjacentlist.append(node5)
node2.adjacentlist.append(node6)
node4.adjacentlist.append(node7)
node6.adjacentlist.append(node8)

graph _ Graph()
print(graph.DFS(node1, []))
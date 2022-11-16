c_ Node(

    ___ -  value
        value _ value
        adjacentlist _    # list
        visited _ False


c_ Graph(

    ___ DFS node, traversal
        node.visited _ True
        traversal.a..(node.value)

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

node1.adjacentlist.a..(node2)
node1.adjacentlist.a..(node3)
node1.adjacentlist.a..(node4)
node2.adjacentlist.a..(node5)
node2.adjacentlist.a..(node6)
node4.adjacentlist.a..(node7)
node6.adjacentlist.a..(node8)

graph _ Graph()
print(graph.DFS(node1,    # list))
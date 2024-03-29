c_ Node(

    ___ -  value
        ? _ ?
        adjacentlist _    # list
        visited _ F..


c_ Graph(

    ___ BFS node

        queue _    # list
        queue.a..(node)
        ?.visited _ T..

        traversal _    # list

        _____ queue:
            actualNode _ queue.p.. 0)
            traversal.a..(actualNode.value)

            ___ element __ actualNode.adjacentlist:
                __ element.visited __ F..:
                    queue.a..(element)
                    element.visited _ T..

        r_ traversal


node1 _ Node("A")
node2 _ Node("B")
node3 _ Node("C")
node4 _ Node("D")
node5 _ Node("E")
node6 _ Node("F")
node7 _ Node("G")

node1.adjacentlist.a..(node2)
node1.adjacentlist.a..(node3)
node1.adjacentlist.a..(node4)
node2.adjacentlist.a..(node5)
node2.adjacentlist.a..(node6)
node4.adjacentlist.a..(node7)

graph _ Graph()
print(graph.BFS(node1))
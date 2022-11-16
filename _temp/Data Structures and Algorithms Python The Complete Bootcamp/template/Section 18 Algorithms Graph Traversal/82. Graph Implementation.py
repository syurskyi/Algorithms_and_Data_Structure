c_ Node(

    ___ -  value
        value _ value
        adjacentlist _ []
        visited _ False

c_ Graph(
    pass

node1 _ Node("A")
node2 _ Node("B")
node3 _ Node("C")
node4 _ Node("D")
node5 _ Node("E")
node6 _ Node("F")
node7 _ Node("G")

node1.adjacentlist.append(node2)
node1.adjacentlist.append(node3)
node1.adjacentlist.append(node4)
node2.adjacentlist.append(node5)
node2.adjacentlist.append(node6)
node4.adjacentlist.append(node7)
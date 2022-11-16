#!/usr/bin/python

c_ Node:
    ___ -  data
        l _ N..
        r _ N..
        v _ data

c_ binTree:
    ___ -  
        root _ N..

    ___ getRoot 
        r_ root

    ___ addnode data
        __(root __ N..
            root _ Node(data)
        ____
            _add(data, root)

    ___ _add data, node
        __(data < node.v
            __(node.l !_ N..
                _add(data, node.l)
            ____
                node.l _ Node(data)
        ____
            __(node.r !_ N..
                _add(data, node.r)
            ____
                node.r _ Node(data)

    ___ findnode data
        __(root !_ N..
            r_ _find(data, root)
        ____
            r_ N..

    ___ _find data, node
        __(data __ node.v
            r_ node
        ____(data < node.v ___ node.l !_ N..
            _find(data, node.l)
        ____(data > node.v ___ node.r !_ N..
            _find(data, node.r)

    ___ deleteTree 
        root _ N..

    ___ printFullTree 
        __(root !_ N..
            _printTree(root)

    ___ _printTree node
        __(node !_ N..
            _printTree(node.l)
            print str(node.v) + ' '
            _printTree(node.r)


___ maxNodeLoop(root
   __ n.. root:
      r_ 0
   _____ root.r !_ N..:
         root_root.r
   print root.v 
        


#     3
# 0     4
#   2      8
tree _ binTree()
tree.addnode(3)
tree.addnode(4)
tree.addnode(0)
tree.addnode(8)
tree.addnode(2)
tree.printFullTree()
print "max value is:"
maxNodeLoop(tree.root)

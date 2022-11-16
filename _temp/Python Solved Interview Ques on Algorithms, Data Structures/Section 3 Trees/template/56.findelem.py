#!/usr/bin/python

import Queue

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
        __(root == N..
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
        __(data == node.v
            r_ node
        elif(data < node.v and node.l !_ N..
            _find(data, node.l)
        elif(data > node.v and node.r !_ N..
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


___ findusingloops(root,data
  __ root __ N..:
     r_

  q _ Queue.Queue()
  q.put(root)

  node_None

  _____ n.. q.empty(
    node_q.get()

    __ data == node.v:
       print "node.v", node.v
       r_ 1

    __ node.l __ n.. N..:
       q.put(node.l)

    __ node.r __ n.. N..:
       q.put(node.r)
        
  r_ 0

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
__ findusingloops(tree.root, 8
   print "The data: 8 is found" 
____
   print "data not found"


#!/usr/bin/python

______ Queue

c_ Node
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
            root _ ? ?
        ____
            _add(data, root)

    ___ _add data, node
        __(data < ?.v
            __(?.l !_ N..
                _add(data, ?.l)
            ____
                ?.l _ ? ?
        ____
            __(?.r !_ N..
                _add(data, ?.r)
            ____
                ?.r _ ? ?

    ___ findnode data
        __(root !_ N..
            r_ _find(data, root)
        ____
            r_ N..

    ___ _find data, node
        __(data __ ?.v
            r_ node
        ____(data < ?.v ___ ?.l !_ N..
            _find(data, ?.l)
        ____(data > ?.v ___ ?.r !_ N..
            _find(data, ?.r)

    ___ deleteTree 
        root _ N..

    ___ printFullTree 
        __(root !_ N..
            _printTree(root)

    ___ _printTree node
        __(node !_ N..
            _printTree(?.l)
            print s..(?.v) + ' '
            _printTree(?.r)


___ maxusingloops(root
  __ root __ N..
     r_

  q _ Queue.Queue()
  q.put(root)

  node_None
  maxElem_0

  _____ n.. q.empty(
    node_q.get()

    __ maxElem < ?.v:
       maxElem_node.v

    __ ?.l __ n.. N..
       q.put(?.l)

    __ ?.r __ n.. N..
       q.put(?.r)
        
  print maxElem

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
print "maxelement:"
maxusingloops(tree.root)

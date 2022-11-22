#!/usr/bin/python

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
        __(data < node.v
            __(node.l !_ N..
                _add(data, node.l)
            ____
                node.l _ ? ?
        ____
            __(node.r !_ N..
                _add(data, node.r)
            ____
                node.r _ ? ?

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
            print s..(node.v) + ' '
            _printTree(node.r)



___ checkwhetheritsabintree(root
        __ root __ N..
                  r_ 1
        # false if left is > than root
        __ root.l !_ N.. ___ root.l.v > root.v:
                  r_ 0

        # false if right is < than root
        __ root.r !_ N.. ___ root.r.v < root.v:
                  r_ 0

        # false if, recursively, the left or right is not a BST
        __ n.. checkwhetheritsabintree(root.l) __ n.. checkwhetheritsabintree(root.r
                  r_ 0

        # passing all that, it's a BST
        r_ 1


___ levelOrder(root
    items _    # list
    count_0
    ?.i.. (count,root)
    elements _""
    _____ items !_    # list:
        temp _ ?.p.. 
        elements_ elements+s..(?.v)+ " "
        __ ?.l!_None:
            ?.i.. (0,?.l)
        __ ?.r!_None:
            ?.i.. (0,?.r)
    print "Level order traversal of BST: "+ elements


___ findsizeusingiteration(root
    items _    # list
    count_0
    ?.i.. (count,root)
    elements _""
    _____ items !_    # list:
        temp _ ?.p.. 
        ? +_ 1 
        __ ?.l!_None:
            ?.i.. (0,?.l)
        __ ?.r!_None:
            ?.i.. (0,?.r)
    print "size of the tree is : ", count



___ findsize(tree
       __ n.. tree:
          r_ 0
       r_ findsize(tree.l)+findsize(tree.r)+1

___ printReverse(root
    items _    # list
    count_0
    ?.i.. (count,root)
    elements _""
    _____ items !_    # list:
        temp _ ?.p.. 
        elements_ s..(?.v)+ " " + elements
        __ ?.l!_None:
            ?.i.. (0,?.l)
        __ ?.r!_None:
            ?.i.. (0,?.r)
    print "Level order traversal of BST: "+ elements


___ maximumDepthOfTree(root
        __ root __ N..
            r_ 0
        r_ m__(maximumDepthOfTree(root.l), maximumDepthOfTree(root.r)) + 1


___ deepestNode(root
    items _    # list
    count_0
    ?.i.. (count,root)
    elements _""
    _____ items !_    # list:
        temp _ ?.p.. 
        elements_ s..(?.v)+ " " + elements
        __ ?.l!_None:
            ?.i.. (0,?.l)
        __ ?.r!_None:
            ?.i.. (0,?.r)

    print "Deepest node is ",?.v


___ countLeaves(root
    items _    # list
    count_0
    ?.i.. (count,root)
    elements _""
    _____ items !_    # list:
        temp _ ?.p.. 
        __ ?.l __ N.. ___ ?.r __ N..
            ? +_ 1
        __ ?.l!_None:
            ?.i.. (0,?.l)
        __ ?.r!_None:
            ?.i.. (0,?.r)

    print "number of leafs in the tree ",count


___ countFullNodes(root
    items _    # list
    count_0
    ?.i.. (count,root)
    _____ items !_    # list:
        temp _ ?.p.. 
        __ ?.l __ n.. N.. ___ ?.r __ n.. N..
            ? +_ 1
        __ ?.l!_None:
            ?.i.. (0,?.l)
        __ ?.r!_None:
            ?.i.. (0,?.r)

    print "number of full nodes in the tree ",count



___ countHalfNodes(root
    items _    # list
    count_0
    ?.i.. (count,root)
    _____ items !_    # list:
        temp _ ?.p.. 
        __ (?.l __ N.. ___ ?.r __ n.. N..) __ \
                        (?.l __ n.. N.. ___ ?.r __ N..
            ? +_ 1
        __ ?.l!_None:
            ?.i.. (0,?.l)
        __ ?.r!_None:
            ?.i.. (0,?.r)

    print "number of half nodes in the tree ",count

ptr _ 0
___ diaTree(root
        global ptr
        __(n.. root) :
                r_ 0
        left _ diaTree(root.l);
        right _ diaTree(root.r);

        __(left + right > ptr
              ptr _ left + right
        r_ m__(left, right) + 1



___ appendpath(root, path, paths
        __ n.. root:
                r_ 0

        path.a..(root.v)
        print "PATH:",path
        paths.a..(path)
        print "PATHS:",paths
        appendpath(root.l, path + [root.v], paths)
        appendpath(root.r, path + [root.v], paths)


___ getthepathofeachnode(rootnode
    nodepaths _    # list
    appendpath(rootnode,    # list, nodepaths)
    print 'path of nodes:', nodepaths


___ getthepath(root, val, path, paths
    
    
    print "root", root
    print "root.data", root.v
    print "val", val
    print "path", path
    print "paths", paths

    __ n.. root:
        r_ F..

    __ n.. root.l ___ n.. root.r:
        __ root.v __ val:
            path.a..(root.v)
            paths.a..(path)
            r_ T..
        ____
            r_ F..

    left _ getthepath(root.l, val - root.v, path + [root.v], paths)
    right _ getthepath(root.r, val - root.v, path + [root.v], paths)
    r_ left __ right


___ checkwhetherpathhassum(root, val
    paths _    # list
    getthepath(root, val,    # list, paths)
    print 'sum:', val
    print 'paths:', paths


___ sumOfNodes(root
    items _    # list
    count_0
    ?.i.. (count,root)
    sum_0
    _____ items !_    # list:
        temp _ ?.p.. 
        sum +_ ?.v 
        __ ?.l!_None:
            ?.i.. (0,?.l)
        __ ?.r!_None:
            ?.i.. (0,?.r)
        ___ p __ items: print ?.v
        print "####"

    print "Total sum of all nodes is ",sum



#     3
# 0     4
#   2      8
tree _ binTree()
tree.addnode(3)
tree.addnode(4)
tree.addnode(0)
tree.addnode(-1)
tree.addnode(8)
tree.addnode(2)
tree.addnode(3.5)
tree.addnode(10)
tree.printFullTree()
deepestNode(tree.root)

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



___ checkwhetheritsabintree(root
        __ root == N..:
                  r_ 1
        # false if left is > than root
        __ root.l !_ N.. and root.l.v > root.v:
                  r_ 0

        # false if right is < than root
        __ root.r !_ N.. and root.r.v < root.v:
                  r_ 0

        # false if, recursively, the left or right is not a BST
        __ n.. checkwhetheritsabintree(root.l) or n.. checkwhetheritsabintree(root.r
                  r_ 0

        # passing all that, it's a BST
        r_ 1


___ levelOrder(root
    items _ []
    count_0
    items.insert(count,root)
    elements _""
    _____ items !_ []:
        temp _ items.pop()
        elements_ elements+str(temp.v)+ " "
        __ temp.l!_None:
            items.insert(0,temp.l)
        __ temp.r!_None:
            items.insert(0,temp.r)
    print "Level order traversal of BST: "+ elements


___ findsizeusingiteration(root
    items _ []
    count_0
    items.insert(count,root)
    elements _""
    _____ items !_ []:
        temp _ items.pop()
        count +_ 1
        __ temp.l!_None:
            items.insert(0,temp.l)
        __ temp.r!_None:
            items.insert(0,temp.r)
    print "size of the tree is : ", count



___ findsize(tree
       __ n.. tree:
          r_ 0
       r_ findsize(tree.l)+findsize(tree.r)+1

___ printReverse(root
    items _ []
    count_0
    items.insert(count,root)
    elements _""
    _____ items !_ []:
        temp _ items.pop()
        elements_ str(temp.v)+ " " + elements
        __ temp.l!_None:
            items.insert(0,temp.l)
        __ temp.r!_None:
            items.insert(0,temp.r)
    print "Level order traversal of BST: "+ elements


___ maximumDepthOfTree(root
        __ root == N..:
            r_ 0
        r_ max(maximumDepthOfTree(root.l), maximumDepthOfTree(root.r)) + 1


___ deepestNode(root
    items _ []
    count_0
    items.insert(count,root)
    elements _""
    _____ items !_ []:
        temp _ items.pop()
        elements_ str(temp.v)+ " " + elements
        __ temp.l!_None:
            items.insert(0,temp.l)
        __ temp.r!_None:
            items.insert(0,temp.r)
        ___ p __ items: print p.v
        print "####"

    print "Deepest node is ",temp.v


___ countLeaves(root
    items _ []
    count_0
    items.insert(count,root)
    elements _""
    _____ items !_ []:
        temp _ items.pop()
        __ temp.l __ N.. and temp.r __ N..:
            count +_ 1
        __ temp.l!_None:
            items.insert(0,temp.l)
        __ temp.r!_None:
            items.insert(0,temp.r)

    print "number of leafs in the tree ",count


___ countFullNodes(root
    items _ []
    count_0
    items.insert(count,root)
    _____ items !_ []:
        temp _ items.pop()
        __ temp.l __ n.. N.. and temp.r __ n.. N..:
            count +_ 1
        __ temp.l!_None:
            items.insert(0,temp.l)
        __ temp.r!_None:
            items.insert(0,temp.r)

    print "number of full nodes in the tree ",count


___ levelwithmaxsum(root
    items _ []
    count_0
    items.insert(count,root)
    items.insert(0,N..)
    level _ maxLevel _ currentSum _ maxSum _ 0
    _____ items !_ []:
        temp _ items.pop()
        __ (temp == N..
            __(currentSum > maxSum
                 maxSum _ currentSum
                 maxLevel _ level
                 currentSum _ 0
                 # place the indicator for end of next level at the end of queue
                 __ items !_ [] :
                    items.insert(0,N..)
                    level +_ 1
        ____
            currentSum +_ temp.v
            __ temp.l!_None:
               items.insert(0,temp.l)
            __ temp.r!_None:
               items.insert(0,temp.r)

    print "level with max sum is",level
    print "max sum is",maxSum




___ countHalfNodes(root
    items _ []
    count_0
    items.insert(count,root)
    _____ items !_ []:
        temp _ items.pop()
        __ (temp.l __ N.. and temp.r __ n.. N..) or \
                        (temp.l __ n.. N.. and temp.r __ N..
            count +_ 1
        __ temp.l!_None:
            items.insert(0,temp.l)
        __ temp.r!_None:
            items.insert(0,temp.r)

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
        r_ max(left, right) + 1



___ appendpath(root, path, paths
        __ n.. root:
                r_ 0

        path.append(root.v)
        print "PATH:",path
        paths.append(path)
        print "PATHS:",paths
        appendpath(root.l, path + [root.v], paths)
        appendpath(root.r, path + [root.v], paths)


___ getthepathofeachnode(rootnode
    nodepaths _ []
    appendpath(rootnode, [], nodepaths)
    print 'path of nodes:', nodepaths


___ getthepath(root, val, path, paths
    
    
    print "root", root
    print "root.data", root.v
    print "val", val
    print "path", path
    print "paths", paths

    __ n.. root:
        r_ False

    __ n.. root.l and n.. root.r:
        __ root.v == val:
            path.append(root.v)
            paths.append(path)
            r_ True
        ____
            r_ False

    left _ getthepath(root.l, val - root.v, path + [root.v], paths)
    right _ getthepath(root.r, val - root.v, path + [root.v], paths)
    r_ left or right


___ checkwhetherpathhassum(root, val
    paths _ []
    getthepath(root, val, [], paths)
    print 'sum:', val
    print 'paths:', paths


___ sumOfNodes(root
    items _ []
    count_0
    items.insert(count,root)
    sum_0
    _____ items !_ []:
        temp _ items.pop()
        sum +_ temp.v
        __ temp.l!_None:
            items.insert(0,temp.l)
        __ temp.r!_None:
            items.insert(0,temp.r)
        ___ p __ items: print p.v
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
tree.printFullTree()
levelwithmaxsum(tree.root)

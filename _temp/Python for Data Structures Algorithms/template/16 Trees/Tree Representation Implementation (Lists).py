# Tree Representation Implementation (Lists)
#
# Below is a representation of a Tree using a list of lists. Refer to the video lecture for an explanation and
# a live coding demonstration!

___ BinaryTree(r
    r_ [r,    # list, []]

___ insertLeft(root,newBranch
    t _ root.p.. 1)
    __ l..(t) > 1:
        root.i.. (1,[newBranch,t,[]])
    ____
        root.i.. (1,[newBranch,    # list, []])
    r_ root

___ insertRight(root,newBranch
    t _ root.p.. 2)
    __ l..(t) > 1:
        root.i.. (2,[newBranch,   # list,t])
    ____
        root.i.. (2,[newBranch,   # list,[]])
    r_ root

___ getRootVal(root
    r_ root[0]

___ setRootVal(root,newVal
    root[0] _ newVal

___ getLeftChild(root
    r_ root[1]

___ getRightChild(root
    r_ root[2]
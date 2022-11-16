# Tree Representation Implementation (Lists)
#
# Below is a representation of a Tree using a list of lists. Refer to the video lecture for an explanation and
# a live coding demonstration!

___ BinaryTree(r
    r_ [r, [], []]

___ insertLeft(root,newBranch
    t _ root.pop(1)
    __ len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    ____
        root.insert(1,[newBranch, [], []])
    r_ root

___ insertRight(root,newBranch
    t _ root.pop(2)
    __ len(t) > 1:
        root.insert(2,[newBranch,[],t])
    ____
        root.insert(2,[newBranch,[],[]])
    r_ root

___ getRootVal(root
    r_ root[0]

___ setRootVal(root,newVal
    root[0] _ newVal

___ getLeftChild(root
    r_ root[1]

___ getRightChild(root
    r_ root[2]
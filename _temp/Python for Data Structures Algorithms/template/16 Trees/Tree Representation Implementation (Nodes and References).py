# Nodes and References Implementation of a Tree
#
# In this notebook is the code corresponding to the lecture for implementing the representation of a Tree as a class with nodes and references!

c_ BinaryTree o..
    ___ - rootObj
        key _ rootObj
        leftChild _ N..
        rightChild _ N..

    ___ insertLeftnewNode
        __ leftChild == N..:
            leftChild _ BinaryTree(newNode)
        ____
            t _ BinaryTree(newNode)
            t.leftChild _ leftChild
            leftChild _ t

    ___ insertRightnewNode
        __ rightChild == N..:
            rightChild _ BinaryTree(newNode)
        ____
            t _ BinaryTree(newNode)
            t.rightChild _ rightChild
            rightChild _ t


    ___ getRightChild
        r_ rightChild

    ___ getLeftChild
        r_ leftChild

    ___ setRootValobj
        key _ obj

    ___ getRootVal
        r_ key

# We can see some examples of creating a tree and assigning children. Note that some outputs are Trees themselves!
#
from __future__ import print_function
#
r _ BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

# a
# None
# <__main__.BinaryTree object at 0x104779c10>
# b
# <__main__.BinaryTree object at 0x103b42c50>
# c
# hello
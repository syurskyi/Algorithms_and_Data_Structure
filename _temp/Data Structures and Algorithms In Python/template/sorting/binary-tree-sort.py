# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ Node:
    ___ - value
        info _ value
        lchild _ N..
        rchild _ N..

c_ BinarySearchTree:
    ___ -
        root _ N..
    
    ___ is_empty
        r_ root == N..
           
    ___ insertx
        root _ _insert(root, x)
                 
    ___ _insertp, x
        __ p __ N..:
            p _ Node(x)
        elif x < p.info :
            p.lchild _ _insert(p.lchild, x)
        ____
            p.rchild _ _insert(p.rchild, x)
        r_ p

    ___ inorder
        _inorder(root)
        print()

    ___ _inorder p
        __ p __ N.. :
            r_
        _inorder(p.lchild)
        print(p.info, " ")
        _inorder(p.rchild)

    
####################################
n _ int(input("Enter the number of elements to be sorted : "))

tree _ BinarySearchTree()
___ i __ range(n
    x _ int(input("Enter element : "))
    tree.insert(x)
    
tree.inorder()  

####################################


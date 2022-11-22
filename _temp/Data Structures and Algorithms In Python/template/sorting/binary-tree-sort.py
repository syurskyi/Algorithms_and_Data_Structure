# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ Node
    ___ - value
        info _ value
        lchild _ N..
        rchild _ N..

c_ BinarySearchTree:
    ___ -
        root _ N..
    
    ___ is_empty
        r_ root __ N..
           
    ___ insertx
        root _ _insert(root, x)
                 
    ___ _insertp, x
        __ p __ N..
            p _ Node(x)
        ____ x < ?.i.. :
            ?.lchild _ _insert(?.lchild, x)
        ____
            ?.rchild _ _insert(?.rchild, x)
        r_ p

    ___ inorder
        _inorder(root)
        print()

    ___ _inorder p
        __ p __ N.. :
            r_
        _inorder(?.lchild)
        print(?.i.., " ")
        _inorder(?.rchild)

    
####################################
n _ i..(i..("Enter the number of elements to be sorted : "))

tree _ BinarySearchTree()
___ i __ r..(n
    x _ i..(i..("Enter element : "))
    tree.i.. (x)
    
tree.inorder()  

####################################


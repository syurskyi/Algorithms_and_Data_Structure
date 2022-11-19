# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

from collections import deque

c_ Node:
    ___ - value
        info _ value
        lchild _ N..
        rchild _ N..

c_ BinaryTree:
    ___ -  
        root _ N..
    
    ___ is_empty 
        r_ root __ N..
        
    ___ display 
        _display(root,0)
        print()
        
    ___ _displayp,level
        __ p __ N..:
            r_
        _display(?.rchild, level+1)
        print()

        ___ i __ r..(level
            print("    ", end_'')
        print(?.i..)
        _display(?.lchild, level+1)
        
    ___ preorder 
        _preorder(root)
        print()
    
    ___ _preorderp
        __ p __ N..:
            r_
        print(?.i.., " ", end _'')
        _preorder(?.lchild)
        _preorder(?.rchild)
        
    ___ inorder 
        _inorder(root)
        print()

    ___ _inorder p
        __ p __ N.. :
            r_
        _inorder(?.lchild)
        print(?.i.., " ", end _'')
        _inorder(?.rchild)

    ___ postorder 
        _postorder(root)
        print() 
         
    ___ _postorder p
        __ p __ N..:
            r_
        _postorder(?.lchild)
        _postorder(?.rchild)
        print(?.i.., " ", end _'')

    ___ level_order 
        __ root __ N..:
            print("Tree is empty")
            r_
              	     
        qu _ deque()
        qu.a..(root)

        _____ l..(qu)!_0:
            p _ qu.popleft()
            print(?.i.. + " ",end_'')
            __ ?.lchild __ n.. N..:
                qu.a..(?.lchild)
            __ ?.rchild __ n.. N..:
                qu.a..(?.rchild)
    	     
    
    ___ height 
        r_ _height(root)

    ___ _heightp
        __ p __ N..:
            r_ 0

        hL _ _height(?.lchild)
        hR _ _height(?.rchild)

        __ hL > hR:
            r_ 1 + hL
        ____
            r_ 1 + hR

    ___ create_tree 
        root _ Node('P')
        root.lchild _ Node('Q')
        root.rchild _ Node('R')
        root.lchild.lchild _ Node('A')
        root.lchild.rchild _ Node('B')
        root.rchild.lchild _ Node('X')
     
        
#################################################################            
bt _ BinaryTree()

bt.create_tree() 

bt.display() 
print() 

print("Preorder : ") 
bt.preorder()  
print("") 

print("Inorder : ") 
bt.inorder() 
print() 

print("Postorder : ") 
bt.postorder() 
print() 

print("Level order : ") 
bt.level_order() 
print() 

print("Height of tree is " , bt.height())


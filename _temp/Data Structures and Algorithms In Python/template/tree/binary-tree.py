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
        r_ root == N..
        
    ___ display 
        _display(root,0)
        print()
        
    ___ _displayp,level
        __ p __ N..:
            r_
        _display(p.rchild, level+1)
        print()

        ___ i __ range(level
            print("    ", end_'')
        print(p.info)
        _display(p.lchild, level+1)
        
    ___ preorder 
        _preorder(root)
        print()
    
    ___ _preorderp
        __ p __ N..:
            r_
        print(p.info, " ", end _'')
        _preorder(p.lchild)
        _preorder(p.rchild)
        
    ___ inorder 
        _inorder(root)
        print()

    ___ _inorder p
        __ p __ N.. :
            r_
        _inorder(p.lchild)
        print(p.info, " ", end _'')
        _inorder(p.rchild)

    ___ postorder 
        _postorder(root)
        print() 
         
    ___ _postorder p
        __ p __ N..:
            r_
        _postorder(p.lchild)
        _postorder(p.rchild)
        print(p.info, " ", end _'')

    ___ level_order 
        __ root __ N..:
            print("Tree is empty")
            r_
              	     
        qu _ deque()
        qu.append(root)

        _____ len(qu)!_0:
            p _ qu.popleft()
            print(p.info + " ",end_'')
            __ p.lchild __ n.. N..:
                qu.append(p.lchild)
            __ p.rchild __ n.. N..:
                qu.append(p.rchild)
    	     
    
    ___ height 
        r_ _height(root)

    ___ _heightp
        __ p __ N..:
            r_ 0

        hL _ _height(p.lchild)
        hR _ _height(p.rchild)

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


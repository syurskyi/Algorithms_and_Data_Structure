# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

c_ TreeEmptyError E..
    p..

c_ Node:
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
        __ p __ N..:
            p _ Node(x)
        ____ x < p.info :
            p.lchild _ _insert(p.lchild, x) 
        ____ x > p.info :
            p.rchild _ _insert(p.rchild, x)   
        ____
            print(x, " already present in the tree") 
        r_ p

    ___ insert1x
        p _ root
        par _ N..
        _____ p __ n.. N..:
            par _ p
            __ x < p.info :
                p _ p.lchild
            ____ x > p.info:
                p _ p.rchild
            ____
                print(x, " already present in the tree")
                r_

        temp _ Node(x) 

        __ par __ N..:
            root _ temp 
        ____ x < par.info:
            par.lchild _ temp 
        ____
            par.rchild _ temp 

    ___ searchx
        r_ _search(root, x) __ n.. N..

    ___ _search p, x
        __ p __ N..:
            r_ N..  # key not found
        __ x < p.info: # search in left subtree
            r_ _search(p.lchild, x) 
        __ x > p.info: # search in right subtree
            r_ _search(p.rchild, x) 
        r_ p  # key found

    ___ search1x
        p _ root 
        _____ p __ n.. N..:
            __ x < p.info :
                p _ p.lchild  # Move to left child
            ____ x > p.info:
                p _ p.rchild  # Move to right child 
            ____   # x found
                r_ true 
        r_ false 

    ___ deletex
        root _ _delete(root, x) 

    ___ _delete p, x
        __ p __ N..:
            print(x , "  not found")
            r_ p 
         
        __ x < p.info:  # delete from left subtree
            p.lchild _ _delete(p.lchild, x) 
        ____ x > p.info: # delete from right subtree
            p.rchild _ _delete(p.rchild, x)
        ____
            # key to be deleted is found
            __ p.lchild __ n.. N..  ___ p.rchild __ n.. N..:  # 2 children
                s _ p.rchild
                _____ s.lchild __ n.. N..:
                    s _ s.lchild
                p.info _ s.info
                p.rchild _ _delete(p.rchild,s.info) 
                 
            ____   # 1 child or no child
                __ p.lchild __ n.. N..: # only left child
                    ch _ p.lchild
                ____  # only right child or no child 
                     ch _ p.rchild
                p _ ch 
        r_ p  

    ___ delete1x
        p _ root
        par _ N..

        _____ p __ n.. N..:
            __ x __ p.info:
                b..
            par _ p
            __ x < p.info:
                p _ p.lchild
            ____
                p _ p.rchild
            
        __ p __ N..:
            print(x , " not found")
            r_

        # Case C: 2 children 
        # Find inorder successor and its parent 

        __ p.lchild __ n.. N.. ___ p.rchild __ n.. N..:
            ps _ p
            s _ p.rchild

            _____ s.lchild __ n.. N..:
                ps _ s
                s _ s.lchild
            p.info _ s.info  
            p _ s 
            par _ ps 
                    
        # Case B and Case A : 1 or no child 
        __ p.lchild __ n.. N..: # node to be deleted has left child
            ch _ p.lchild 
        ____                # node to be deleted has right child or no child
            ch _ p.rchild

        __ par __ N..:   # node to be deleted is root node
            root _ ch
        ____ p __ par.lchild: # node is left child of its parent
            par.lchild _ ch
        ____       # node is right child of its parent
            par.rchild _ ch 
     

    ___ min1 
        __ is_empty(
            r... TreeEmptyError("Tree is empty")
        p _ root 
        _____ p.lchild __ n.. N..:
            p _ p.lchild 
        r_ p.info
    
    ___ max1 
        __ is_empty(
            r... TreeEmptyError("Tree is empty")
        p _ root 
        _____ p.rchild __ n.. N..:
            p _ p.rchild 
        r_ p.info
    
    ___ min2 
        __ is_empty(
            r... TreeEmptyError("Tree is empty")
        r_ _min(root).info 

    ___ _minp
        __ p.lchild __ N..:
            r_ p 
        r_ _min(p.lchild) 

    ___ max2 
        __ is_empty(
           r... TreeEmptyError("Tree is empty")
        r_ _max(root).info 

    ___ _maxp
        __ p.rchild __ N..:
            r_ p 
        r_ _max(p.rchild) 

    ___ display 
        _display(root,0)
        print()
        
    ___ _displayp,level
        __ p __ N..:
            r_
        _display(p.rchild, level+1)
        print()

        ___ i __ r..(level
            print("    ", end_'')
        print(p.info)
        _display(p.lchild, level+1) 
        
    ___ preorder 
        _preorder(root)
        print()
    
    ___ _preorderp
        __ p __ N..:
            r_
        print(p.info, " ")
        _preorder(p.lchild)
        _preorder(p.rchild) 
        
    ___ inorder 
        _inorder(root)
        print()

    ___ _inorder p
        __ p __ N.. :
            r_
        _inorder(p.lchild)
        print(p.info, " ")
        _inorder(p.rchild) 

    ___ postorder 
        _postorder(root)
        print() 
 
    ___ _postorder p
        __ p __ N..:
            r_
        _postorder(p.lchild)
        _postorder(p.rchild) 
        print(p.info , " ") 

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

##############################################################################################
            
bst _ BinarySearchTree()

_____ T..:
    print("1.Display Tree") 
    print("2.Search(Iterative)")
    print("3.Search(Recursive)")
    print("4.Insert a new node(Iterative)") 
    print("5.Insert a new node(Recursive)") 
    print("6.Delete a node(Iterative)")
    print("7.Delete a node(Recursive)") 
    print("8.Find Minimum key(Iterative)")
    print("9.Find Minimum key(Recursive)") 
    print("10.Find Maximum key(Iterative)")
    print("11.Find Maximum key(Recursive)") 
    print("12.Preorder Traversal") 
    print("13.Inorder Traversal") 
    print("14.Postorder Traversal") 
    print("15.Height of tree")
    print("16.Quit")
    choice _ i..(i..("Enter your choice : "))
    
    __ choice __ 1:
        bst.display()
    ____ choice __ 2:
        x _ i..(i..("Enter the key to be searched : "))
        __ bst.search1(x
            print("Key found")
        ____
            print("Key not found")
    ____ choice __ 3:
        x _ i..(i..("Enter the key to be searched : "))
        __ bst.search(x
            print("Key found")
        ____
            print("Key not found")
    ____ choice __ 4:
        x _ i..(i..("Enter the key to be inserted : "))
        bst.insert1(x)
    ____ choice __ 5:
        x _ i..(i..("Enter the key to be inserted : "))
        bst.i.. (x)
    ____ choice __ 6:
        x _ i..(i..("Enter the element to be deleted : ")) 
        bst.delete1(x)
    ____ choice __ 7:
        x _ i..(i..("Enter the element to be deleted : ")) 
        bst.delete(x)
    ____ choice __ 8:
        print("Minimum key is " , bst.min1())
    ____ choice __ 9:
        print("Minimum key is " , bst.min2())
    ____ choice __ 10:
        print("Maximum key is " , bst.max1())
    ____ choice __ 11:
        print("Maximum key is " , bst.max2())
    ____ choice __ 12:
        bst.preorder()
    ____ choice __ 13:
        bst.inorder()
    ____ choice __ 14:
        bst.postorder()
    ____ choice __ 15:
        print("Height of tree is " , bst.height())
    ____ choice __ 16:
        b..
    ____
        print("Wrong choice") 
    print()


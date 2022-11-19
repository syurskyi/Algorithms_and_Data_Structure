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
        ____ x < ?.i.. :
            ?.lchild _ _insert(?.lchild, x) 
        ____ x > ?.i.. :
            ?.rchild _ _insert(?.rchild, x)   
        ____
            print(x, " already present in the tree") 
        r_ p

    ___ insert1x
        p _ root
        par _ N..
        _____ p __ n.. N..:
            par _ p
            __ x < ?.i.. :
                p _ ?.lchild
            ____ x > ?.i..:
                p _ ?.rchild
            ____
                print(x, " already present in the tree")
                r_

        temp _ Node(x) 

        __ par __ N..:
            root _ temp 
        ____ x < par.i..:
            par.lchild _ temp 
        ____
            par.rchild _ temp 

    ___ searchx
        r_ _search(root, x) __ n.. N..

    ___ _search p, x
        __ p __ N..:
            r_ N..  # key not found
        __ x < ?.i..: # search in left subtree
            r_ _search(?.lchild, x) 
        __ x > ?.i..: # search in right subtree
            r_ _search(?.rchild, x) 
        r_ p  # key found

    ___ search1x
        p _ root 
        _____ p __ n.. N..:
            __ x < ?.i.. :
                p _ ?.lchild  # Move to left child
            ____ x > ?.i..:
                p _ ?.rchild  # Move to right child 
            ____   # x found
                r_ true 
        r_ false 

    ___ deletex
        root _ _delete(root, x) 

    ___ _delete p, x
        __ p __ N..:
            print(x , "  not found")
            r_ p 
         
        __ x < ?.i..:  # delete from left subtree
            ?.lchild _ _delete(?.lchild, x) 
        ____ x > ?.i..: # delete from right subtree
            ?.rchild _ _delete(?.rchild, x)
        ____
            # key to be deleted is found
            __ ?.lchild __ n.. N..  ___ ?.rchild __ n.. N..:  # 2 children
                s _ ?.rchild
                _____ s.lchild __ n.. N..:
                    s _ s.lchild
                ?.i.. _ s.i..
                ?.rchild _ _delete(?.rchild,s.i..) 
                 
            ____   # 1 child or no child
                __ ?.lchild __ n.. N..: # only left child
                    ch _ ?.lchild
                ____  # only right child or no child 
                     ch _ ?.rchild
                p _ ch 
        r_ p  

    ___ delete1x
        p _ root
        par _ N..

        _____ p __ n.. N..:
            __ x __ ?.i..:
                b..
            par _ p
            __ x < ?.i..:
                p _ ?.lchild
            ____
                p _ ?.rchild
            
        __ p __ N..:
            print(x , " not found")
            r_

        # Case C: 2 children 
        # Find inorder successor and its parent 

        __ ?.lchild __ n.. N.. ___ ?.rchild __ n.. N..:
            ps _ p
            s _ ?.rchild

            _____ s.lchild __ n.. N..:
                ps _ s
                s _ s.lchild
            ?.i.. _ s.i..  
            p _ s 
            par _ ps 
                    
        # Case B and Case A : 1 or no child 
        __ ?.lchild __ n.. N..: # node to be deleted has left child
            ch _ ?.lchild 
        ____                # node to be deleted has right child or no child
            ch _ ?.rchild

        __ par __ N..:   # node to be deleted is root node
            root _ ch
        ____ p __ par.lchild: # node is left child of its parent
            par.lchild _ ch
        ____       # node is right child of its parent
            par.rchild _ ch 
     

    ___ min1 
        __ ?
            r... TreeEmptyError("Tree is empty")
        p _ root 
        _____ ?.lchild __ n.. N..:
            p _ ?.lchild 
        r_ ?.i..
    
    ___ max1 
        __ ?
            r... TreeEmptyError("Tree is empty")
        p _ root 
        _____ ?.rchild __ n.. N..:
            p _ ?.rchild 
        r_ ?.i..
    
    ___ min2 
        __ ?
            r... TreeEmptyError("Tree is empty")
        r_ _min(root).i.. 

    ___ _minp
        __ ?.lchild __ N..:
            r_ p 
        r_ _min(?.lchild) 

    ___ max2 
        __ ?
           r... TreeEmptyError("Tree is empty")
        r_ _max(root).i.. 

    ___ _maxp
        __ ?.rchild __ N..:
            r_ p 
        r_ _max(?.rchild) 

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
        print(?.i.., " ")
        _preorder(?.lchild)
        _preorder(?.rchild) 
        
    ___ inorder 
        _inorder(root)
        print()

    ___ _inorder p
        __ p __ N.. :
            r_
        _inorder(?.lchild)
        print(?.i.., " ")
        _inorder(?.rchild) 

    ___ postorder 
        _postorder(root)
        print() 
 
    ___ _postorder p
        __ p __ N..:
            r_
        _postorder(?.lchild)
        _postorder(?.rchild) 
        print(?.i.. , " ") 

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


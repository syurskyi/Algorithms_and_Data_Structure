# Binary Search Trees
# This is the code ot go along with the video explanation. Check out the video lecture for full details!

c_ TreeNode:

    ___ - key,val,left_None,right_None,parent_None
        key _ key
        payload _ val
        leftChild _ left
        rightChild _ right
        parent _ parent

    ___ hasLeftChild 
        r_ leftChild

    ___ hasRightChild 
        r_ rightChild

    ___ isLeftChild 
        r_ parent ___ parent.leftChild __ self

    ___ isRightChild 
        r_ parent ___ parent.rightChild __ self

    ___ isRoot 
        r_ n.. parent

    ___ isLeaf 
        r_ n.. (rightChild __ leftChild)

    ___ hasAnyChildren 
        r_ rightChild __ leftChild

    ___ hasBothChildren 
        r_ rightChild ___ leftChild

    ___ replaceNodeDatakey,value,lc,rc
        key _ key
        payload _ value
        leftChild _ lc
        rightChild _ rc
        __ hasLeftChild(
            leftChild.parent _ self
        __ hasRightChild(
            rightChild.parent _ self


c_ BinarySearchTree:

    ___ -  
        root _ N..
        size _ 0

    ___ length 
        r_ size

    ___ -l 
        r_ size

    ___ putkey,val
        __ root:
            _put(key,val,root)
        ____
            root _ TreeNode(key,val)
        size _ size + 1

    ___ _putkey,val,currentNode
        __ key < ?.key:
            __ ?.hasLeftChild(
                   _put(key,val,?.leftChild)
            ____
                   ?.leftChild _ TreeNode(key,val,parent_currentNode)
        ____
            __ ?.hasRightChild(
                   _put(key,val,?.rightChild)
            ____
                   ?.rightChild _ TreeNode(key,val,parent_currentNode)

    ___ __setitem__k,v
        put(k,v)

    ___ getkey
        __ root:
            res _ _get(key,root)
            __ res:

                r_ res.payload
            ____
                r_ N..
        ____
            r_ N..

    ___ _getkey,currentNode

        __ n.. currentNode:
            r_ N..
        ____ ?.key __ key:
            r_ currentNode
        ____ key < ?.key:
            r_ _get(key,?.leftChild)
        ____
            r_ _get(key,?.rightChild)

    ___ __getitem__key
        r_ get(key)

    ___ __contains__key
        __ _get(key,root
            r_ T..
        ____
            r_ F..

    ___ deletekey

        __ size > 1:

            nodeToRemove _ _get(key,root)
            __ nodeToRemove:
                remove(nodeToRemove)
                size _ size-1
            ____
                r... KeyError('Error, key not in tree')
        ____ size __ 1 ___ root.key __ key:
            root _ N..
            size _ size - 1
        ____
            r... KeyError('Error, key not in tree')

    ___ __delitem__key

        delete(key)

    ___ spliceOut 
        __ isLeaf(
            __ isLeftChild(

                parent.leftChild _ N..
            ____
                parent.rightChild _ N..
        ____ hasAnyChildren(
            __ hasLeftChild(

                __ isLeftChild(

                    parent.leftChild _ leftChild
                ____

                    parent.rightChild _ leftChild
                    leftChild.parent _ parent
        ____

            __ isLeftChild(

                parent.leftChild _ rightChild
            ____
                parent.rightChild _ rightChild
                rightChild.parent _ parent

    ___ findSuccessor 

        succ _ N..
        __ hasRightChild(
            succ _ rightChild.findMin()
        ____
            __ parent:

                __ isLeftChild(

                    succ _ parent
                ____
                    parent.rightChild _ N..
                    succ _ parent.findSuccessor()
                    parent.rightChild _ self
        r_ succ

    ___ findMin 

        current _ self
        _____ current.hasLeftChild(
            current _ current.leftChild
        r_ current

    ___ removecurrentNode

        __ ?.isLeaf( #leaf
            __ currentNode __ ?.parent.leftChild:
                ?.parent.leftChild _ N..
            ____
                ?.parent.rightChild _ N..
        ____ ?.hasBothChildren( #interior

            succ _ ?.findSuccessor()
            succ.spliceOut()
            ?.key _ succ.key
            ?.payload _ succ.payload

        ____ # this node has one child
            __ ?.hasLeftChild(
                __ ?.isLeftChild(
                    ?.leftChild.parent _ ?.parent
                    ?.parent.leftChild _ ?.leftChild
                ____ ?.isRightChild(
                    ?.leftChild.parent _ ?.parent
                    ?.parent.rightChild _ ?.leftChild
                ____

                    ?.replaceNodeData(?.leftChild.key,
                                    ?.leftChild.payload,
                                    ?.leftChild.leftChild,
                                    ?.leftChild.rightChild)
            ____

                __ ?.isLeftChild(
                    ?.rightChild.parent _ ?.parent
                    ?.parent.leftChild _ ?.rightChild
                ____ ?.isRightChild(
                    ?.rightChild.parent _ ?.parent
                    ?.parent.rightChild _ ?.rightChild
                ____
                    ?.replaceNodeData(?.rightChild.key,
                                    ?.rightChild.payload,
                                    ?.rightChild.leftChild,
                                    ?.rightChild.rightChild)


mytree _ BinarySearchTree()
mytree[3]_"red"
mytree[4]_"blue"
mytree[6]_"yellow"
mytree[2]_"at"

print(mytree[6])
print(mytree[2])

# yellow
# at
#
# ** Check the video for full explanation! **
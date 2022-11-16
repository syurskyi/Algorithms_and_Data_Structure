#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

c_ BinaryTree:
    ___ -  size
        customList _ size * [N..]
        lastUsedIndex _ 0
        maxSize _ size
    
    ___ insertNode value
        __ lastUsedIndex + 1 __ maxSize:
            r_ "The Binary Tree is full"
        customList[lastUsedIndex+1] _ value
        lastUsedIndex +_ 1
        r_ "The value has been successfully inserted"

    ___ searchNode nodeValue
        ___ i __ r..(l..(customList
            __ customList[i] __ nodeValue:
                r_ "Success"
        r_ "Not found"
    
    ___ preOrderTraversal index
        __ index > lastUsedIndex:
            r_
        print(customList[index])
        preOrderTraversal(index*2)
        preOrderTraversal(index*2 + 1)

    ___ inOrderTraversal index
        __ index > lastUsedIndex:
            r_
        inOrderTraversal(index*2)
        print(customList[index])
        inOrderTraversal(index*2+1)
    
    ___ postOrderTraversal index
        __ index > lastUsedIndex:
            r_
        postOrderTraversal(index*2)
        postOrderTraversal(index*2+1)
        print(customList[index])
    
    ___ levelOrderTraversal index
        ___ i __ r..(index, lastUsedIndex+1
            print(customList[i])
    
    ___ deleteNode value
        __ lastUsedIndex __ 0:
            r_ "There is not any node to delete"
        ___ i __ r..(1, lastUsedIndex+1
            __ customList[i] __ value:
                customList[i] _ customList[lastUsedIndex]
                customList[lastUsedIndex] _ N..
                lastUsedIndex -_ 1
                r_ "The node has been successfully deleted"
    
    ___ deleteBT 
       customList _ N..
       r_ "The BT has been successfully deleted"

    
 

newBT _ BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

print(newBT.deleteBT())

newBT.levelOrderTraversal(1)




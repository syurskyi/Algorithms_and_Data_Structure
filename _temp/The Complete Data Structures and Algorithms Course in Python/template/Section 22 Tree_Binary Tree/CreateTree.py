#   Created by Elshad Karimov on 05/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ TreeNode:
    ___ -  data, children _ []
        data _ data
        children _ children
    
    ___ __str__ level_0
        ret _ "  " * level + str(data)  + "\n"
        ___ child __ children:
            ret +_ child.__str__(level + 1)
        r_ ret
    
    ___ addChild TreeNode
        children.append(TreeNode)

tree _ TreeNode('Drinks', [])
cold _ TreeNode('Cold', [])
hot _ TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)
tea _ TreeNode('Tea', [])
coffee _ TreeNode('Coffee', [])
cola _ TreeNode('Cola', [])
fanta _ TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)
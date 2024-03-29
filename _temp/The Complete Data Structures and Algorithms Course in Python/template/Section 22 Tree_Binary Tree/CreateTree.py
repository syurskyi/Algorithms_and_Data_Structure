#   Created by Elshad Karimov on 05/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ TreeNode:
    ___ -  data, children _    # list
        ? _ ?
        children _ children
    
    ___ -s level_0
        ret _ "  " * level + s..(data)  + "\n"
        ___ child __ children:
            ret +_ child.-s(level + 1)
        r_ ret
    
    ___ addChild TreeNode
        children.a..(TreeNode)

tree _ TreeNode('Drinks',    # list)
cold _ TreeNode('Cold',    # list)
hot _ TreeNode('Hot',    # list)
tree.addChild(cold)
tree.addChild(hot)
tea _ TreeNode('Tea',    # list)
coffee _ TreeNode('Coffee',    # list)
cola _ TreeNode('Cola',    # list)
fanta _ TreeNode('Fanta',    # list)
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)
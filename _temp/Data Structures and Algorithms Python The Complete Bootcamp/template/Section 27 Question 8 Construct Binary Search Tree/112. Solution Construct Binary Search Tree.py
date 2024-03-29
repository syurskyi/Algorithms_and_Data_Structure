# Definition for a binary tree node.
c_ TreeNode:
    ___ -  val_0, left_None, right_None
        ? _ ?
        left _ left
        right _ right


c_ Solution
    ___ bstFromPreorder preorder

        root _ TreeNode(preorder[0])
        stack _ [root]

        ___ i __ r..(1, l..(preorder
            __ preorder[i] < stack[-1].v..:
                node _ TreeNode(preorder[i])
                stack[-1].left _ node
                stack.a..(node)
            ____
                _____ stack ___ stack[-1].v.. < preorder[i]:
                    pop _ stack.p.. 
                node _ TreeNode(preorder[i])
                pop.right _ node
                stack.a..(node)

        r_ root
# Definition for a binary tree node.
c_ TreeNode:
    ___ -  val_0, left_None, right_None
        ? _ ?
        left _ left
        right _ right


c_ Solution
    ___ buildTree preorder, inorder
        memory _     # dict
        ___ i, e __ enumerate(inorder
            memory[e] _ i

        root _ helper(preorder[::-1], inorder, 0, l..(inorder), memory)
        r_ root

    ___ helper preorder, inorder, leftPointer, rightPointer, memory
        __ leftPointer >_ rightPointer:
            r_ N..

        num _ preorder.p.. 
        root _ TreeNode(num)
        idx _ memory.get(num)

        root.left _ helper(preorder, inorder, leftPointer, idx, memory)
        root.right _ helper(preorder, inorder, idx + 1, rightPointer, memory)

        r_ root
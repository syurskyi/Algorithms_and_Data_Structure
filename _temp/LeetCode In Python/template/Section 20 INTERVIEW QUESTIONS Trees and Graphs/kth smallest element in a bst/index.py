c_ Solution:
    ___ kthSmallest root: TreeNode, k: i..) -> i..:
        k _ k
        res _ N..
        helper(root)
        r_ res

    ___ helper root
        __ n.. root:
            r_
        helper(root.left)
        
        k -_ 1
        __ k __ 0:
            res _ root.val
            r_
        helper(root.right)

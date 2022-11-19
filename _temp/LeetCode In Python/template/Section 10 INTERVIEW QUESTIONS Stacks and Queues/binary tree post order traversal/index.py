# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution
    ___ postorderTraversal root: TreeNode) __ List[i..]:
        __(n.. root
            r_
        
        ans _    # list
        s1 _    # list
        s2 _    # list

        s1.a..(root)

        _____(s1
            x _ s1[-1]
            s1.p.. 
            s2.a..(x)

            __(x.left
                s1.a..(x.left)
            __(x.right
                s1.a..(x.right)
        
        _____(s2
            y _ s2[-1]
            s2.p.. 
            ans.a..(y.v..)
        r_ ans
# Definition for a binary tree node.
# class TreeNode:
#     def init(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution
    ___ zigzagLevelOrder root: TreeNode) __ List[List[i..]]:
        __ n.. root:
            r_    # list
        res _    # list
        q _ collections.deque()

        zigzag _ F..
        q.a..(root)

        _____ q:
            level _    # list
            ___ _ __ r..(l..(q
                __ zigzag:
                    node _ q.p.. 
                    level.a..(node.v..)
                    __ node.right:
                        q.appendleft(node.right)
                    __ node.left:
                        q.appendleft(node.left)

                ____
                    node _ q.popleft()
                    level.a..(node.v..)
                    __ node.left:
                        q.a..(node.left)
                    __ node.right:
                        q.a..(node.right)
            res.a..(level)
            zigzag _ n.. zigzag

        r_ res

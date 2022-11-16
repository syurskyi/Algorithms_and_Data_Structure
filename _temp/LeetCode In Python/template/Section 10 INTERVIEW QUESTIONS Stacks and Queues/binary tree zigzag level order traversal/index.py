# Definition for a binary tree node.
# class TreeNode:
#     def init(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution:
    ___ zigzagLevelOrder root: TreeNode) -> List[List[int]]:
        __ n.. root:
            r_ []
        res _ []
        q _ collections.deque()

        zigzag _ False
        q.append(root)

        _____ q:
            level _ []
            ___ _ __ range(len(q)):
                __ zigzag:
                    node _ q.pop()
                    level.append(node.val)
                    __ node.right:
                        q.appendleft(node.right)
                    __ node.left:
                        q.appendleft(node.left)

                ____
                    node _ q.popleft()
                    level.append(node.val)
                    __ node.left:
                        q.append(node.left)
                    __ node.right:
                        q.append(node.right)
            res.append(level)
            zigzag _ n.. zigzag

        r_ res

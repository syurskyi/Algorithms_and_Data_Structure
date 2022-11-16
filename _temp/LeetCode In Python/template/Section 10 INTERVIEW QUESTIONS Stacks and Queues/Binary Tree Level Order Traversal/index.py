# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

c_ Solution:
    ___ levelOrder root: TreeNode) -> List[List[int]]:
        ans _    # list

        __(root __ N..
            r_ ans
        
        q _ deque([root])

        _____(q
            n _ l..(q)
            temp _    # list
            ___ i __ range(0,n
                f _ q.popleft()
                temp.a..(f.val)

                __(f.left __ n.. N..
                    q.a..(f.left)
                __(f.right __ n.. N..
                    q.a..(f.right)

            __(l..(temp)>0
                ans.a..(temp[:])
                temp.clear()
        r_ ans
        

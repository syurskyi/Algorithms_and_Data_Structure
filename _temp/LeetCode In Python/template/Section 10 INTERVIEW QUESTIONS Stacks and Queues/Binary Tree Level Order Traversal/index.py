# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

c_ Solution:
    ___ levelOrder root: TreeNode) -> List[List[int]]:
        ans _ []

        __(root __ N..
            r_ ans
        
        q _ deque([root])

        _____(q
            n _ len(q)
            temp _ []
            ___ i __ range(0,n
                f _ q.popleft()
                temp.append(f.val)

                __(f.left __ n.. N..
                    q.append(f.left)
                __(f.right __ n.. N..
                    q.append(f.right)

            __(len(temp)>0
                ans.append(temp[:])
                temp.clear()
        r_ ans
        

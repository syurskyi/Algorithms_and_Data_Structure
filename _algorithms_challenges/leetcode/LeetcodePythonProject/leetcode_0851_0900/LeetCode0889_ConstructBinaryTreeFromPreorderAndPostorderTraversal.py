'''
Created on Oct 29, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        return self.helper(pre, 0, len(pre)-1, post, 0, len(post)-1)
    
    def helper(self, pre, preStart, preEnd, post, postStart, postEnd):
        if preStart > preEnd:
            return None
        val = pre[preStart]
        node = TreeNode(val)
        if postStart == postEnd:
            return node
        
        nextPreStart = preStart+1
        val = pre[preStart+1]
        nextPostEnd = post.index(val)
        nextPreEnd = nextPreStart+(nextPostEnd-postStart)
        leftNode = self.helper(pre, nextPreStart, nextPreEnd, post, postStart, nextPostEnd)
        rightNode = self.helper(pre, nextPreEnd+1, preEnd, post, nextPostEnd+1, postEnd-1)

        node.left = leftNode
        node.right = rightNode
        return node
    
    def test(self):
        testCases = [
            [
                [2,1,3],
                [3,1,2],
            ],
#             [
#                 [2,1],
#                 [1,2],
#             ],
#             [
#                 [1,2,4,5,3,6,7],
#                 [4,5,2,6,7,3,1],
#             ],
        ]
        for pre, post in testCases:
            node = self.constructFromPrePost(pre, post)
            print(node)

if __name__ == '__main__':
    Solution().test()


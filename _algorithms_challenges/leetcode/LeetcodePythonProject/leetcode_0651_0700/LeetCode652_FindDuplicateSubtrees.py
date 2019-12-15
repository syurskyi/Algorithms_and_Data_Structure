'''
Created on Oct 4, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        self.postorder(root, {}, res)
        return res
    
    def postorder(self, cur, hashmap, res):
        if not cur: return '#'
        serial = '%s,%s,%s' % (cur.val,\
                self.postorder(cur.left, hashmap, res),\
                self.postorder(cur.right, hashmap, res))
        if hashmap.get(serial, 0) == 1:
            res.append(cur)
        hashmap[serial] = hashmap.get(serial, 0)+1
        return serial
    
    def test(self):
        testCases = [
            TreeNode(2, TreeNode(1), TreeNode(1)),
            TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4))),
        ]
        for root in testCases:
            res = self.findDuplicateSubtrees(root)
            print('result: %s' % [node.val for node in res])
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

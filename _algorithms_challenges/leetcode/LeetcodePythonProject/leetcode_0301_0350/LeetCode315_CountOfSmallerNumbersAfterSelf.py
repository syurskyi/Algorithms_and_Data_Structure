'''
Created on Mar 15, 2017

@author: MT
'''

class TreeNode(object):
    def __init__(self, val, num=1):
        self.val = val
        self.num = num
        self.left = None
        self.right = None
    
    def __str__(self):
        return '<val: %s, num: %s>' % (self.val, self.num)
    
    def __repr__(self):
        return self.__str__()

class Solution(object):
    def countSmaller(self, nums):
        if not nums: return []
        root = TreeNode(nums[-1])
        result = [0]
        for i in range(len(nums)-2, -1, -1):
            result.insert(0, self.getVal(root, nums[i], 0))
        return result, root
    
    def getVal(self, root, val, num):
        if root.val >= val:
            root.num += 1
            if not root.left:
                root.left = TreeNode(val)
                return num
            else:
                return self.getVal(root.left, val, num)
        else:
            num += root.num
            if not root.right:
                root.right = TreeNode(val)
                return num
            else:
                return self.getVal(root.right, val, num)
    
    def test(self):
        testCases = [
            [5, 2, 6, 1],
            [-1, -1],
            [3, 2, 2, 6, 1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result, root = self.countSmaller(nums)
            print('result: %s' % (result))
            print('-='*20+'-')
            
            queue= [root]
            line = []
            nextQueue = []
            while queue:
                node = queue.pop(0)
                line.append(node)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
                if not queue:
                    queue = nextQueue
                    nextQueue = []
                    print(line)
                    line = []
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()


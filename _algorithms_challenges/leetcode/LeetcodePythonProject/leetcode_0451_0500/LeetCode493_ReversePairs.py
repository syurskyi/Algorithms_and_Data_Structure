'''
Created on May 9, 2017

@author: MT
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.less = 0
        self.same = 1
        self.left = None
        self.right = None

class Solution(object):
    def reversePairs_mergeSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cnt = 0
        def msort(lst):
            n = len(lst)
            if n <= 1:
                return lst
            else:
                return merger(msort(lst[:int(n/2)]), msort(lst[int(n/2):]))
        def merger(left, right):
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= 2*right[r]:
                    l += 1
                else:
                    self.cnt += len(left)-l
                    r += 1
            return sorted(left+right)
        msort(nums)
        return self.cnt
    
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = None
        cnt = [0]
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            self.search(cnt, root, num/2.0)
            root = self.build(num, root)
        return cnt[0]
    
    def search(self, cnt, node, target):
        if not node:
            return
        elif target == node.val:
            cnt[0] += node.less
        elif target < node.val:
            self.search(cnt, node.left, target)
        else:
            cnt[0] += node.less + node.same
            self.search(cnt, node.right, target)
    
    def build(self, val, node):
        if not node:
            return Node(val)
        elif val == node.val:
            node.same += 1
        elif val > node.val:
            node.right = self.build(val, node.right)
        else:
            node.less += 1
            node.left = self.build(val, node.left)
        return node
    
    def test(self):
        testCases = [
            [1, 3, 2, 3, 1],
            [2, 4, 3, 5, 1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.reversePairs_mergeSort(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

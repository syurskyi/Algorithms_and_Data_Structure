'''
Created on Jan 31, 2018

@author: tongq
'''
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashmap = {}
        for a in A:
            for b in B:
                hashmap[a+b] = hashmap.get(a+b, 0)+1
        res = 0
        for c in C:
            for d in D:
                res += hashmap.get(-c-d, 0)
        return res
    
    def test(self):
        testCases = [
            [
                [ 1, 2],
                [-2,-1],
                [-1, 2],
                [ 0, 2],
            ],
        ]
        for nums1, nums2, nums3, nums4 in testCases:
            result = self.fourSumCount(nums1, nums2, nums3, nums4)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

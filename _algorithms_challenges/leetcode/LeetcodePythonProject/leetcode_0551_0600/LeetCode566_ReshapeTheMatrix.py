'''
Created on Aug 30, 2017

@author: MT
'''
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or not nums[0]: return nums
        m, n = len(nums), len(nums[0])
        if m*n != r*c:
            return nums
        res = []
        k, l = 0, 0
        for _ in range(r):
            cur = []
            for _ in range(c):
                cur.append(nums[k][l])
                l += 1
                if l == n:
                    l = 0
                    k += 1
            res.append(cur)
        return res
    
    def test(self):
        testCases = [
            [
                [[1, 2],
                 [3, 4]],
                1,
                4,
            ],
            [
                [[1, 2],
                 [3, 4]],
                2,
                4,
            ],
        ]
        for nums, r, c in testCases:
            print('nums:')
            print('\n'.join([str(row) for row in nums]))
            print('r: %s' % r)
            print('c: %s' % c)
            result = self.matrixReshape(nums, r, c)
            print('result:')
            print('\n'.join([str(row) for row in result]))
            print('-='*30)

if __name__ == '__main__':
    Solution().test()

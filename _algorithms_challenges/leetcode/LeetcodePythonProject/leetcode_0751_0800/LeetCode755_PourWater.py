'''
Created on Mar 28, 2018

@author: tongq
'''
class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        if not heights: return heights
        idx = 0
        while V > 0:
            idx = K
            for i in range(K-1, -1, -1):
                if heights[i] > heights[idx]:
                    break
                elif heights[i] < heights[idx]:
                    idx = i
            if idx != K:
                heights[idx] += 1
                V -= 1
                continue
            for i in range(K+1, len(heights)):
                if heights[i] > heights[idx]:
                    break
                elif heights[i] < heights[idx]:
                    idx = i
            heights[idx] += 1
            V -= 1
        return heights
    
    def test(self):
        testCases = [
            [[2,1,1,2,1,2,2], 4, 3],
            [[1,2,3,4], 2, 2],
            [[3,1,3], 5, 1],
            [
                [1,2,3,4,3,2,1,2,3,4,3,2,1],
                5,
                5,
            ],
            [
                [1,2,3,4,3,2,1,2,3,4,3,2,1],
                10,
                2,
            ],
            [
                [1,2,3,4,3,2,1,2,3,4,3,2,1],
                5,
                2,
            ],
        ]
        for heights, v, k in testCases:
            print('heights: %s' % heights)
            print('v: %s' % v)
            print('k: %s' % k)
            result = self.pourWater(heights, v, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Oct 7, 2019

@author: tongq
'''
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        import math
        piles.sort()
        l, r = 1, max(piles)
        while l <= r:
            mid = l+(r-l)//2
            sumVal = sum(math.ceil(float(num)/mid) for num in piles)
            if sumVal <= H:
                r = mid-1
            else:
                l = mid+1
        return l
    
    def test(self):
        testCases = [
            [
                [3,6,7,11],
                8
            ],
            [
                [30,11,23,4,20],
                5,
            ],
            [
                [30,11,23,4,20],
                6,
            ],
        ]
        for piles, h in testCases:
            res = self.minEatingSpeed(piles, h)
            print('res: %s' % str(res))
            print('-='*30+'-')

if __name__ == '__main__':
    import math
    print(math.ceil(float(3)/3))
    print(math.ceil(float(4)/3))
    Solution().test()

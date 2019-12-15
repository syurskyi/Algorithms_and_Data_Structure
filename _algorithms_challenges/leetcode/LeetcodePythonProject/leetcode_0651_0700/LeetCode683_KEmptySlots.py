'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers: return -1
        n = len(flowers)
        days = [False]*n
        for i in range(n):
            days[flowers[i]-1] = i+1
        left, right = 0, k+1
        res = float('inf')
        for i in range(n):
            if right >= n: break
            if days[i] == days[right] and i == right:
                res = min(res, max(days[left], days[right]))
            if days[i] < days[left] or days[i] < days[right]:
                left = i
                right = k+1+i
        return res if res != float('inf') else -1
    
    def test(self):
        testCases = [
            [
                [1, 3, 2],
                1,
            ],
            [
                [1, 2, 3],
                1,
            ],
            [
                [1,2,3,4,5,6,7],
                1,
            ],
        ]
        for flowers, k in testCases:
            print('flowers: %s' % flowers)
            print('k: %s' % k)
            result = self.kEmptySlots(flowers, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

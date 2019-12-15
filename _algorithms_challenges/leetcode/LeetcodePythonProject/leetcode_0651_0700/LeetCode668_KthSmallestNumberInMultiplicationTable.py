'''
Created on Oct 11, 2017

@author: MT
'''
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        low, high = 1, m*n+1
        while low < high:
            mid = (low+high)//2
            c = self.count(mid, m, n)
            if c >= k:
                high = mid
            else:
                low = mid+1
        return high
    
    def count(self, val, m, n):
        count = 0
        for i in range(1, m+1):
            tmp = min(val//i, n)
            count += tmp
        return count
    
    def test(self):
        testCases = [
            [
                3,
                3,
                5,
            ],
            [
                2,
                3,
                6,
            ],
        ]
        for m, n, k in testCases:
            print('m: %s' % m)
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.findKthNumber(m, n, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

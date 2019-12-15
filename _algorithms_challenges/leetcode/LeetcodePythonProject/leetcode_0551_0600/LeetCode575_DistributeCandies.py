'''
Created on Sep 3, 2017

@author: MT
'''
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        n = int(len(candies)/2)
        candies = set(candies)
        return min(n, len(candies))
    
    def test(self):
        testCases = [
            [1,1,2,3],
            [1,1,2,2,3,3],
        ]
        for candies in testCases:
            print('candies: %s' % candies)
            result = self.distributeCandies(candies)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Feb 9, 2017

@author: MT
'''

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        left = [0]*n
        left[0] = 1
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
            else:
                left[i] = 1
        right = [0]*n
        right[-1] = 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1]+1
            else:
                right[i] = 1
        res = 0
        for i in range(n):
            res += max(left[i], right[i])
        return res
    
    def test(self):
        testCases = [
            [1, 0, 2],
            [1, 2, 2],
            [1,3,2,2,1],
            [1, 2, 3, 1, 3, 3, 2],
        ]
        for ratings in testCases:
            print('ratings: %s' % (ratings))
            result = self.candy(ratings)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0]*121
        for x in ages:
            count[x] += 1
        res = 0
        for i in range(1, 121):
            if i > 14:
                res += count[i]*(count[i]-1+count[i-1]-count[i//2+7])
            count[i] += count[i-1]
        return res
    
    def test(self):
        testCases = [
            [16,16],
            [16,17,18],
            [20,30,100,110,120],
            [54,23,102,90,40,74,112,74,76,21],
        ]
        for ages in testCases:
            print('ages: %s' % ages)
            result = self.numFriendRequests(ages)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on Oct 1, 2017

@author: MT
'''
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        res = 1
        pairs.sort(key=lambda x: (x[1], x[0]))
        maxLen = pairs[0][1]
        for i in range(1, len(pairs)):
            pair = pairs[i]
            if pair[0] > maxLen:
                maxLen = pairs[i][1]
                res += 1
        return res
    
    def test(self):
        testCases = [
            [[1, 2], [2, 3], [3, 4]],
            [[1, 10], [2, 3], [4, 5], [6, 7]],
        ]
        for pairs in testCases:
            print('pairs: %s' % pairs)
            result = self.findLongestChain(pairs)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

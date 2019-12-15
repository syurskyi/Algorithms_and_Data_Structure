'''
Created on May 6, 2018

@author: tongq
'''
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        s = S
        res = []
        left = 0
        for i in range(len(s)+1):
            if i == len(s) or s[i] != s[left]:
                if i-left >= 3:
                    res.append([left, i-1])
                left = i
        return res
    
    def test(self):
        testCases = [
            'aaa',
            'abbxxxxzzy',
            'abc',
            'abcdddeeeeaabbbcd',
        ]
        for s in testCases:
            result = self.largeGroupPositions(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

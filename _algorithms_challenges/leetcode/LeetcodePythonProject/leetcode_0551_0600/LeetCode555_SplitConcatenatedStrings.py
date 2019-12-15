'''
Created on Aug 24, 2017

@author: MT
'''

class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = None
        arr = [max(s, s[::-1]) for s in strs]
        for i, s in enumerate(arr):
            for start in (s, s[::-1]):
                for j in range(len(start)+1):
                    if not res:
                        res = start[j:] + ''.join(arr[i+1:]+arr[:i]) + start[:j]
                    else:
                        res = max(res, start[j:] + ''.join(arr[i+1:]+arr[:i]) + start[:j])
        return res
    
    def test(self):
        testCases = [
            ['abc', 'xyz'],
        ]
        for strs in testCases:
            print('strs: %s' % strs)
            result = self.splitLoopedString(strs)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

'''
Created on May 2, 2018

@author: tongq
'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        s, c = S, C
        arr = []
        for i, c0 in enumerate(s):
            if c0 == c:
                arr.append(i)
        res = []
        j = 0
        for i in range(len(s)):
            if i < arr[j]:
                val = arr[j]-i
                if j > 0:
                    val = min(val, i-arr[j-1])
            elif i == arr[j]:
                val = 0
                if j < len(arr)-1:
                    j += 1
            else:
                val = i-arr[j]
            res.append(val)
        return res
    
    def test(self):
        testCases = [
            [
                'loveleetcode', 'e',
            ],
        ]
        for s, c in testCases:
            print('s: %s' % s)
            print('c: %s' % c)
            result = self.shortestToChar(s, c)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

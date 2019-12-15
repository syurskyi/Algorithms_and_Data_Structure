'''
Created on May 6, 2018

@author: tongq
'''
class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        s = S
        hashmap = {}
        for i, c in enumerate(s):
            if c in hashmap:
                l = hashmap[c]
            else:
                l = []
            l.append(i)
            hashmap[c] = l
        sumVal = 0
        for c, l in hashmap.items():
            for i in range(len(l)):
                if i == 0:
                    left = l[i]
                else:
                    left = l[i]-l[i-1]-1
                if i == len(l)-1:
                    right = len(s)-l[i]-1
                else:
                    right = l[i+1]-l[i]-1
                sumVal = (sumVal+1+left+right+left*right)%(10**9+7)
        return sumVal
    
    def test(self):
        testCases = [
            'ABC',
            'ABA',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.uniqueLetterString(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

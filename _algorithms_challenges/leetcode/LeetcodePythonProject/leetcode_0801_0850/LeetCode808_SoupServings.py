'''
Created on Apr 25, 2018

@author: tongq
'''
class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        n = N
        hashmap = {}
        if N < 5000:
            return self.helper(hashmap, n, n)
        else:
            return 1
    
    def helper(self, hashmap, a, b):
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0
        s = str(a)+':'+str(b)
        if s not in hashmap:
            hashmap[s] = 0.25*(
                    self.helper(hashmap, a-100, b)+\
                    self.helper(hashmap, a-25, b-75)+\
                    self.helper(hashmap, a-75, b-25)+\
                    self.helper(hashmap, a-50, b-50)
                )
        return hashmap[s]
    
    def test(self):
        testCases = [
            50,
        ]
        for n in testCases:
            result = self.soupServings(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

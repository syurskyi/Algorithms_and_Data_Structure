'''
Created on Mar 4, 2017

@author: MT
'''

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return False
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        odd = 0
        oddVal = ''
        for key, value in hashmap.items():
            if value%2 != 0:
                oddVal = key
                odd += 1
        if len(s)%2 == 0:
            if odd != 0:
                return []
        else:
            if odd >= 2:
                return []
        result = []
        self.helper(oddVal, len(s), hashmap, result)
        return result
    
    def helper(self, s0, length, hashmap, result):
        if len(s0) >= length:
            result.append(s0)
            return
        for c, val in hashmap.items():
            if val >= 2:
                hashmap[c] -= 2
                self.helper(c+s0+c, length, hashmap, result)
                hashmap[c] += 2
    
    def test(self):
        testCases = [
            'aaabb',
            'abc',
            'aab',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.generatePalindromes(s)
            print('result: %s' % (result))
            print('-='*20+'-')
            

if __name__ == '__main__':
    Solution().test()

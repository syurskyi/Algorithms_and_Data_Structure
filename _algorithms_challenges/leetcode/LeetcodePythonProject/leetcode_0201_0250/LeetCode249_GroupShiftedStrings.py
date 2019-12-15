'''
Created on Feb 28, 2017

@author: MT
'''

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for s in strings:
            hashStr = self.getHash(s)
            hashmap[hashStr] = hashmap.get(hashStr, []) + [s]
        res = []
        for vals in hashmap.values():
            res.append(vals)
        return res
    
    def getHash(self, s):
        if not s: return '-2'
        if len(s) == 1: return '-1'
        res = ''
        for i in range(1, len(s)):
            diff = ord(s[i])-ord(s[i-1])
            if diff < 0:
                diff += 26
            res += '%s,' % diff
        return res
    
    def groupStrings_another(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        result = []
        for s in strings:
            added = False
            for l in result:
                if self.isSameGroup(l[0], s):
                    l.append(s)
                    added = True
            if not added:
                result.append([s])
        return result
    
    def isSameGroup(self, s1, s2):
        if len(s1) != len(s2):
            return False
        length = len(s1)
        if length == 1:
            return True
        diff = ord(s1[0]) - ord(s2[0])
        if diff < 0:
            diff += 26
        for i in range(1, length):
            d = ord(s1[i]) - ord(s2[i])
            if d < 0:
                d += 26
            if d > 26:
                d -= 26
            if d != diff:
                return False
        return True
    
    def test(self):
        testCases = [
            ["abc","bcd","acef","xyz","az","ba","a","z"],
        ]
        for strings in testCases:
            print('strs: %s' % (strings))
            result = self.groupStrings(strings)
            print('result: %s' % (result))
            print('-='*20+'-')
    
if __name__ == '__main__':
    Solution().test()

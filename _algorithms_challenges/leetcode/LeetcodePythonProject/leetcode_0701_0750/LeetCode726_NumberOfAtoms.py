'''
Created on Feb 21, 2018

@author: tongq
'''
import re
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        hashmap = self.helper(formula)
        arr = sorted([str(c)+str(count) if count > 1 else str(c) for c, count in hashmap.items()])
        res = ''.join(arr)
        return res
    
    def helper(self, s):
        hashmap = {}
        i = 0
        while i < len(s):
            if s[i] == '(':
                count0 = 1
                i += 1
                prev = i
                while i < len(s) and count0 > 0:
                    if s[i] == ')':
                        count0 -= 1
                    elif s[i] == '(':
                        count0 += 1
                    i += 1
                hashmap0 = self.helper(s[prev:i-1])
                if i == len(s) or not s[i].isdigit():
                    count = 1
                else:
                    prev = i
                    while i < len(s) and s[i].isdigit():
                        i += 1
                    count = int(s[prev:i])
                for elem, freq in hashmap0.items():
                    hashmap[elem] = hashmap.get(elem, 0)+freq*count
            else:
                if i+1 < len(s) and re.match('[a-z]', s[i+1]):
                    elem = s[i:i+2]
                    i+=1
                else:
                    elem = s[i]
                i+=1
                if i == len(s) or not s[i].isdigit() or s[i] == '(':
                    count = 1
                else:
                    prev = i
                    while i < len(s) and s[i].isdigit():
                        i += 1
                    count = int(s[prev:i])
                hashmap[elem] = hashmap.get(elem, 0)+count
        return hashmap
    
    def test(self):
        testCases = [
#             'H2O',
#             'Mg(OH)2',
#             'K4(ON(SO3)2)2',
            '((N42)24(B11))2',
            '((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.countOfAtoms(s)
            print('result: %s' % result)
            print('-='*30+'-')
        
if __name__ == '__main__':
    Solution().test()

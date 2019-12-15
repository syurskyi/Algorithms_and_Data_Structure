'''
Created on Mar 16, 2017

@author: MT
'''

class Solution(object):
    def removeDuplicateLetters(self, s):
        if not s: return ''
        cnt = [0]*26
        pos = 0
        for c in s:
            cnt[ord(c)-ord('a')] += 1
        for i, c in enumerate(s):
            if s[i] < s[pos]:
                pos = i
            cnt[ord(c)-ord('a')] -= 1
            if cnt[ord(c)-ord('a')] == 0:
                break
        return s[pos]+self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))
    
    def removeDuplicateLetters_another(self, s):
        if not s: return ''
        lastPosMap = {}
        for i, c in enumerate(s):
            lastPosMap[c] = i
        length = len(lastPosMap)
        res = ['a']*length
        begin, end = 0, min(lastPosMap.values())
        for i in range(length):
            minChar = chr(ord('z')+1)
            for j in range(begin, end+1):
                if s[j] in lastPosMap and s[j] < minChar:
                    minChar = s[j]
                    begin = j+1
            res[i] = minChar
            if i == length-1:
                break
            del lastPosMap[minChar]
            end = min(lastPosMap.values())
        return ''.join(res)
    
    def test(self):
        testCases = [
            'bcabc',
            'cbacbcbc',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.removeDuplicateLetters(s)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

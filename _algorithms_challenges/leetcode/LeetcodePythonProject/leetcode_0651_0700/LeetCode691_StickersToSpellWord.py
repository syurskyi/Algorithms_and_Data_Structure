'''
Created on Oct 24, 2017

@author: MT
'''
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        n = len(stickers)
        mp = [[0]*26 for _ in range(n)]
        for i in range(n):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1
        mem = {}
        mem[''] = 0
        return self.helper(mem, mp, target)
    
    def helper(self, mem, mp, target):
        if target in mem:
            return mem[target]
        n = len(mp)
        tar = [0]*26
        for c in target:
            tar[ord(c)-ord('a')] += 1
        res = float('inf')
        for i in range(n):
            if mp[i][ord(target[0])-ord('a')] == 0:
                continue
            s = ''
            for j in range(26):
                if tar[j] > mp[i][j]:
                    s += chr(ord('a')+j)*(tar[j]-mp[i][j])
            tmp = self.helper(mem, mp, s)
            if tmp != -1:
                res = min(res, 1+tmp)
        mem[target] = -1 if res == float('inf') else res
        return mem[target]
    
    def test(self):
        testCases = [
            [
                ["with", "example", "science"],
                "thehat",
            ],
            [
                ["notice", "possible"],
                "basicbasic",
            ],
        ]
        for stickers, target in testCases:
            print('stickers: %s' % stickers)
            print('target: %s' % target)
            result = self.minStickers(stickers, target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

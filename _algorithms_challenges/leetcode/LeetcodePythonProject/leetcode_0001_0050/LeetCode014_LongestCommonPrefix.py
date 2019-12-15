'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        ind = 0
        while True:
            same = True
            for i, s in enumerate(strs):
                if ind == len(s):
                    same = False
                    break
                if i == 0:
                    c = s[ind]
                elif c != s[ind]:
                    same = False
                    break
            if not same:
                break
            ind += 1
        return strs[0][:ind]
    
    def test(self):
        testCases = [
            ['a', 'b'],
            ['aa', 'aa'],
        ]
        for strs in testCases:
            print('\n'.join([str(row) for row in strs]))
            result = self.longestCommonPrefix(strs)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

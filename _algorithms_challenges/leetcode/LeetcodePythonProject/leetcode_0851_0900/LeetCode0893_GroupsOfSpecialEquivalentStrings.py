'''
Created on Nov 4, 2019

@author: tongq
'''
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        hashset = set()
        for w in A:
            hashset.add(self.getHash(w))
        return len(hashset)
    
    def getHash(self, word):
        arr = [[0]*26, [0]*26]
        for i, c in enumerate(word):
            arr[i%2][ord(c)-ord('a')] += 1
        return '|'.join([','.join(str(num) for num in arr0) for arr0 in arr])
    
    def test(self):
        testCases = [
            ["abcd","cdab","cbad","xyzz","zzxy","zzyx"],
        ]
        for arr in testCases:
            res = self.numSpecialEquivGroups(arr)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

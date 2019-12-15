'''
Created on Feb 28, 2017

@author: MT
'''

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.pairs = ['00', '11', '69', '96', '88']
        res = []
        self.helper(0, n-1, ['']*n, res)
        return res
    
    def helper(self, l, r, curr, res):
        if l > r:
            res.append(''.join(curr))
            return
        for p in self.pairs:
            curr[l] = p[0]
            curr[r] = p[1]
            if l == r and p[0] != p[1]:
                continue
            elif l == 0 and l != r and p[0] == '0':
                continue
            self.helper(l+1, r-1, curr, res)
    
    def findStrobogrammatic_short(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        evenMidCandidate = ['11', '69', '88', '96', '00']
        oddMidCandidate = ['0', '1', '8']
        if n == 1:
            return oddMidCandidate
        if n == 2:
            return evenMidCandidate[:-1]
        if n % 2 != 0:
            pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
        else:
            pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
        premid = int((n-1)/2)
        result = []
        for c in midCandidate:
            for p in pre:
                result.append(p[:premid]+c+p[premid:])
        return result
    
    def test(self):
        testCases = [
            4,
        ]
        for n in testCases:
            print('n: %s' % (n))
            result = self.findStrobogrammatic(n)
            print('result: %s' % (result))
            print('-='*20+'-')
 
if __name__ == '__main__':
    Solution().test()

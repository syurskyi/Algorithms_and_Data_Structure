'''
Created on Oct 16, 2019

@author: tongq
'''
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        arr1 = A.split(' ')
        arr2 = B.split(' ')
        hashset1, hashset2, hashset3 = set(), set(), set()
        for w in arr1:
            if w not in hashset1:
                hashset1.add(w)
            else:
                hashset3.add(w)
        for w in arr2:
            if w not in hashset2:
                hashset2.add(w)
            else:
                hashset3.add(w)
        res = []
        for w in hashset1:
            if w not in hashset3 and w not in hashset2:
                res.append(w)
        for w in hashset2:
            if w not in hashset3 and w not in hashset1:
                res.append(w)
        return res

'''
Created on Jun 10, 2018

@author: tongq
'''
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        import collections
        n = len(A)
        #encode the position of 1 in A and B
        #we can' t use i//n*n + i%n. Although it is a distinct way to encode position
        LA = [(i, j) for i in range(n) for j in range(n) if A[i][j] == 1]
        LB = [(i, j) for i in range(n) for j in range(n) if B[i][j] == 1]
        counts = collections.defaultdict(int)
        res = 0
        for i in LA:
            for j in LB:
                counts[(i[0]-j[0], i[1]-j[1])] += 1
                res = max(res, counts[(i[0]-j[0], i[1]-j[1])])
        return res
    
    def largestOverlap_another(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        la = [i/n*100 + i%n for i in range(n*n) if A[i/n][i%n]]
        lb = [i/n*100 + i%n for i in range(n*n) if B[i/n][i%n]]
        count = {}
        for i in la:
            for j in lb:
                count[i-j] = count.get(i-j, 0)+1
        return max(count.values() or [0])

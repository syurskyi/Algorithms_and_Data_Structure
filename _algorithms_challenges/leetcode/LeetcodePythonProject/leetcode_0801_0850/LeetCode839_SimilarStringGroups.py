'''
Created on Oct 10, 2018

@author: tongq
'''
import itertools

class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        arr = list(set(A))
        parents = {x: x for x in arr}
        n, m = len(arr), len(arr[0])
        self.count = n
        
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parents[x] = y
                self.count -= 1
                return True
            return False
        
        def similar(x, y):
            return sum(i != j for i, j in zip(x, y)) == 2
        
        ## Solution part ##
        if n < m:
            for x, y in itertools.combinations(arr, 2):
                if similar(x, y):
                    union(x, y)
        else:
            for x in arr:
                for i, j in itertools.combinations(range(m), 2):
                    y = x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
                    if y in parents:
                        union(x, y)
        
        return self.count
    
    def test(self):
        testCases = [
            ["aaa", "aaa", "aaa"],
            ["tars","rats","arts","star"],
            ["blw","bwl","wlb"],
            ["nmiwx","mniwx","wminx","mnixw","xnmwi"],
        ]
        for strs in testCases:
            print('strs: %s' % strs)
            result = self.numSimilarGroups(strs)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

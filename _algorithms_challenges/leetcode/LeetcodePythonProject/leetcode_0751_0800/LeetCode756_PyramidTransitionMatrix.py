'''
Created on Mar 30, 2018

@author: tongq
'''
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        if not bottom:
            return False
        hashmap = {}
        for s in allowed:
            if s[:2] in hashmap:
                hashmap[s[:2]].add(s[-1])
            else:
                hashmap[s[:2]] = set([s[-1]])
        level = len(bottom)
        queue = list(bottom)
        while queue:
            if level == 1:
                if queue and queue[0]:
                    return True
                else:
                    return False
            nextQueue = [set() for _ in range(level-1)]
            for i in range(level-1):
                arr1 = queue[i]
                arr2 = queue[i+1]
                for c1 in arr1:
                    for c2 in arr2:
                        if c1+c2 in hashmap:
                            nextQueue[i] = nextQueue[i].union(hashmap[c1+c2])
                if not nextQueue[i]:
                    return False
            queue = nextQueue
            level -= 1
        return True
    
    def test(self):
        testCases = [
            [ "XYZ", ["XYD", "YZE", "DEA", "FFF"], ],
            [ 'XXYX', ["XXX", "XXY", "XYX", "XYY", "YXZ"], ],
            [
                "CCC",
                ["CBB","ACB","ABD","CDB","BDC","CBC","DBA","DBB","CAB","BCB","BCC","BAA","CCD","BDD","DDD","CCA","CAA","CCC","CCB"]
            ],
        ]
        for bottom, allowed in testCases:
            print('bottom: %s' % bottom)
            print('allowed: %s' % allowed)
            result = self.pyramidTransition(bottom, allowed)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

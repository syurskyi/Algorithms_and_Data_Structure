'''
Created on Sep 4, 2017

@author: MT
'''
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        hashmap = {}
        for p, pp in zip(pid, ppid):
            hashset = hashmap.get(pp, set())
            hashset.add(p)
            hashmap[pp] = hashset
        if kill not in hashmap:
            return [kill]
        queue = list(hashmap[kill])
        result = set([kill])
        while queue:
            node = queue.pop(0)
            result.add(node)
            for node0 in hashmap.get(node, []):
                if node0 not in result:
                    queue.append(node0)
        return list(result)
    
    def test(self):
        testCases = [
            [
                [1, 3, 10, 5],
                [3, 0, 5,  3],
                5,
            ],
        ]
        for pid, ppid, kill in testCases:
            print('pid: %s' % pid)
            print('ppid: %s' % ppid)
            print('kill: %s' % kill)
            result = self.killProcess(pid, ppid, kill)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

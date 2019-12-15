'''
Created on Mar 27, 2018

@author: tongq
'''
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = ['0000']
        level = 0
        visited = set(['0000'])
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        while queue:
            n = len(queue)
            for _ in range(n):
                s = queue.pop(0)
                if s == target:
                    return level
                for i in range(4):
                    s01 = int(s[i])+1
                    if s01 >= 10:
                        s01 -= 10
                    s01 = str(s01)
                    s02 = int(s[i])-1
                    if s02 < 0:
                        s02 += 10
                    s02 = str(s02)
                    s0 = s[:i]+s01+s[i+1:]
                    if s0 not in visited and s0 not in deadends:
                        queue.append(s0)
                        visited.add(s0)
                    s0 = s[:i]+s02+s[i+1:]
                    if s0 not in visited and s0 not in deadends:
                        queue.append(s0)
                        visited.add(s0)
            level += 1
        return -1
    
    def test(self):
        testCases = [
            [
                ["0201","0101","0102","1212","2002"],
                "0202",
            ],
            [
                ["8888"],
                "0009",
            ],
            [
                ["8887","8889","8878","8898","8788","8988","7888","9888"],
                "8888",
            ],
            [
                ["0000"],
                "8888",
            ],
        ]
        for deadends, target in testCases:
            result = self.openLock(deadends, target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

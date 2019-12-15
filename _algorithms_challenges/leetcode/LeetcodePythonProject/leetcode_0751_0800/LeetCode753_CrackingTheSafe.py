'''
Created on Mar 28, 2018

@author: tongq
'''
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        total = k**n
        arr = ['0']*n
        visited = set(['0'*n])
        self.dfs(arr, total, visited, n, k)
        return ''.join(arr)
    
    def dfs(self, arr, goal, visited, n, k):
        if len(visited) == goal: return True
        prevArr = arr[len(arr)-n+1:]
        for i in range(k):
            nextArr = prevArr+[str(i)]
            nextStr = ''.join(nextArr)
            if nextStr not in visited:
                visited.add(nextStr)
                arr.append(str(i))
                if self.dfs(arr, goal, visited, n, k):
                    return True
                visited.remove(nextStr)
                arr.pop()
        return False
    
    def test(self):
        testCases = [
            [1, 2],
            [2, 2],
        ]
        for n, k in testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.crackSafe(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

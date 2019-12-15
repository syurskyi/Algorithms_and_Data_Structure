'''
Created on Jan 30, 2019

@author: tongq
'''
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        dfs = [0]
        seen = set(dfs)
        while dfs:
            i = dfs.pop()
            for j in rooms[i]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
                    if len(seen) == len(rooms):
                        return True
        return len(seen) == len(rooms)
    
    def test(self):
        testCases = [
            [[1],[2],[3],[]],
            [[1,3],[3,0,1],[2],[0]],
            [[2,3],[],[2],[1,3,1]],
            [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]],
        ]
        for rooms in testCases:
            print('rooms: %s' % rooms)
            res = self.canVisitAllRooms(rooms)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

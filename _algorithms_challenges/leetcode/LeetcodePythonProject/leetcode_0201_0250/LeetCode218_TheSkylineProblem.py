'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        import heapq
        heights = []
        for b in buildings:
            heights.append([b[0], -b[2]])
            heights.append([b[1], b[2]])
        heights.sort()
        heap = [0]
        res = []
        prev = 0
        for h in heights:
            if h[1] < 0:
                heapq.heappush(heap, h[1])
            else:
                heap.remove(-h[1])
                heapq.heapify(heap)
            curr = -heap[0]
            if curr != prev:
                res.append([h[0], curr])
            prev = curr
        return res
    
    def test(self):
        testCases = [
            [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ],
        ]
        for buildings in testCases:
            print('buildings: %s' % (buildings))
            result = self.getSkyline(buildings)
            print('result: %s' % (result))
            print('-='*20+'-')
    
if __name__ == '__main__':
    Solution().test()

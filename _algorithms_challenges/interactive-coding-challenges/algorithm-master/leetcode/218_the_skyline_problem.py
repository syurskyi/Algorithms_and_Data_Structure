"""
REF: https://briangordon.github.io/2014/08/the-skyline-problem.html
"""
import heapq


class HashHeapq:
    def __init__(self):
        self.heap = []
        self.deleted = {}

    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        if self.is_empty():
            return -1

        return heapq.heappop(self.heap)

    def remove(self, val):
        if self.is_empty():
            return

        if val not in self.deleted:
            self.deleted[val] = 0

        self.deleted[val] += 1

    def top(self):
        if self.is_empty():
            return -1

        return self.heap[0]

    def is_empty(self):
        while self.heap and self.deleted.get(self.heap[0]):
            val = heapq.heappop(self.heap)
            self.deleted[val] -= 1

        return not self.heap


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        if not buildings:
            return ans

        time = []

        for x, _x, height in buildings:
            time.append((x, height, True))
            time.append((_x, height, False))

        time.sort()
        heap = HashHeapq()

        for x, height, is_start in time:
            if is_start:
                heap.push(-height)
            else:
                heap.remove(-height)

            max_h = -heap.top() if not heap.is_empty() else 0

            if ans and ans[-1][0] == x:
                ans.pop()
            if ans and ans[-1][1] == max_h:
                continue
            ans.append([x, max_h])

        return ans

'''
Created on Apr 18, 2017

@author: MT
'''

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        graph = {}
        degree = {}
        for seq in seqs:
            length = len(seq)
            for i in range(length):
                if seq[i] not in graph:
                    graph[seq[i]] = []
                if seq[i] not in degree:
                    degree[seq[i]] = 0
                if i > 0:
                    graph[seq[i-1]].append(seq[i])
                    degree[seq[i]] += 1
        queue = []
        for key, val in degree.items():
            if val == 0:
                queue.append(key)
        index = 0
        while queue:
            size = len(queue)
            if size > 1:
                return False
            curr = queue.pop(0)
            if index >= len(org) or org[index] != curr:
                return False
            index += 1
            if curr in graph:
                for nextVal in graph[curr]:
                    degree[nextVal] -= 1
                    if degree[nextVal] == 0:
                        queue.append(nextVal)
        return index == len(org) and index == len(graph)

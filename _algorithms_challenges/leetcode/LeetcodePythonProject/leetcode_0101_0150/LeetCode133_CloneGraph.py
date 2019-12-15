'''
Created on Feb 8, 2017

@author: MT
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node
        newHead = UndirectedGraphNode(node.label)
        hashmap = {node:newHead}
        queue = [node]
        while queue:
            node = queue.pop(0)
            nodeCopy = hashmap[node]
            for node0 in node.neighbors:
                if node0 in hashmap:
                    nodeCopy.neighbors.append(hashmap[node0])
                else:
                    node0Copy = UndirectedGraphNode(node0.label)
                    hashmap[node0] = node0Copy
                    nodeCopy.neighbors.append(node0Copy)
                    queue.append(node0)
        return newHead

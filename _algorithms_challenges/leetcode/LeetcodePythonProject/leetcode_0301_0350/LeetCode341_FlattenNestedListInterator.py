'''
Created on Mar 20, 2017

@author: MT
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass

class NestedIterator(object):
    def __init__(self, nestedList):
        deque = nestedList
        result = []
        while deque:
            ni = deque.pop(0)
            if ni.isInteger():
                result.append(ni.getInteger())
            else:
                l = ni.getList()
                l.reverse()
                for ni0 in l:
                    deque.insert(0, ni0)
        self.result = result

    def next(self):
        return self.result.pop(0)

    def hasNext(self):
        if self.result:
            return True
        return False


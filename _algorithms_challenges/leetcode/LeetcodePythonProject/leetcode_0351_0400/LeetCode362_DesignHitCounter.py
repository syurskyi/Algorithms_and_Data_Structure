'''
Created on Mar 27, 2017

@author: MT
'''

class HitCounter(object):
    def __init__(self):
        self.hitCount = [0]*300
        self.timestampes = [0]*300
    
    def hit(self, timestamp):
        ind = timestamp % 300
        if timestamp != self.timestampes[ind]:
            self.hitCount[ind] = 1
            self.timestampes[ind] = timestamp
        else:
            self.hitCount[ind] += 1
    
    def getHits(self, timestamp):
        count = 0
        for i, time in enumerate(self.timestampes):
            if timestamp - time < 300:
                count += self.hitCount[i]
        return count

class HitCounterOwn(object):
    def __init__(self):
        self.queue = []
    
    def hit(self, timestamp):
        self.queue.append(timestamp)
        if self.queue and self.queue[0] < timestamp-300:
            self.queue.pop(0)
    
    def getHits(self, timestamp):
        start, end = 0, len(self.queue)
        target = timestamp - 300
        while start < end:
            mid = (start+end)/2
            if target >= self.queue[mid]:
                start = mid+1
            else:
                end = mid
        return len(self.queue)-end

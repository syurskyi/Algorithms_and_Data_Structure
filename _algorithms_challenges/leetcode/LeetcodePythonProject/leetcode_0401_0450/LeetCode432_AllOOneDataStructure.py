'''
Created on Apr 15, 2017

@author: MT
'''

class Bucket(object):
    def __init__(self, value):
        self.keySet = set()
        self.value = value
        self.next = None
        self.prev = None

class AllOne(object):
    def __init__(self):
        self.keyBucketMap = {}
        self.head = None
        self.tail = None
    
    def inc(self, key):
        if key in self.keyBucketMap:
            bucket = self.keyBucketMap[key]
            nextBucket = bucket.next
            if nextBucket and nextBucket.value == bucket.value+1:
                nextBucket.keySet.add(key)
                self.keyBucketMap[key] = nextBucket
            elif not nextBucket:
                nextBucket = Bucket(bucket.value+1)
                nextBucket.keySet.add(key)
                self.tail = nextBucket
                bucket.next = nextBucket
                self.keyBucketMap[key] = nextBucket
            else:
                newBucket = Bucket(bucket.value+1)
                newBucket.keySet.add(key)
                nextBucket.prev = newBucket
                newBucket.next = nextBucket
                bucket.next = newBucket
                newBucket.prev = bucket
                self.keyBucketMap[key] = newBucket
            bucket.keySet.remove(key)
            if not bucket.keySet:
                prevBucket = bucket.prev
                if prevBucket:
                    nextBucket = bucket.next
                    prevBucket.next = bucket.next
                    nextBucket.prev = prevBucket
                else:
                    nextBucket = bucket.next
                    nextBucket.prev = None
                    self.head = nextBucket
        else:
            if self.head:
                if self.head.value == 1:
                    self.head.keySet.add(key)
                else:
                    bucket = Bucket(1)
                    bucket.keySet.add(key)
                    self.head.prev = bucket
                    bucket.next = self.head
                    self.head = bucket
            else:
                bucket= Bucket(1)
                bucket.keySet.add(key)
                self.head = bucket
                self.tail = bucket
            self.keyBucketMap[key] = self.head
    
    def dec(self, key):
        if key in self.keyBucketMap:
            bucket = self.keyBucketMap[key]
            prevBucket = bucket.prev
            if prevBucket:
                if prevBucket.value+1 == bucket.value:
                    prevBucket.keySet.add(key)
                    self.keyBucketMap[key] = prevBucket
                else:
                    newBucket = Bucket(bucket.value-1)
                    newBucket.keySet.add(key)
                    newBucket.prev = prevBucket
                    newBucket.next = bucket
                    prevBucket.next = newBucket
                    bucket.prev = newBucket
                    self.keyBucketMap[key] = newBucket
            else:
                if bucket.value == 1:
                    del self.keyBucketMap[key]
                else:
                    newBucket = Bucket(bucket.value-1)
                    newBucket.keySet.add(key)
                    newBucket.next = bucket
                    bucket.prev = newBucket
                    self.head = newBucket
                    self.keyBucketMap[key] = newBucket
            bucket.keySet.remove(key)
            if not bucket.keySet:
                if not bucket.prev and not bucket.next:
                    self.head = None
                    self.tail = None
                elif bucket.prev and not bucket.next:
                    bucket.prev.next = None
                    self.tail = bucket.prev
                    bucket.prev = None
                elif bucket.next and not bucket.prev:
                    bucket.next.prev = None
                    self.head = bucket.next
                    bucket.next = None
                else:
                    bucket.next.prev = bucket.prev
                    bucket.prev.next = bucket.next
                    bucket.prev = None
                    bucket.next = None
        
    def getMax(self):
        if self.tail:
            val = self.tail.keySet.pop()
            self.tail.keySet.add(val)
            return val
        else:
            return ''
    
    def getMin(self):
        if self.head:
            val = self.head.keySet.pop()
            self.head.keySet.add(val)
            return val
        else:
            return ''
    
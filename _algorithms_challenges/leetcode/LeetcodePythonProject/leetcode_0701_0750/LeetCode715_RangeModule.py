'''
Created on Oct 29, 2017

@author: MT
'''
import bisect

class RangeModule(object):

    def __init__(self):
        self.X = [0, 10**9]
        self.track = [False]*2
    
    def addRangeHelper(self, left, right, track=True):
        def index(x):
            i = bisect.bisect_left(self.X, x)
            if self.X[i] != x:
                self.X.insert(i, x)
                self.track.insert(i, self.track[i-1])
            return i
        i = index(left)
        j = index(right)
        self.X[i:j] = [left]
        self.track[i:j] = [track]

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.addRangeHelper(left, right, True)

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i = bisect.bisect(self.X, left)-1
        j = bisect.bisect_left(self.X, right)
        return all(self.track[i:j])

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.addRangeHelper(left, right, False)

class Interval(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class RangeModule_own(object):
    def __init__(self):
        self.intervals = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        newInterval = Interval(left, right)
        res = []
        for interval in self.intervals:
            if newInterval.right < interval.left:
                res.append(newInterval)
                newInterval = interval
            elif interval.right < newInterval.left:
                res.append(interval)
            else:
                newInterval = Interval(min(interval.left, newInterval.left),\
                                    max(interval.right, newInterval.right))
        res.append(newInterval)
        self.intervals = res

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        newInterval = Interval(left, right)
        l, r = 0, len(self.intervals)-1
        while l <= r:
            mid = (l+r)//2
            if self.intervals[mid].left >= newInterval.right:
                r = mid-1
            elif self.intervals[mid].right <= newInterval.left:
                l = mid+1
            else:
                return self.intervals[mid].left <= newInterval.left and\
                    self.intervals[mid].right >= newInterval.right
        return False

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        newInterval = Interval(left, right)
        res = []
        for interval in self.intervals:
            if newInterval.right >= interval.right and newInterval.left <= interval.left:
                continue
            elif newInterval.right <= interval.right and newInterval.left >= interval.left:
                if interval.left != newInterval.left:
                    res.append(Interval(interval.left, newInterval.left))
                if interval.right != newInterval.right:
                    res.append(Interval(newInterval.right, interval.right))
            elif newInterval.right <= interval.left or interval.right <= newInterval.left:
                res.append(interval)
            elif newInterval.right <= interval.right:
                tmpInterval = Interval(newInterval.right, interval.right)
                if tmpInterval.left < tmpInterval.right:
                    res.append(tmpInterval)
            elif newInterval.left >= interval.left:
                tmpInterval = Interval(interval.left, newInterval.left)
                if tmpInterval.left < tmpInterval.right:
                    res.append(tmpInterval)
        self.intervals = res

if __name__ == '__main__':
#     rangeModule = RangeModule()
#     rangeModule.addRange(10, 20)
#     rangeModule.removeRange(14, 16)
#     print(rangeModule.queryRange(10, 14))
#     print(rangeModule.queryRange(13, 15))
#     print(rangeModule.queryRange(16, 17))
    
#     rangeModule = RangeModule()
#     print(rangeModule.addRange(6,8))
#     print(rangeModule.removeRange(7,8))
#     print(rangeModule.removeRange(8,9))
#     print(rangeModule.addRange(8,9))
#     print(rangeModule.removeRange(1,3))
#     print(rangeModule.addRange(1,8))
#     print(rangeModule.queryRange(2,4))
#     print(rangeModule.queryRange(2,9))
#     print(rangeModule.queryRange(4,6))

#     rangeModule = RangeModule()
#     print(rangeModule.queryRange(21,34))
#     print(rangeModule.queryRange(27,87))
#     print(rangeModule.addRange(44,53))
#     print(rangeModule.addRange(69,89))
#     print(rangeModule.queryRange(23,26))
#     print(rangeModule.queryRange(80,84))
#     print(rangeModule.queryRange(11,12))
#     print(rangeModule.removeRange(86,91))
#     print(rangeModule.addRange(87,94))
#     print(rangeModule.removeRange(34,52))
#     print(rangeModule.addRange(1,59))
#     print(rangeModule.removeRange(62,96))
#     print(rangeModule.removeRange(34,83))
#     print(rangeModule.queryRange(11,59))
#     print(rangeModule.queryRange(59,79))
#     print(rangeModule.queryRange(1,13))
#     print(rangeModule.queryRange(21,23))
#     print(rangeModule.removeRange(9,61))
#     print(rangeModule.addRange(17,21))
#     print(rangeModule.removeRange(4,8))
#     print(rangeModule.queryRange(19,25))
#     print(rangeModule.addRange(71,98))
#     print(rangeModule.addRange(23,94))
#     print(rangeModule.removeRange(58,95))
#     print(rangeModule.queryRange(12,78))
#     print(rangeModule.removeRange(46,47))
#     print(rangeModule.removeRange(50,70))
#     print(rangeModule.removeRange(84,91))
#     print(rangeModule.addRange(51,63))
#     print(rangeModule.removeRange(26,64))
#     print(rangeModule.addRange(38,87))
#     print(rangeModule.queryRange(41,84))
#     print(rangeModule.queryRange(19,21))
#     print(rangeModule.queryRange(18,56))
#     print(rangeModule.queryRange(23,39))
#     print(rangeModule.queryRange(29,95))
#     print(rangeModule.addRange(79,100))
#     print(rangeModule.removeRange(76,82))
#     print(rangeModule.addRange(37,55))
#     print(rangeModule.addRange(30,97))
#     print(rangeModule.addRange(1,36))
#     print(rangeModule.queryRange(18,96))
#     print(rangeModule.removeRange(45,86))
#     print(rangeModule.addRange(74,92))
#     print(rangeModule.queryRange(27,78))
#     print(rangeModule.addRange(31,35))
#     print(rangeModule.queryRange(87,91))
#     print(rangeModule.removeRange(37,84))
#     print(rangeModule.removeRange(26,57))
#     print(rangeModule.addRange(65,87))
#     print(rangeModule.addRange(76,91))
#     print(rangeModule.queryRange(37,77))
#     print(rangeModule.queryRange(18,66))
#     print(rangeModule.addRange(22,97))
#     print(rangeModule.addRange(2,91))
#     print(rangeModule.removeRange(82,98))
#     print(rangeModule.removeRange(41,46))
#     print(rangeModule.removeRange(6,78))
#     print(rangeModule.queryRange(44,80))
#     print(rangeModule.removeRange(90,94))
#     print(rangeModule.removeRange(37,88))
#     print(rangeModule.addRange(75,90))
#     print(rangeModule.queryRange(23,37))
#     print(rangeModule.removeRange(18,80))
#     print(rangeModule.addRange(92,93))
#     print(rangeModule.addRange(3,80))
#     print(rangeModule.queryRange(68,86))
#     print(rangeModule.removeRange(68,92))
#     print(rangeModule.queryRange(52,91))
#     print(rangeModule.addRange(43,53))
#     print(rangeModule.addRange(36,37))
#     print(rangeModule.addRange(60,74))
#     print(rangeModule.addRange(4,9))
#     print(rangeModule.addRange(44,80))
#     print(rangeModule.removeRange(85,93))
#     print(rangeModule.removeRange(56,83))
#     print(rangeModule.addRange(9,26))
#     print(rangeModule.queryRange(59,64))
#     print(rangeModule.queryRange(16,66))
#     print(rangeModule.removeRange(29,36))
#     print(rangeModule.removeRange(51,96))
#     print(rangeModule.removeRange(56,80))
#     print(rangeModule.addRange(13,87))
#     print(rangeModule.queryRange(42,72))
#     print(rangeModule.removeRange(6,56))
#     print(rangeModule.queryRange(24,53))
#     print(rangeModule.addRange(43,71))
#     print(rangeModule.removeRange(36,83))
#     print(rangeModule.removeRange(15,45))
#     print(rangeModule.queryRange(10,48))

    rangeModule = RangeModule()
    print(rangeModule.addRange(55,62))
    print(rangeModule.addRange(1,29))
    print(rangeModule.removeRange(18,49))
    print(rangeModule.queryRange(6,98))
    print(rangeModule.queryRange(59,71))
    print(rangeModule.removeRange(40,45))
    print(rangeModule.removeRange(4,58))
    print(rangeModule.removeRange(57,69))
    print(rangeModule.removeRange(20,30))
    print(rangeModule.removeRange(1,40))
    print(rangeModule.queryRange(73,93))
    print(rangeModule.removeRange(32,93))
    print(rangeModule.addRange(38,100))
    print(rangeModule.removeRange(50,64))
    print(rangeModule.addRange(26,72))
    print(rangeModule.queryRange(8,74))
    print(rangeModule.queryRange(15,53))
    print(rangeModule.addRange(44,85))
    print(rangeModule.addRange(10,71))
    print(rangeModule.queryRange(54,70))
    print(rangeModule.removeRange(10,45))
    print(rangeModule.queryRange(30,66))
    print(rangeModule.addRange(47,98))
    print(rangeModule.queryRange(1,7))
    print(rangeModule.removeRange(44,78))
    print(rangeModule.removeRange(31,49))
    print(rangeModule.addRange(62,63))
    print(rangeModule.addRange(49,88))
    print(rangeModule.removeRange(47,72))
    print(rangeModule.removeRange(8,50))
    print(rangeModule.removeRange(49,79))
    print(rangeModule.addRange(31,47))
    print(rangeModule.addRange(54,87))
    print(rangeModule.queryRange(77,78))
    print(rangeModule.queryRange(59,100))
    print(rangeModule.queryRange(8,9))
    print(rangeModule.queryRange(50,51))
    print(rangeModule.queryRange(67,93))
    print(rangeModule.removeRange(25,86))
    print(rangeModule.removeRange(8,92))
    print(rangeModule.queryRange(31,87))
    print(rangeModule.addRange(90,95))
    print(rangeModule.addRange(28,56))
    print(rangeModule.addRange(10,42))
    print(rangeModule.queryRange(27,34))
    print(rangeModule.addRange(75,81))
    print(rangeModule.addRange(17,63))
    print(rangeModule.removeRange(78,90))
    print(rangeModule.addRange(9,18))
    print(rangeModule.queryRange(51,74))
    print(rangeModule.removeRange(20,54))
    print(rangeModule.addRange(35,72))
    print(rangeModule.queryRange(2,29))
    print(rangeModule.addRange(28,41))
    print(rangeModule.addRange(17,95))
    print(rangeModule.addRange(73,75))
    print(rangeModule.queryRange(34,43))
    print(rangeModule.addRange(57,96))
    print(rangeModule.queryRange(51,72))
    print(rangeModule.removeRange(21,67))
    print(rangeModule.removeRange(40,73))
    print(rangeModule.removeRange(14,26))
    print(rangeModule.removeRange(71,86))
    print(rangeModule.queryRange(34,41))
    print(rangeModule.removeRange(10,25))
    print(rangeModule.queryRange(27,68))
    print(rangeModule.queryRange(18,32))
    print(rangeModule.removeRange(30,31))
    print(rangeModule.queryRange(45,61))
    print(rangeModule.addRange(64,66))
    print(rangeModule.addRange(18,93))
    print(rangeModule.queryRange(13,21))
    print(rangeModule.removeRange(13,46))
    print(rangeModule.removeRange(56,99))
    print(rangeModule.queryRange(6,93))
    print(rangeModule.addRange(25,36))
    print(rangeModule.removeRange(27,88))
    print(rangeModule.removeRange(82,83))
    print(rangeModule.addRange(30,71))
    print(rangeModule.addRange(31,73))
    print(rangeModule.addRange(10,41))
    print(rangeModule.queryRange(71,72))
    print(rangeModule.queryRange(9,56))
    print(rangeModule.addRange(22,76))
    print(rangeModule.queryRange(38,74))
    print(rangeModule.removeRange(2,77))
    print(rangeModule.queryRange(33,61))
    print(rangeModule.removeRange(74,75))
    print(rangeModule.addRange(11,43))
    print(rangeModule.queryRange(27,75))

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.arr = []
        hashmap = {}
        maxNum = 0
        maxP = None
        for p, t in zip(persons, times):
            hashmap[p] = hashmap.get(p, 0)+1
            if hashmap[p] >= maxNum:
                maxP = p
                maxNum = hashmap[p]
            self.arr.append([t, maxP])

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        i, j = 0, len(self.arr)
        while i < j:
            mid = (i+j)//2
            if t < self.arr[mid][0]:
                j = mid
            else:
                i = mid+1
        return self.arr[i-1][1]


if __name__ == '__main__':
    candidate = TopVotedCandidate(
        [0,  1, 0, 1, 1],
        [24,29,31,76,81]
    )
    # [28],[24],[29],[77],[30],[25],[76],[75],[81],[80]
    print(candidate.q(28))
    print(candidate.q(24))
    print(candidate.q(29))
    print(candidate.q(77))
    print(candidate.q(30))
    print(candidate.q(25))
    print(candidate.q(76))
    print(candidate.q(75))
    print(candidate.q(81))
    print(candidate.q(80))

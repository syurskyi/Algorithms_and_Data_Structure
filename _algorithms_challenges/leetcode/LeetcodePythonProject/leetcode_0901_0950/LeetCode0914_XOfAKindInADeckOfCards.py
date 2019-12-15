class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if not deck: return False
        hashmap = {}
        for num in deck:
            hashmap[num] = hashmap.get(num, 0)+1
        counts = list(hashmap.values())
        minVal = min(hashmap.values())
        while counts:
            if 1 in counts:
                return False
            counts = [c - minVal for c in counts if c > minVal]
        return True

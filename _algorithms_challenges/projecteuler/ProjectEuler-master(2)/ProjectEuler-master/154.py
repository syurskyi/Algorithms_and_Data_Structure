import sys

class Problem():
    def __init__(self):
        self.bound = 200000
        self.min_bound = self.bound // 3
        self.factor2 = self._init_factor(2)
        self.factor5 = self._init_factor(5)
    
    def _init_factor(self, factor):
        rv = [0] * (self.bound + 1)
        d = factor
        while d <= self.bound:
            for i in range(d, self.bound + 1, d):
                rv[i] += 1
            d *= factor
        for i in range(1, self.bound + 1):
            rv[i] += rv[i-1]
        return rv
    
    def solve(self):
        count = 0
        for a in range(self.min_bound + 1):
            b = a
            c = self.bound - a - b
            if self._has_multiples(a, b, c):
                count += 3
            for b in range(a + 1, self.bound + 1):
                c = self.bound - a - b
                if c < b:
                    break
                if self._has_multiples(a, b, c):
                    if c == b:
                        count += 3
                    else:
                        count += 6
            print(a, count)
    
    def _has_multiples(self, a, b, c):
        if 199982 < self.factor2[a] + self.factor2[b] + self.factor2[c]:
            return False
        if 49986 < self.factor5[a] + self.factor5[b] + self.factor5[c]:
            return False
        return True
        
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

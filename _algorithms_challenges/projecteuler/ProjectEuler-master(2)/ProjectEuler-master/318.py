import math
import sys

class Problem():
    def __init__(self):
        self.bound = 2011

    def solve(self):
        rv = 0
        for p in range(1, self.bound + 1):
            for q in range(p+1, self.bound + 1 - p):
                if math.sqrt(q) - math.sqrt(p) < 1:
                    rv += self.N(p, q, self.bound)
        print(rv)
        
    def C(self, p, q, n):
        return math.floor(-2 * n * math.log(math.sqrt(q) - math.sqrt(p), 10))

    def N(self, p, q, n):
        rv = math.ceil(-n/math.log(math.sqrt(q) - math.sqrt(p), 10))
        rv = (rv + rv % 2) // 2
        assert(self.C(p, q, rv) >= n)
        assert(self.C(p, q, rv - 1) < n)
        return rv
        
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

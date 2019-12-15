import bisect
import math
import sys

class GolombSelfDescribingSequence():
    def __init__(self):
        self.value_bound = 20000000
        self.g = [0 for _ in range(self.value_bound)]
        self.g_sum = [0 for _ in range(self.value_bound)]
        self.aux = [0 for _ in range(self.value_bound)]
        self.g[1] = 1
        self.g_sum[1] = 1
        self.aux[1] = 1
        for i in range(2, self.value_bound):
            self.g[i] = 1 + self.g[i - self.g[self.g[i - 1]]]
            self.g_sum[i] = self.g_sum[i - 1] + self.g[i]
            self.aux[i] = self.aux[i - 1] + i * self.g[i]

    def get(self, n):
        k = bisect.bisect_left(self.aux, n)
        if k == self.value_bound:
            raise Exception("Precalculated tables are too small", n)
        return self.g_sum[k-1] + math.ceil((n - self.aux[k-1]) / k)

class Problem():
    def __init__(self):
        self.sequence = GolombSelfDescribingSequence()
    
    def solve(self):
        print(self.sequence.get(1000))
        print(self.get(10**3))
        print(self.get(10**6))
    
    def get(self, bound):
        rv = 0
        for n in range(1, bound):
            g = self.sequence.get(n**3)
            rv += g
            if n % 10000 == 0:
                print(n, n**3, g)
        return rv

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())


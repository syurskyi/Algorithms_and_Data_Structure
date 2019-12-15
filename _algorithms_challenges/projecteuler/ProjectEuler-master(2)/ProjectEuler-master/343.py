from fractions import gcd
import sys

class PrimeTable():
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()
    
    def _sieve(self):
        visited = [False] * (self.bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, self.bound + 1):
            if not visited[i]:
                self.primes.append(i)
            for j in range(i + i, self.bound + 1, i):
                visited[j] = True
        print('Prime count:', len(self.primes))

class Problem():
    def __init__(self):
        self.primes = PrimeTable(10000000).primes
    
    def solve(self):
        self.get(100)
        self.get(2 * 10**6)
    
    def get(self, bound):
        results = 0
        for k in range(1, bound + 1):
            f = self.get_f(k**3)
            if k % 1000 == 0:
                print(k, f)
            results += f
        print(results)
        
    def get_f(self, n):
        x, y = 1, n
        while y != 1:
            z = x + y
            d = self._get_smallest_nontrivial_divisor(z)
            if d == z:
                return d - 1
            x, y = 1, z // d - 1
        return x

    def _get_smallest_nontrivial_divisor(self, n):
        for d in self.primes:
            if n < d * d:
                return n
            if n % d == 0:
                return d
        for d in range(self.primes[-1], n + 1, 2):
            if n < d * d:
                return n
            if n % d == 0:
                return d

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

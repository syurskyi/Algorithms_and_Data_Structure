import math
import sys

class Problem():
    def __init__(self):
        self.cache = { 
            0: 0,
            1: 1,
        }
    
    def solve(self):
        print(self.get(10**12))
        
    def get(self, n):
        return self.oeis_org_A006046((n - 2) // 4 + 1)
    
    def oeis_org_A006046(self, n):
        if n not in self.cache:     
            q, r = divmod(n, 2)
            if r == 0:
                results = 3 * self.oeis_org_A006046(q)
                self.cache[n] = results
            else:
                results = 2 * self.oeis_org_A006046(q) + self.oeis_org_A006046(q + 1)
                self.cache[n] = results
        return self.cache[n]    
    
    def get_naive(self, n):
        count = 0
        for i in range(1, n, 2):
            for k in range(1, i + 1, 2):
                if self.f(i, k) % 2 == 1:
                    count += 1
        return count
                    
    def f(self, n, k):
        results = 0
        for i in range(1, k + 1, 2):
            if n // 2 + 1 >= i and n // 2 >= k - i:
                results += self.c(n // 2 + 1, i) * self.c(n // 2, k - i) 
        return results
    
    def c(self, n, k):
        return math.factorial(n) // math.factorial(k) // math.factorial(n - k)
    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

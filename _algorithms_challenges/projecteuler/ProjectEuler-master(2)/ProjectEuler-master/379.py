import math
import sys

class MobiusFunction():
    def get(self, n):
        visited = [False for _ in range(n + 1)]
        sqrt_n = int(math.sqrt(n)) + 1 
        for i in range(2, sqrt_n + 1):
            if not visited[i]:
                for j in range(2 * i, n + 1, i):
                    visited[j] = True

        mu = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            if not visited[i]:
                for j in range(i, n + 1, i):
                    mu[j] *= -1
                i2 = i**2
                for j in range(i2, n + 1, i2):
                    mu[j] = 0
        return mu

class Problem():
    def solve(self):
        for n in [10**6, 10**12]:
            print(n, '=>', self.get(n))

    def get(self, n):
        sqrt_n = int(math.sqrt(n))
        mu = MobiusFunction().get(sqrt_n + 1)
        result = 0
        for d in range(1, sqrt_n + 1):
            if mu[d] == 0:
                continue
            for i in range(1, (sqrt_n + d) // d):
                m = n // (d**2 * i)
                summation = self.floor_summation(m, i, m)
                result += summation * mu[d]
        return result

    def floor_summation(self, n, begin_k, end_k):
        result = 0
        k = begin_k
        k_bound = min(end_k, n)
        while k < k_bound + 1:
            m = n // k
            boost_k = min((n // m), k_bound)
            result += m * (boost_k - k + 1)
            k = boost_k + 1
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

import math
import sys

class MobiusFunction():
    def __init__(self, n):
        self.mu = self.__init_mu(n)

    def __init_mu(self, n):
        sieve = [False for i in range(n + 1)]
        for i in range(2, n + 1):
            i2 = i**2
            if i2 > n:
                break
            for j in range(i2, n + 1, i2):
                sieve[j] = True
        mu = [q for q in range(1, len(sieve)) if not sieve[q]]
        print("Squarefree number count =>", len(mu))
        return mu

class Problem():
    def solve(self):
        print(self.get(10**9))

    def get(self, L):
        function = MobiusFunction(L // 6)
        result = 0
        for q in function.mu:
            if 12 * q > L:
                result += 6 * q
            else:
                n = 2
                while True:
                    if n * (n+1) * q > L:
                        break
                    m_begin = n + 1
                    m_end = min(2 * n - 1, L // (n * q))
                    result += n * q * (m_end + m_begin) * (m_end - m_begin + 1) // 2
                    n += 1
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

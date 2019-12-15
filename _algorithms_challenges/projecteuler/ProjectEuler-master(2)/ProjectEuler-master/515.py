import math
import sys

class ExtendedGCD():
    def solve(a, b):
        x, y = 0, 1
        last_x, last_y = 1, 0
        while b != 0:
            q, r = divmod(a, b)
            a, b = b, r
            x, last_x = last_x - q * x, x
            y, last_y = last_y - q * y, y
        return last_x, last_y

# Solve ax = 1 (mod m).
class ModInverse():
    def solve(a, m):
        x, y = ExtendedGCD.solve(a, m)
        return x % m

class Primes():
    def get(self, begin, end):
        basic_primes = self.__get_basic_primes(int(math.sqrt(end)) + 1)
        visited = [False for _ in range(end - begin + 1)]
        for p in basic_primes:
            reduced_begin = begin % p
            i0 = 0
            if reduced_begin != 0:
                i0 = p - reduced_begin
            for i in range(i0, end - begin + 1, p):
                visited[i] = True
        primes = []
        for i in range(end - begin + 1):
            if not visited[i]:
                primes.append(begin + i)
        return primes

    def __get_basic_primes(self, n):
        primes = []
        visited = [False for _ in range(n + 1)]
        for i in range(2, n + 1):
            if not visited[i]:
                primes.append(i)
                for j in range(i + i, n + 1, i):
                    visited[j] = True
        return primes

class Problem():
    def solve(self):
        self.benchmark()
        print(self.D(10**9, 10**5, 10**5))

    def benchmark(self):
        assert(self.D(101, 1, 10) == 45)
        assert(self.D(10**3, 10**2, 10**2) == 8334)
        assert(self.D(10**6, 10**3, 10**3) == 38162302)

    def D(self, a, b, k):
        primes = Primes().get(a, a + b - 1)
        result = 0
        for p in primes:
            result += ModInverse.solve(k - 1, p)
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

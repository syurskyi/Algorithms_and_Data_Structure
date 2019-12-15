import fractions
import itertools
import math
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

class Factorization():
    def __init__(self):
        self.prime_table = PrimeTable(3000)
    
    def get(self, n):
        d = n
        f = {}
        for p in self.prime_table.primes:
            if d == 1 or p > d:
                break
            e = 0
            while d % p == 0:
                d = d // p
                e += 1
            if e > 0:
                f[p] = e
        if d > 1:
            f[d] = 1
            #raise Exception('prime factor should be small', d)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])

    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result

class Problem():
    def __init__(self):
        self.factorization = Factorization()
        self.primes = self.factorization.prime_table.primes

    def solve(self):
        print(self.get(1000))

    def get(self, m_bound):
        rv = 0
        for m in range(1, m_bound + 1):
            count = self.get_count(m)
            rv += count
            print('ratio, acc, curr:', m, rv, count)
        return rv

    def get_count(self, m):
        rv = 0
        performance_counter = 0
        hashed_triangles = set()
        u_list = self.factorization.get(2*m)
        #print(m, u_list)
        for u in u_list:
            for v in range(1, int(math.sqrt(3)*u) + 1):
                if fractions.gcd(u, v) != 1:
                    continue
                d = 4 * m**2 * (u**2 + v**2)
                delta_list = self.factorization.get(d)
                for delta1 in delta_list:
                    if delta1**2 > d:
                        break
                    delta2 = d // delta1
                    q1, r1 = divmod(delta1 + 2*m*u, v)
                    q2, r2 = divmod(delta2 + 2*m*u, v)
                    if r1 != 0 or r2 != 0:
                        continue
                    t = sorted([q1 + (2*m*v) // u, q2 + (2*m*v) // u, q1 + q2])
                    hashed_key = self._hash_triangle(t)
                    if hashed_key not in hashed_triangles:
                        hashed_triangles.add(hashed_key)
                        rv += sum(t)
                        performance_counter += 1
                        if performance_counter % 10000 == 0:
                            print('internal:', rv, t, hashed_key)
        return rv

    def _hash_triangle(self, t):
        a, b, c = t
        return '''%d|%d|%d''' % (a, b, c)

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
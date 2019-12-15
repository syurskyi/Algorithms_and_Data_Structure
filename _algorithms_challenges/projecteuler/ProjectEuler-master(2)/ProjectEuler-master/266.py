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
        self.prime_table = PrimeTable(190)
    
    def factorize(self, n):
        d = n
        rv = []
        for i in range(len(self.prime_table.primes)):
            p = self.prime_table.primes[i]
            if d == 1 or p > d:
                break
            count = 0
            while d % p == 0:
                d = d // p
                count += 1
            if count > 0:
                rv += [p] * count
        if d > 1:
            rv.append(d)
        return rv

class Problem():
    def __init__(self):
        self.factorization = Factorization()
        self.primes = self.factorization.prime_table.primes
        self.lower_half_array = None
        self.upper_half_array = None

    def solve(self):
        print(self.pseudo_square_root(self.factorization.factorize(12)))
        print(self.pseudo_square_root(self.factorization.factorize(3102)))
        print(self.pseudo_square_root(self.primes))

    def pseudo_square_root(self, prime_factors):
        upper_bound = self.get_upper_bound(prime_factors)
        half_len = len(prime_factors) // 2
        self.lower_half_array = self.populate(prime_factors[:half_len], upper_bound)
        self.upper_half_array = self.populate(prime_factors[half_len:], upper_bound)
        best_so_far = 0
        for n in self.lower_half_array:
            x = self.binary_search(n, upper_bound)
            if x > best_so_far:
                best_so_far = x
                print('Current best:', n, x, best_so_far)
        return best_so_far % 10**16

    def binary_search(self, n, upper_bound):
        L = 0
        U = len(self.upper_half_array) - 1
        while L <= U:
            M = (L + U) // 2
            if self.upper_half_array[M] * n < upper_bound:
                L = M + 1
            else:
                U = M - 1
        return self.upper_half_array[U] * n

    def get_upper_bound(self, n):
        product = 1
        for i in n:
            product *= i
        return int(math.sqrt(product)) + 1

    def populate(self, prime_factors, upper_bound):
        rv = [1]
        for d in prime_factors:
            next = [d * x for x in rv if d * x < upper_bound]
            rv += next
        rv.sort()
        return rv

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
import itertools
import math
import sys

class Problem():
    def __init__(self):
        self.primes = []
        self.binomial_coefficients = {}
        
        self._init_primes()
        self._init_binomial_coefficients()
        
    def solve(self):
        n = len(self.primes)
        rv = 0
        for i in range(n):
            p = self.primes[i]
            a = self.binomial_coefficients[p]
            print('Current prime p with sum:', p, rv)
            for j in range(i+1, n):
                q = self.primes[j]
                b = self.binomial_coefficients[q]
                x = self._solve_equations(a, p, b, q)
                for k in range(j+1, n):
                    r = self.primes[k]
                    c = self.binomial_coefficients[r]
                    y = self._solve_equations(x, p*q, c, r)
                    rv += y
        print(rv)
            
    def _init_primes(self):
        sieve_range = 5000
        visited = [False] * sieve_range
        visited[0] = visited[1] = True
        for i in range(2, sieve_range):
            if not visited[i]:
                if i > 1000:
                    self.primes.append(i)
                for j in range(i+i, sieve_range, i):
                    visited[j] = True
        print('Prime count:', len(self.primes))
    
    def _init_binomial_coefficients(self):
        m = 10**18
        n = 10**9
        for p in self.primes:
            self.binomial_coefficients[p] = self._combination_number(m, n, p)

    def _combination_number(self, m, n, prime):
        m_rep = self._base_convert(m, prime)
        n_rep = self._base_convert(n, prime)
        len_diff = len(m_rep) - len(n_rep)
        n_rep += [0] * len_diff
        rv = 1
        for i, j in zip(m_rep, n_rep):
            if i < j:
                rv = 0
                break
            curr_c = math.factorial(i) // math.factorial(j) // math.factorial(i-j)
            rv = (rv * curr_c) % prime
        return rv

    def _base_convert(self, number, base):    
        d = number
        rv = []
        while d > 0:
            d, r = divmod(d, base)
            rv.append(r)
        return rv        
        
    def _solve_equations(self, a, m, b, n):
        q = m*n
        (x, y) = self._extended_gcd(m, n)
        root = a + (b - a) * x * m
        return ((root % q) + q) % q
                    
    def _extended_gcd(self, a, b):
        (x, y) = (0, 1)
        (last_x, last_y) = (1, 0)
        while b != 0:
            (q, r) = divmod(a, b);
            (a, b) = (b, r)
            (x, last_x) = (last_x - q * x, x)
            (y, last_y) = (last_y - q * y, y)
        return (last_x, last_y)    
            
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

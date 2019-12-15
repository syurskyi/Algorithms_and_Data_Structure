import sys

class Problem():
    def __init__(self):
        self.primes = None       
        self._init_primes(10**7)
        
    def solve(self):
        sr = 0
        for p in self.primes:
            if p == 2 or p == 13:
                continue
            n = self._solve_by_number_theory(13, p)
            sr += n
        print('Fast =>', sr)
        
    def _init_primes(self, sieve_range):
        self.primes = [] 
        visited = [False] * sieve_range
        visited[0] = visited[1] = True
        for i in range(2, sieve_range):
            if not visited[i]:
                self.primes.append(i)
                for j in range(i+i, sieve_range, i):
                    visited[j] = True
        print('Prime count:', len(self.primes))
    
    def _solve_by_number_theory(self, n, p):
        x0 = self._cipolla_algorithm(n, p)
        if x0 is None:
            return 0
        x = (self._hensel_lemma(x0, n, p) + 3) * ((p**2+1) // 2) % (p**2)
        y = (self._hensel_lemma(p - x0, n, p) + 3) * ((p**2+1) // 2) % (p**2)
        return min(x, y)
        
    def _cipolla_algorithm(self, n, p):
        if self._legendre_symbol(n, p) != 1:
            return None
        a = self._cipolla_algorithm_find_a(n, p)
        x = self._cipolla_algorithm_compute_x(a, n, p)
        return x
    
    def _hensel_lemma(self, x, n, p):
        return (x * ((p**2+1) // 2) + n * self._mod_inverse(2*x, p**2)) % (p**2)
        
    def _cipolla_algorithm_find_a(self, n, p):
        for a in range(p):
            if self._legendre_symbol(a**2 - n, p) != 1:
                return a
    
    def _cipolla_algorithm_compute_x(self, a, n, p):
        d = a**2 - n
        q = (p+1) // 2        
        b = [a, 1]
        x = [1, 0]
        while q > 0:
            if q & 1 != 0:
                x = [(x[0]*b[0] + d*x[1]*b[1]) % p, (x[0]*b[1] + x[1]*b[0]) % p] 
            b = [(b[0]**2 + d * b[1]**2) % p, (2*b[0]*b[1]) % p]
            q >>= 1
        return x[0]
    
    def _legendre_symbol(self, a, p):
        return pow(a % p, (p-1)//2, p)

    def _mod_inverse(self, a, m):
        g, x, y = self._extended_gcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def _extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)        
            
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

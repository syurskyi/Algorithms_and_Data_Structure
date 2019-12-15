import sys

class Problem():
    def __init__(self):
        self.SIEVE_RANGE = 2 * 10**7 + 1
        self.power2 = set()
        self.primes = []        
        self._init_power2()
        self._sieve()
            
    def solve(self):
        rv = 0
        for i in range(3, self.SIEVE_RANGE):
            max_root = self._get_max_root(i)
            rv += max_root
            if i % 10000 == 0:
                print('''Current number: %d => %d''' % (i, max_root))
        print(rv)

    def _init_power2(self):
        d = 8
        while d < self.SIEVE_RANGE:
            self.power2.add(d)
            d *= 2
            
    def _sieve(self):
        visited = [False] * self.SIEVE_RANGE
        for i in range(2, self.SIEVE_RANGE):
            if visited[i] is False:
                self.primes.append(i)
                for j in range(i+i, self.SIEVE_RANGE, i):
                    visited[j] = True
        print('''sieve completed, the last prime is %d''' % self.primes[-1])
        
    def _get_max_root(self, n):
        d = n
        m = 1
        roots = set([n-1, 1])
        for prime in self.primes:
            if prime * prime > d:
                break
            if d % prime != 0:
                continue
            power_prime = 1
            while d % prime == 0:
                power_prime *= prime
                d = int(d/prime)
            curr_roots = set()
            power_prime_roots = [power_prime-1, 1]
            if power_prime in self.power2:
                power_prime_roots += [power_prime//2 + 1, power_prime//2 - 1]
            for a in power_prime_roots:
                for b in roots:
                    curr_roots.add(self._solve_equations(a, power_prime, b, m))
            roots = curr_roots
            m *= power_prime
        if d > 1:
            curr_roots = set()
            d_roots = [d-1, 1]
            if d in self.power2:
                d_roots += [d//2 + 1, d//2 - 1]
            for a in d_roots:
                for b in roots:
                    curr_roots.add(self._solve_equations(a, d, b, m))
            roots = curr_roots
        roots.remove(n-1)
        return max(roots)
    
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

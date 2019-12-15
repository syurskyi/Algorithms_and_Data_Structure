import sys

class PrimeTable():
    def get(self, sieve_range):
        primes = []
        visited = [False] * sieve_range
        visited[0] = visited[1] = True
        for i in range(2, sieve_range):
            if not visited[i]:
                primes.append(i)
                for j in range(2*i, sieve_range, i):
                    visited[j] = True
        return primes
        
class CipollaAlgorithm():
    def execute(self, n, p):
        if p == 2:
            return None
        if self._legendre_symbol(n, p) != 1:
            return None
        a = self._find_a(n, p)
        x = self._compute_x(a, n, p)
        return x
            
    def _legendre_symbol(self, a, p):
        return pow(a % p, (p - 1) // 2, p)    

    def _find_a(self, n, p):
        for a in range(p):
            if self._legendre_symbol(a**2 - n, p) != 1:
                return a
        
    def _compute_x(self, a, n, p):
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

class Factorization():
    def __init__(self, primes):
        self.primes = primes
    
    def factorize(self, n):
        d = n
        rv = []
        for i in range(len(self.primes)):
            p = self.primes[i]
            if d == 1 or p * p > d:
                break
            if d % p == 0:
                rv.append(p)
            while d % p == 0:
                d = d // p
        if d > 1:
            rv.append(d)
        return rv
        
class Problem():
    def __init__(self):
        self.primes = None
        self.factorization = None
        
    def solve(self):
        self.get_sum(10000)
        self.get_sum(100000000)

    """
    If x is a primitive root of p, then x^n + x^{n+1} = x^{n+2} (mod p) 
    if and only if x^2 - x - 1 = 0 (mod p) or (2x - 1)^2 = 5 (mod p)
    """
    def get_sum(self, range):
        self.primes = PrimeTable().get(range)
        self.factorization = Factorization(self.primes)
        solution_sum = 5 
        solution_count = 0
        for p in self.primes:
            if self.has_fibonacci_primitive_root(p):
                solution_sum += p
                solution_count += 1
                if solution_count % 1000 == 0:
                    print(p, solution_count, solution_sum)
        print(solution_sum)
    
    def has_fibonacci_primitive_root(self, p):
        if p % 10 != 1 and p % 10 != 9:
            return False
        y = CipollaAlgorithm().execute(5, p)
        if not y:
            return False
        if y % 2 == 0:
            y = p - y
        x_list = [((y + 1) // 2) % p, ((-y + 1) // 2) % p]
        g_list = self.factorization.factorize(p-1)
        for x in x_list:
            is_primitive = True
            for g in g_list:
                if pow(x, p // g, p) == 1:
                    is_primitive = False
                    break
            if is_primitive:
                return True
        return False
    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

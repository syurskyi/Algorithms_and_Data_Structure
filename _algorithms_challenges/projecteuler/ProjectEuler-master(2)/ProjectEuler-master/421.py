import fractions
import sys

"""
http://math.stackexchange.com/questions/158344/how-to-find-the-solutions-for-the-n-th-root-of-unity-in-modular-arithmetic
http://math.stackexchange.com/questions/156213/practical-method-of-calculating-primitive-roots-modulo-a-prime
"""
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

class Factorization():
    def __init__(self, primes):
        self.primes = primes
    
    def get_prime_factors(self, n):
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
        
class PrimitiveRootFinder():
    def __init__(self, primes):
        self.primes = primes
        self.factorization = Factorization(primes)

    def find(self, prime):
        phi = prime - 1
        prime_factors = self.factorization.get_prime_factors(phi)
        for x in range(1, prime):
            is_primitive = True
            for factor in prime_factors:
                if pow(x, phi // factor, prime) == 1:
                    is_primitive = False
                    break
            if is_primitive:
                return x
        return None
        
class Problem():
    def __init__(self):
        self.primes = None
        self.finder = None
    
    def solve(self):
        print(self.get_sum(10**11, 10**8))

    def get_sum(self, n, m):
        self.primes = PrimeTable().get(m)
        self.finder = PrimitiveRootFinder(self.primes)
        results = 0
        performance_counter = 0
        for prime in self.primes:
            x_array = self.solve_equation(prime)
            performance_counter += 1
            if performance_counter % 1000 == 0:
                print(prime, x_array)
            for x in x_array:
                results += prime * self.get_count(x, n, prime)
        return results
    
    """
    Solve x^15 + 1 = 0 (mod p) where p is prime.
    x^15 + 1 = 0 (mod p) <=> (-x)^15 = 1 (mod p).
    """
    def solve_equation(self, prime):
        d = fractions.gcd(15, prime - 1)
        g = self.finder.find(prime)
        h = pow(g, (prime - 1) // d, prime)
        solutions = [prime - pow(h, t, prime) for t in range(d)]
        solutions.sort()
        return solutions

    def get_count(self, first_term, upper_bound, common_difference):
        if first_term > upper_bound:
            return 0
        return (upper_bound - first_term) // common_difference + 1

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
import fractions
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

class Factorization():
    def __init__(self, primes):
        self.primes = primes
        self.max_prime = primes[-1]
    
    def get_prime_factors(self, n):
        assert(self.max_prime**2 > n)
        d = n
        prime_factors = []
        for i in range(len(self.primes)):
            p = self.primes[i]
            if d == 1 or p * p > d:
                break
            if d % p == 0:
                prime_factors.append(p)
            while d % p == 0:
                d = d // p
        if d > 1:
            prime_factors.append(d)
        return prime_factors

class Problem():
    def __init__(self):
        self.primes = PrimeTable().get(10**8)
        self.factorization = Factorization(self.primes)
        print('Init completed.')
    
    def solve(self):
        for n in [10**3, 10**6, 10**15]:
            print(n, self.get_g(n))

    def get_g(self, n):
        k = 5
        g = 13
        while True:
            prime_factors = self.factorization.get_prime_factors(g - k)
            d = sys.maxsize
            for prime_factor in prime_factors:
                mod_k = k % prime_factor
                if mod_k == 0:
                    d = 0
                    break
                else:
                    d = min(d, prime_factor - mod_k)
            if k + d + 1 >= n:
                break
            g += d + fractions.gcd(k + d, g + d)
            k += d + 1
        return g + n - k + 1

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

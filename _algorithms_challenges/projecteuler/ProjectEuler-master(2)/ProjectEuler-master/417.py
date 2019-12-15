import fractions
import sys

class Factorization():
    def __init__(self, sieve_range):
        self.results = [[] for _ in range(sieve_range + 1)]
        for i in range(2, sieve_range + 1):
            if len(self.results[i]) == 0:
                for j in range(i, sieve_range + 1, i):
                    self.results[j].append(i)
    
    def get_prime_factors(self, n):
        return self.results[n]

class PhiFunction():
    def __init__(self, factorization):
        self.factorization = factorization
        self.cache = {}
    
    def get(self, n):
        if n in self.cache:
            return self.cache[n]
        results = n
        for prime in self.factorization.get_prime_factors(n):
            results = results // prime * (prime - 1)
        self.cache[n] = results
        return results

"""
Algorithm: http://mathforum.org/library/drmath/view/67018.html
Small benchmark dataset: https://oeis.org/A051626/b051626.txt
"""
class Problem():
    def __init__(self):
        self.factorization = None
        self.phi_function = None
        self.cycle_length_cache = {}
    
    def solve(self):
        print(self.get_sum(100000000))
    
    def get_sum(self, n):
        self.factorization = Factorization(n)
        self.phi_function = PhiFunction(self.factorization)
        results = 0
        for i in range(1, n + 1):
            length = self.get_cycle_length(i)
            results += length
            if i % 10001 == 0:
                print(i, length, results)
        return results
    
    def get_cycle_length(self, n):
        m = self.reduce_n(n)
        if m == 1:
            return 0
        if m in self.cycle_length_cache:
            return self.cycle_length_cache[m]
        d = self.phi_function.get(m)
        while True:
            prime_factors = self.factorization.get_prime_factors(d)
            found = True
            for x in prime_factors:
                if pow(10, d // x, m) == 1:
                    d = d // x
                    found = False
                    break
            if found:
                self.cycle_length_cache[m] = d
                return d

    def reduce_n(self, n):
        d = n
        while d % 2 == 0:
            d = d // 2
        while d % 5 == 0:
            d = d // 5
        return d

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
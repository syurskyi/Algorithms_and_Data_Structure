import sys

class FactorizationTable():
    def get(self, sieve_range):
        table = [{} for _ in range(sieve_range + 1)]
        for i in range(2, sieve_range + 1):
            if not table[i]:
                for j in range(i, sieve_range + 1, i):
                    table[j][i] = 1
                prime_power = i**2
                while prime_power <= sieve_range:
                    for j in range(prime_power, sieve_range + 1, prime_power):
                        table[j][i] += 1
                    prime_power = prime_power * i
        return table
        
class Problem():
    def __init__(self):
        self.min_factorial_cached = {}
    
    def solve(self):
        print(self.get(1000000))
    
    def get(self, u):
        results = 0
        table = FactorizationTable().get(u)
        factorial_factorization = {}
        min_factorial = {}
        for i in range(1, u + 1):
            min_factorial_so_far = 1
            for factor in table[i]:
                if factor not in factorial_factorization:
                    factorial_factorization[factor] = 0
                factorial_factorization[factor] += table[i][factor]
                x = self.get_min_factorial(factor, factorial_factorization[factor] * 1234567890)
                min_factorial[factor] = x
            if i < 10:
                continue
            min_factorial_so_far = 1
            for divisor in factorial_factorization:
                min_factorial_so_far = max(min_factorial_so_far, min_factorial[divisor])
            results += min_factorial_so_far
            if i % 1000 == 0:
                print(i, results)
        return results
                    
    def get_min_factorial(self, divisor, power):
        if power == 1:
            return divisor
        hashed = self.hash_pair(divisor, power)
        if hashed in self.min_factorial_cached:
            return self.min_factorial_cached[hashed]
        L = divisor*power // 2
        U = divisor*power
        while L <= U:
            M = (L + U) // 2
            count = self.get_divisor_count(M, divisor)
            if count < power:
                L = M + 1
            elif count >= power:
                U = M - 1
        assert(self.get_divisor_count(L, divisor) >= power)
        assert(self.get_divisor_count(L - 1, divisor) < power)
        self.min_factorial_cached[hashed] = L
        return L

    def get_divisor_count(self, n, divisor):
        results = 0
        divisor_power = divisor
        while divisor_power <= n:
            results += n // divisor_power
            divisor_power *= divisor
        return results

    def hash_pair(self, x, y):
        return '''%d-%d''' % (x, y)

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
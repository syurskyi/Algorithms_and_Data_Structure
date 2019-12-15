import itertools
import math
import sys

class HammingNumber():
    def get(self, n):
        e2 = int(math.log(n, 2))
        e3 = int(math.log(n, 3))
        e5 = int(math.log(n, 5))
        
        result = [1]
        for i in range(1, e2 + 1):
            a = 2**i
            for j in range(e3 + 1):
                b = 3**j
                if a * b > n:
                    break
                for k in range(e5 + 1):
                    c = 5**k
                    x = a * b * c
                    if x > n:
                        break
                    result.append(x)
        return sorted(result)

class NumberTheory():
    def __init__(self, n):
        self.primes = self.__init_primes(n)
        self.is_prime_cache = {}
        self.factorize_cache = {}
        self.all_divisors = {}
        print('Prime count =>', len(self.primes))

    def __init_primes(self, n):
        visited = [False for _ in range(n + 1)]
        visited[0] = visited[1] = True
        for i in range(2, n + 1):
            if visited[i]:
                continue
            for j in range(i*i, n + 1, i):
                visited[j] = True
        return [i for i in range(2, n + 1) if not visited[i]]

    def is_prime(self, n):
        if n in self.is_prime_cache:
            return self.is_prime_cache[n]
        for prime in self.primes:
            if prime * prime > n:
                break
            if n % prime == 0:
                self.is_prime_cache[n] = False
                return self.is_prime_cache[n]
        self.is_prime_cache[n] = True
        return self.is_prime_cache[n]

    def factorize(self, n):
        if n not in self.factorize_cache:
            result = []
            d = n
            for prime in self.primes:
                if prime * prime > d:
                    break
                e = 0
                while d % prime == 0:
                    e += 1
                    d = d // prime
                if e > 0:
                    result.append((prime, e))
            if d > 1:
                result.append((d, 1))
            if not result:
                result = [(1, 0)]
            self.factorize_cache[n] = result
        return self.factorize_cache[n]

    def get_all_divisors(self, n):
        if n not in self.all_divisors:
            rep = self.factorize(n)
            unpacking = [[p**a for a in range(e + 1)] for p, e in rep]
            self.all_divisors[n] = sorted([self.__product(divisor) for divisor in itertools.product(*unpacking)])
        return self.all_divisors[n]

    def __product(self, sequence):
        rv = 1
        for number in sequence:
            rv *= number
        return rv

class InverseEulerTotientFunction():
    def __init__(self, n):
        self.n = n
        self.number_theory = NumberTheory(int(math.sqrt(n)) + 1) 
        self.value_cache = { 1: { 1: [1], 2: [2] } }
        self.max_prime_factor_cache = {}

    def get(self, phi):
        if phi in self.value_cache:
            return self.value_cache[phi]
        if phi % 2 == 1:
            return {}

        divisors = self.number_theory.get_all_divisors(phi)
        max_primes = [d + 1 for d in divisors if self.number_theory.is_prime(d + 1)][::-1]

        result = {}
        for prime in max_primes:
            d = 1
            prime_phi = prime - 1
            result[prime] = []
            while phi % prime_phi == 0:
                prime_power = prime**d
                rest_phi = phi // prime_phi
                rest_solution = self.get_with_max_prime(rest_phi, prime)
                for x in rest_solution:
                    new_x = prime_power * x
                    if new_x <= self.n:
                        result[prime].append(new_x)
                d += 1
                prime_phi *= prime
        self.value_cache[phi] = result
        return self.value_cache[phi]

    def get_with_max_prime(self, phi, max_prime):
        if max_prime == 2:
            if phi == 1:
                return [1]
            else:
                return []

        inverse_phi = self.get(phi)
        result = []
        for prime in inverse_phi:
            if prime < max_prime:
                result += inverse_phi[prime]
        return result

class Problem():
    def __init__(self):
        self.mod = 2**32

    def solve(self):
        #self.benchmark()
        print(self.get(10**12) % self.mod)

    def benchmark(self):
        assert(self.get(100) == 3728)

    def get(self, n):
        function = InverseEulerTotientFunction(n)
        hamming_number = HammingNumber().get(n)
        hamming_number_len = len(hamming_number)
        print('HammingNumber size:', len(hamming_number))
        
        result = 0
        for i in range(hamming_number_len):
            phi_inverse = function.get(hamming_number[i])
            if i % 100 == 0:
                print(i, '=>', hamming_number[i], '=>', len(phi_inverse))
            for prime in phi_inverse:
                result += sum(phi_inverse[prime])
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

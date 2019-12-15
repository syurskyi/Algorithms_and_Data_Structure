import math
import sys

class FactorizationSieve():
    def __init__(self, bound):
        self.value = None
        self.factorization = None
        self.__sieve_n2_plus_one(bound)

    def __sieve_n2_plus_one(self, bound):
        self.value = [n**2 + 1 for n in range(bound + 1)]
        self.factorization = [{} for n in range(bound + 1)]
        for n in range(bound + 1):
            if self.value[n] == 1:
                continue
            p = self.value[n]
            for m in range(n, bound + 1, p):
                e = 0
                while self.value[m] % p == 0:
                    self.value[m] = self.value[m] // p
                    e += 1
                if e > 0:
                    self.factorization[m][p] = e
            for m in range((p - n) % p, bound + 1, p):
                e = 0
                while self.value[m] % p == 0:
                    self.value[m] = self.value[m] // p
                    e += 1
                if e > 0:
                    self.factorization[m][p] = e

    def get(self, n):
        return self.factorization[n]

class Problem():
    def __init__(self):
        self.sieve = None

    def solve(self):
        print(self.get(1024))
        print(self.get_mod(10**7, 1000000007))

    def get_mod(self, bound, mod):
        self.sieve = FactorizationSieve(bound + 1)
        result = 0
        for n in range(1, bound + 1):
            retraction_count = self.__get_retraction_count(n)
            result = (result + retraction_count) % mod
        return result

    def get(self, bound):
        self.sieve = FactorizationSieve(bound + 1)
        result = 0
        for n in range(1, bound + 1):
            retraction_count = self.__get_retraction_count(n)
            result += retraction_count
        return result

    def __get_retraction_count(self, n):
        x = self.sieve.get(n - 1)
        y = self.sieve.get(n + 1)
        z = self.__merge_factorizations(x, y)
        result = 1
        for d in z:
            result *= (d**z[d] + 1)
        return result - (n**4 + 4)

    def __merge_factorizations(self, x, y):
        result = dict(x)
        for d in y:
            if d not in result:
                result[d] = 0
            result[d] += y[d]
        return result

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
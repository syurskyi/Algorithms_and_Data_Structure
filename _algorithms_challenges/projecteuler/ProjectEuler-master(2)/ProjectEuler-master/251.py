import itertools
import sys

class PrimeTable():
    def __init__(self, bound):
        self.factorization = [{} for _ in range(bound + 1)]
        self.special_factorization = [{} for _ in range(bound + 1)]
        self.primes = []
        self._sieve(bound)
    
    def _sieve(self, bound):
        visited = [False] * (bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, bound + 1):
            if visited[i]:
                continue
            self.primes.append(i)
            for j in range(i, bound + 1, i):
                visited[j] = True
                self.factorization[j][i] = 1
            d = i**2
            while d <= bound:
                for j in range(d, bound + 1, d):
                    self.factorization[j][i] += 1
                d *= i
    
            # Sieve on (8k+5)-type number
            if i == 2 or 8 * bound + 5 < i**2:
                continue
            k = (-5 * self._mod_inverse(8, i**2)) % i**2
            if k > bound:
                continue
            for j in range(k, bound + 1, i**2):
                self.special_factorization[j][i] = 1
            d = i**4
            while d <= bound:
                k = (-5 * self._mod_inverse(8, d)) % d
                for j in range(k, bound + 1, d):
                    self.special_factorization[j][i] += 1
                d *= i**2
        #print(self.factorization)
        #print(self.special_factorization)
        print('Sieve completed:', len(self.primes))

    def _mod_inverse(self, a, mod):
        g, x, y = self._extended_gcd(a, mod)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % mod

    def _extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

class Factorization():
    def __init__(self, bound):
        self.prime_table = PrimeTable(bound)
    
    def factorize(self, n):
        return self.prime_table.factorization[n]
    
    def get_all_divisor(self, factorization):
        unpacking = [[p**e for e in range(factorization[p] + 1)] for p in factorization]
        return [self._product(divisor) for divisor in itertools.product(*unpacking)]

    def get_problem251(self, k):
        first_part = self.factorize(k + 1) # (k + 1)^2
        second_part = self._get_square_divisor(k) # (8k + 5)
        return self._merge_two_factorization(first_part, second_part)

    def _get_square_divisor(self, k):
        return self.prime_table.special_factorization[k]

    def _merge_two_factorization(self, x, y):
        for p in y:
            if p not in x:
                x[p] = 0
            x[p] += y[p]
        return x

    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result

class Problem():
    def __init__(self):
        self.factorization = None

    def solve(self):
        #self.get_count(10**6)
        self.get_count(110000000)

    def get_count(self, bound):
        max_k = (bound - 2)//3
        self.factorization = Factorization(max_k + 1)

        count = 0
        for k in range((bound - 2)//3 + 1):
            a = 3*k + 2
            x = (k + 1)**2 * (8 * k + 5) # where x = b^2 c
            if 4 * (bound - a)**3 < 27 * x:
                break
            x_good_factorization = self.factorization.get_problem251(k)
            for b in self.factorization.get_all_divisor(x_good_factorization):
                c = x // b**2
                if a + b + c <= bound:
                    count += 1
                    if count % 1000 == 0:
                        print(count, "=>", a, b, c)
        print(count)
        return count

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

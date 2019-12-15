import bisect
import itertools
import math
import sys

class FibonacciNumberFactorization():
    def __init__(self):
        self.values = self.__init_values_by_file()

    def __init_values_by_file(self):
        import ast
        return ast.literal_eval(open('fib1000.txt').read())

class PrimeTable():
    def get(self, bound):
        primes = []
        visited = [False] * (bound + 1)
        for i in range(2, bound + 1):
            if not visited[i]:
                primes.append(i)
            for j in range(i + i, bound + 1, i):
                visited[j] = True
        print('Sieve range:', bound)
        print('Prime count:', len(primes))
        return primes

class Factorization():
    def __init__(self, primes):
        self.primes = primes

    def get(self, n):
        result = {}
        d = n
        for p in self.primes:
            if p**2 > d:
                break
            if d % p == 0:
                e = 0
                while d % p == 0:
                    e += 1
                    d = d // p
                result[p] = e
        if d > 1:
            result[d] = 1
        return result

    def get_all_divisors(self, n):
        factorization = self.get(n)
        unpacking = [[p**e for e in range(factorization[p] + 1)] for p in factorization]
        return sorted([self.__product(divisor) for divisor in itertools.product(*unpacking)])

    def __product(self, list):
        result = 1
        for number in list:
            result *= number
        return result

class Matrix():
    def multiply(self, x, y, mod):
        results = [[0 for j in range(len(y[0]))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    results[i][j] = (results[i][j] + x[i][k] * y[k][j]) % mod
        return results

    def power(self, x, n, mod):
        if n == 1:
            return x
        half = self.power(x, n >> 1, mod)
        if n & 1 == 1:
            return self.multiply(self.multiply(half, half, mod), x, mod)
        else:
            return self.multiply(half, half, mod)

class Problem():
    def __init__(self):
        self.period_list = self.__get_pisano_period_list()
        #print(self.period_list)
        self.factorization = None

    def solve(self):
        for n in [200, 100000000]:
            print(n, "=>", self.get(n))

    def get(self, n):
        pos = self.__search_fibonacci_number(n)
        print('nth fibonacci number =>', pos)
        mod_part = self.__get_mod_fibonacci_number(pos, 10**16)
        scientific_notation_part = self.__get_scientific_notation_fibonacci_number(pos)
        #print(mod_part, scientific_notation_part)
        return str(mod_part) + ',' + str(scientific_notation_part)

    def __search_fibonacci_number(self, n):
        visited_range = self.__get_visited_range(n)
        print('visited_range =>', visited_range)
        visited = [False] * (visited_range + 1)
        for period in self.period_list:
            for i in range(period, visited_range + 1, period):
                visited[i] = True
        print('square sieve done!')
        pos = 0
        for i in range(1, visited_range + 1):
            if visited[i]:
                continue
            pos += 1
            if pos == n:
                return i

    def __get_scientific_notation_fibonacci_number(self, n):
        phi = (1.0 + math.sqrt(5)) / 2.0
        log_value = n * math.log10(phi) - 0.5 * math.log10(5.0)
        log_integer_part = int(log_value)
        log_fractional_part = log_value - log_integer_part
        
        log_table = [math.log10(i / 10.0) for i in range(10, 100)]
        pos = bisect.bisect_left(log_table, log_fractional_part) - 1

        a = str((pos + 10) // 10) + '.' + str((pos + 10) % 10)
        b = str(log_integer_part)
        return a + 'e' + b

    def __get_pisano_period_list(self):
        big_list = self.__get_big_pisano_period_list()
        small_list = self.__get_small_pisano_period_list()
        return sorted(list(set(big_list + small_list)))
        
    def __get_visited_range(self, n):
        lower_bound, upper_bound = n, 2 * n
        while True:
            mid = (lower_bound + upper_bound) // 2
            count = self.__get_squarefree_count(mid)
            if count > n:
                upper_bound = mid
            elif count < n:
                lower_bound = mid
            else:
                break
        return (lower_bound + upper_bound) // 2

    def __get_squarefree_count(self, visited_range):
        count = visited_range
        for period in self.period_list:
            if period > visited_range:
                break
            count -= visited_range // period
        return count

    def __get_big_pisano_period_list(self):
        result = []
        visited = set()
        visited.add(0)
        visited.add(1)
        factorization_list = FibonacciNumberFactorization().values
        for n in factorization_list:
            factorization = factorization_list[n]
            for prime in factorization:
                if prime not in visited:
                    result.append(prime * n)
                    visited.add(prime)
        return result

    def __get_small_pisano_period_list(self):
        primes = PrimeTable().get(150000)
        self.factorization = Factorization(primes)
        result = []
        for p in primes:
            pisano_period = self.__get_pisano_period(p)
            result.append(p * pisano_period)
        return result

    def __get_pisano_period(self, p):
        if p == 2:
            return 3
        if p == 3:
            return 4
        if p == 5:
            return 5
        candidates = self.__get_possible_pisano_period_candidates(p)
        for d in candidates:
            if self.__get_mod_fibonacci_number(d, p) == 0:
                return d

    def __get_possible_pisano_period_candidates(self, p):
        p_mod_5 = p % 5
        if p_mod_5 == 1 or p_mod_5 == 4:
            return self.factorization.get_all_divisors(p - 1)
        if p_mod_5 == 2 or p_mod_5 == 3:
            return self.factorization.get_all_divisors(p + 1)

    def __get_mod_fibonacci_number(self, n, mod):
        if n == 0:
            return 0
        if n == 1:
            return 1
        transition_matrix = [[0, 1], [1, 1]]
        return Matrix().power(transition_matrix, n - 1, mod)[1][1]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

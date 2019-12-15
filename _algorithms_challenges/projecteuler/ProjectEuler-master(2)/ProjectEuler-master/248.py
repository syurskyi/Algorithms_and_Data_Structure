import itertools
import sys

class PrimeTable():
    def __init__(self, bound):
        self.primes = self.__init_primes(bound)
    
    def __init_primes(self, bound):
        primes = []
        visited = [False] * (bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, bound + 1):
            if not visited[i]:
                primes.append(i)
            for j in range(i + i, bound + 1, i):
                visited[j] = True
        print("Prime count:", len(primes))
        return primes

    def is_prime(self, n):
        for p in self.primes:
            if p**2 > n:
                return True
            if n % p == 0:
                return False
        assert(False)

class Factorization():
    def __init__(self, bound):
        self.prime_table = PrimeTable(13)

    def get(self, n):
        result = {}
        d = n
        for p in self.prime_table.primes:
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

    def get_all_divisors(self, factorization):
        unpacking = [[p**e for e in range(factorization[p] + 1)] for p in factorization]
        return sorted([self.__product(divisor) for divisor in itertools.product(*unpacking)])

    def __product(self, list):
        result = 1
        for number in list:
            result *= number
        return result

class Problem():
    def __init__(self):
        self.factorization = Factorization(13)
        self.prime_table = PrimeTable(80000)

    def solve(self):
        n_factorization = self.__get_factorial(13)
        solution = []
        dfs_stack = [[(p, a, n_factorization)] for p, a in self.__invert_prime(n_factorization, 1)]
        while dfs_stack:
            top = dfs_stack[-1]
            dfs_stack.pop(-1)            
            p, a, f = top[-1]
            next_factorization = self.__remove_phi_factor(f, p, a)
            if not next_factorization:
                x = self.__get_number(top)
                solution.append(x)
                if len(solution) % 1000 == 1:
                    print(len(solution), "=>", x)
            for next_p, next_a in self.__invert_prime(next_factorization, p):
                next_state = top + [(next_p, next_a, next_factorization)]
                dfs_stack.append(next_state)
        sorted_solution = sorted(solution)
        print("stat =>", sorted_solution[0], sorted_solution[-1], len(sorted_solution))
        print("answer =>", sorted_solution[150000 - 1])

    def __invert_prime(self, n_factorization, min_prime):
        pairs = []
        n_divisors = self.factorization.get_all_divisors(n_factorization)
        for divisor in n_divisors:
            p = divisor + 1
            if p <= min_prime:
                continue
            if not self.prime_table.is_prime(p):
                continue
            max_a = n_factorization[p] if p in n_factorization else 0
            for a in range(max_a + 1):
                pairs.append((p, a))
        return pairs

    def __get_factorial(self, n):
        result = {}
        for i in range(2, n + 1):
            i_factorization = self.factorization.get(i)
            print(i, i_factorization)
            for p in i_factorization:
                if p not in result:
                    result[p] = 0
                result[p] += i_factorization[p]
        return result

    def __remove_phi_factor(self, some_factorization, p, a):
        result = dict(some_factorization)
        if p in result:
            assert(result[p] >= a)
            result[p] -= a
        else:
            assert(a == 0)

        y = self.factorization.get(p - 1)
        for q in y:
            assert(q in result)
            assert(result[q] >= y[q])
            result[q] -= y[q]

        normalized_result = {}
        for p in result:
            if result[p] != 0:
                normalized_result[p] = result[p]
        return normalized_result

    def __get_number(self, some_state):
        result = 1
        for p, a, f in some_state:
            result *= p**(a + 1)
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

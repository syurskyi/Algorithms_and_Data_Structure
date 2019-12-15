import itertools
import sys

class Problem():
    def __init__(self):
        self.primes = []
        self._init_primes()

    def solve(self):
        print(self.get_way_count(11))
        print(self.get_way_count(1000001))
        print(self.get_way_count(12017639147))

    def get_way_count(self, surface_count):
        assert(surface_count % 2 == 1)
        n = (surface_count + 3) // 2
        assert(n % 3 == 1)
        factors = self._get_prime_factors(n)

        count = (n - 2) // 3 + 1
        for multiply in self._get_factor_multiplies(factors):
            if multiply[1]:
                count -= self._get_multiply_count(n, multiply[0])
            else:
                count += self._get_multiply_count(n, multiply[0])
        return count

    def _get_factor_multiplies(self, factors):
        rv = []
        n = len(factors)
        for i in range(1, n + 1):
            for factor_subset in itertools.combinations(factors, i):
                x = 1
                for j in factor_subset:
                    x *= j
                rv.append([x, len(factor_subset) % 2 == 1])
        return rv

    def _get_multiply_count(self, n, multiply):
        first_k = None
        if multiply % 3 == 1:
            first_k = (multiply * 2 - 2) // 3
        elif multiply % 3 == 2:
            first_k = (multiply - 2) // 3
        last_k = (n - 2) // 3
        last_k = first_k + ((last_k - first_k) // multiply) * multiply
        return (last_k - first_k) // multiply + 1

    def _init_primes(self):
        SIEVE_RANGE = 80000
        sieve_visited = [False] * SIEVE_RANGE
        sieve_visited[0] = sieve_visited[1] = True
        for i in range(2, SIEVE_RANGE):
            if sieve_visited[i] is False:
                self.primes.append(i)
                for j in range(i + i, SIEVE_RANGE, i):
                    sieve_visited[j] = True

    def _get_prime_factors(self, n):
        factors = []
        d = n
        for i in range(len(self.primes)):
            if d == 1:
                break
            p = self.primes[i]
            if d < p**2:
                break
            if d % p == 0:
                while d % p == 0:
                    d = d // p
                factors.append(p)
        if d > 1:
            factors.append(d)
        return factors

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
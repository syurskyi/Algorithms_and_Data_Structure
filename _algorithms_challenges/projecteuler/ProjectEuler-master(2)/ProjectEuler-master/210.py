import sys

class PrimeTable():
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()
    
    def _sieve(self):
        visited = [False] * (self.bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, self.bound + 1):
            if not visited[i]:
                self.primes.append(i)
            for j in range(i + i, self.bound + 1, i):
                visited[j] = True

class Factorization():
    def __init__(self):
        self.prime_table = PrimeTable(100)
    
    def get(self, n):
        d = n
        rv = []
        for i in range(len(self.prime_table.primes)):
            p = self.prime_table.primes[i]
            if d == 1 or p > d:
                break
            count = 0
            while d % p == 0:
                d = d // p
                count += 1
            if count > 0:
                rv += [(p, count)]
        if d > 1:
            raise Exception('prime factor should be small')
        return rv

class ProjectEulerProblem233():
    def __init__(self):
        self.factorization = Factorization()
    
    def get(self, n):
        rv = 4
        factors = self.factorization.get(n)
        for p, e in factors:
            if p % 4 == 1:
                rv *= (2 * e + 1)
        return rv

class GaussCircleProblem():
    def get(self, n):
        N = 2 * (n // 8)**2
        floor_r = self._int_sqrt(N)
        sum = 0
        for x in range(floor_r + 1):
            sum += self._int_sqrt(N - x**2)
        return 4 * sum + 1

        n = N
        sum = 0
        for i in range(n // 4 + 1):
            sum += n // (4*i + 1) - n // (4*i + 3)
        return 1 + 4 * sum

    """
    http://www.codecodex.com/wiki/Calculate_an_integer_square_root
    """
    def _int_sqrt(self, n):
        guess = (n >> n.bit_length() // 2) + 1
        result = (guess + n // guess) // 2
        while abs(result - guess) > 1:
            guess = result
            result = (guess + n // guess) // 2
        while result * result > n:
            result -= 1
        return result

class Problem():
    def __init__(self):
        self.gauss_circle_problem = GaussCircleProblem()
        self.project_euler_problem = ProjectEulerProblem233()
    
    def solve(self):
        self.validate_by_projecteuler_forum()
        print(self.get(10**9))
        
    def validate_by_projecteuler_forum(self):
        assert(self.benchmark(8) == 100)
        assert(self.get(8) == 100)
        assert(self.get(1000) == 1597880)
        assert(self.get(2000) == 6392158)
        assert(self.get(10000) == 159814790)
        assert(self.get(20000) == 639264906)
        assert(self.get(100000) == 15981722482)
        assert(self.get(1000000) == 1598174519142)
    
    def get(self, n):
        square = 2 * n**2 + 2 * n + 1
        stripped = (n + 1) * (n // 4 + 1) + n * (n // 4)
        gauss_circle = self.gauss_circle_problem.get(n)
        on_circle = self.project_euler_problem.get(n // 4)
        line = n + 1
        result = square - stripped + gauss_circle - on_circle - line + 2
        print(n, square, stripped, gauss_circle, on_circle, line, result)
        return result
    
    def benchmark(self, n):
        import itertools
        square, stripped, gauss_circle, on_circle, line = 0, 0, 0, 0, 0
        for x, y in itertools.product(range(-n, n+1), repeat=2):
            if abs(x) + abs(y) > n:
                continue
            # On square
            square += 1
            # On the line
            if x == y:
                line += 1
            # On the stripped area
            if x + y >= 0 and x + y <= n // 2:
                stripped += 1
            # On the circle
            if (x - n // 8)**2 + (y - n // 8)**2 == 2 * (n // 8)**2:
                on_circle += 1
            # Inside the circle
            if (x - n // 8)**2 + (y - n // 8)**2 <= 2 * (n // 8)**2:
                gauss_circle += 1
        result = square - stripped + gauss_circle - on_circle - line + 2
        print(n, square, stripped, gauss_circle, on_circle, line, result)
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

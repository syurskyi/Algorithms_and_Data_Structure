import fractions
import itertools
import sys

class Factorization():
    def __init__(self):
        self.factorization = None
        self.visited = None
    
    def build(self, bound):
        self.factorization = [{} for _ in range(bound + 1)]
        self.visited = [False for _ in range(bound + 1)]
        self.visited[0] = self.visited[1] = True
        for i in range(2, bound + 1):
            if self.visited[i]:
                continue
            self.factorization[i][i] = 1
            for j in range(i + i, bound + 1, i):
                self.visited[j] = True
                self.factorization[j][i] = 1
            d = i**2
            while d <= bound:
                for j in range(d, bound + 1, d):
                    self.factorization[j][i] += 1
                d *= i
        print(self.factorization)
    
    def is_prime(self, n):
        return not self.visited[n]
    
    def get_rep(self, n_list):
        rv = {}
        for n in n_list:
            f = self.factorization[n]
            for p in f:
                if p not in rv:
                    rv[p] = 0
                rv[p] += f[p]
        return rv

    def get_all_divisors(self, n_list):
        f = self.get_rep(n_list)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])

    def _product(self, sequence):
        rv = 1
        for number in sequence:
            rv *= number
        return rv

class Problem():
    def solve(self):
        assert(self.get(200) == 5)
        print(self.get(1000000))
    
    def get(self, bound):
        rv = 0
        visited_solutions = set()
        
        factorization = Factorization()
        factorization.build(bound)
        for e in range(1, bound + 1):
            if factorization.is_prime(e):
                continue
            if e % 2 == 0 and factorization.is_prime(e // 2):
                continue
            
            smooth_divisors = self.get_smooth_divisors(factorization.get_all_divisors([e, e]), e-1)
            for B, D in itertools.combinations(smooth_divisors, 2):
                A = e**2 // B
                C = e**2 // D
                if (A + B) % 2 != 0 or (C + D) % 2 != 0:
                    continue
                a = (A + B) // 2
                b = (C + D) // 2
                c = (A - B) // 2
                d = (C - D) // 2
                v = fractions.gcd(c + d, c * d)
                u = (c + d) // v
                X = c * u
                Y = e * u
                Z = d * u
                alpha = a * u
                beta = b * u
                h = c * d // v
                if alpha < bound and beta < bound:
                    hashed = self.hash_solution([beta, alpha, h])
                    if hashed in visited_solutions:
                        continue
                    visited_solutions.add(hashed)
                    rv += 1
                    if rv % 1000 == 0:
                        print(rv, '=>', beta, alpha, h)
        return rv

    def hash_solution(self, solution):
        x, y, h = solution
        return '''%d|%d|%d''' % (x, y, h)

    def get_smooth_divisors(self, all_divisors, e):
        rv = []
        for d in all_divisors:
            if d > e:
                break
            rv.append(d)
        return(rv)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

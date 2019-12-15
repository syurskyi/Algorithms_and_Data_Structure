import itertools
import math
import sys

class PrimeTable():
    def get(self, n):
        sqrt_n = int(math.sqrt(n))
        visited = [False] * (n + 1)
        visited[0] = visited[1] = True
        for i in range(2, sqrt_n + 1):
            if not visited[i]:
                for j in range(i * i, n + 1, i):
                    visited[j] = True
        result = [i for i in range(2, n + 1) if not visited[i]]
        return result

class FactorizationAlgorithm():
    def __init__(self, n):
        self.prime_table = self.__init_prime_table(n)

    def __init_prime_table(self, n):
        sqrt_n = int(math.sqrt(n))
        return PrimeTable().get(sqrt_n)

    def get(self, n):
        result = []
        d = n
        for prime in self.prime_table:
            if prime * prime > n:
                break
            if d % prime == 0:
                e = 0
                while d % prime == 0:
                    d //= prime
                    e += 1
                result.append((prime, e))
        if d > 1:
            result.append((d, 1))
        return result

class CipollaAlgorithm():
    def execute(self, n, p):
        if p == 2:
            return None
        if self.__legendre_symbol(n, p) != 1:
            return None
        a = self.__find_a(n, p)
        x = self.__compute_x(a, n, p)
        if 2 * x > p:
            return p - x
        else: 
            return x
            
    def __legendre_symbol(self, a, p):
        return pow(a % p, (p - 1) // 2, p)    

    def __find_a(self, n, p):
        for a in range(p):
            if self.__legendre_symbol(a**2 - n, p) != 1:
                return a
        
    def __compute_x(self, a, n, p):
        d = a**2 - n
        q = (p+1) // 2        
        b = [a, 1]
        x = [1, 0]
        while q > 0:
            if q & 1 != 0:
                x = [(x[0]*b[0] + d*x[1]*b[1]) % p, (x[0]*b[1] + x[1]*b[0]) % p] 
            b = [(b[0]**2 + d * b[1]**2) % p, (2*b[0]*b[1]) % p]
            q >>= 1
        return x[0]  

class SumOfTwoSquaresAlgorithm():
    def __init__(self, n):
        self.cipolla_algorithm = CipollaAlgorithm()
        self.n = n
        self.prime_table = self.__init_prime_table(n)
        self.prime_solution = self.__init_prime_solution()

    def get(self, factorization):
        for p, e in factorization:
            if p % 4 == 3:
                return []
        solution = self.prime_solution[2][0]
        for p, e in factorization:
            if p * p > self.n:
                self.__set_large_prime_solution(p)
            solution = self.__combine(solution, self.prime_solution[p][e - 1])
        return solution
        
    def __init_prime_table(self, n):
        sqrt_n = int(math.sqrt(n))
        return PrimeTable().get(sqrt_n)

    def __init_prime_solution(self):
        result = { 2: [self.__generate_solution(0, 1), self.__generate_solution(1, 1)] }
        for p in self.prime_table:
            if p % 4 != 1:
                continue
            solution_vector = []
            a, b = self.__execute_prime(p)
            base = self.__generate_solution(a, b)
            d = p
            solution = result[2][0]
            while d <= self.n:
                solution = self.__combine(solution, base)
                solution_vector.append(solution)
                d *= p
            result[p] = solution_vector
        return result

    def __set_large_prime_solution(self, p):
        if p not in self.prime_solution:
            if p % 4 == 1:
                a, b = self.__execute_prime(p)
                self.prime_solution[p] = [self.__generate_solution(a, b)]
            else:
                self.prime_solution[p] = [set()]

    def __generate_solution(self, a, b):
        result = set()
        for a_sign in [1, -1]:
            for b_sign in [1, -1]:
                result.add((a * a_sign, b * b_sign))
                result.add((b * b_sign, a * a_sign))
        return result

    def __execute_prime(self, p):
        z = self.cipolla_algorithm.execute(-1, p)
        return self.__extended_euclidean_algorithm(p, z, p)

    def __extended_euclidean_algorithm(self, a, b, p):
        sqrt_p = int(math.sqrt(p)) + 1
        x, y = 0, 1
        last_x, last_y = 1, 0
        while b != 0:
            if a < sqrt_p:
                return b, a
            q, r = a // b, a % b
            a, b = b, r
            x, last_x = last_x - q * x, x
            y, last_y = last_y - q * y, y

    def __combine(self, one, other):
        result = set()
        for a, b in one:
            for c, d in other:
                result.add((a * d + b * c, a * c - b * d))
        return result

class Problem():
    def solve(self):
        print(self.get(10**5))

    def get(self, perimeter_bound):
        n = perimeter_bound**2 // 16

        factorization_algorithm = FactorizationAlgorithm(n)
        sum_of_two_squares_algorithm = SumOfTwoSquaresAlgorithm(n)

        print('radius count =>', n // 10)
        result = 0.0
        for i in range(5, n + 1, 10):
            if i % 100005 == 0:
                print('progress =>', i, '/', n)

            if i % 3 == 0 or i % 7 == 0:
                continue

            factorization = factorization_algorithm.get(i)
            solution = sum_of_two_squares_algorithm.get(factorization)
            for p1, p2, p3 in itertools.combinations(solution, 3):
                x1, y1 = p1
                x2, y2 = p2
                x3, y3 = p3
                if x1 + x2 + x3 == 5 and y1 + y2 + y3 == 0:
                    perimeter = self.__distance(p1, p2) + self.__distance(p2, p3) + self.__distance(p3, p1)
                    if perimeter <= perimeter_bound:
                        result += perimeter
                        print(i, '=>', p1, p2, p3, perimeter, 'result =>', result)
                    else:
                        break
        return result

    def __distance(self, p, q):
        x1, y1 = p
        x2, y2 = q
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

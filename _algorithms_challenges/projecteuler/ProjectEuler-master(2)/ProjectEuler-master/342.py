import sys

class Factorization():
    def __init__(self, bound):
        self.factorization = self.__init_factorization(bound)

    def __init_factorization(self, bound):
        result = [{} for _ in range(bound + 1)]
        visited = [False for _ in range(bound + 1)]
        for i in range(2, bound + 1):
            if visited[i]:
                continue
            for j in range(i, bound + 1, i):
                visited[j] = True
                result[j][i] = 1
            d = i**2
            while d <= bound:
                for j in range(d, bound + 1, d):
                    result[j][i] += 1
                d *= i
        return result

    def get(self, n):
        return self.factorization[n]

class Problem():
    def __init__(self):
        self.factorization = None

    def solve(self):
        print(self.get(10**10))

    def get(self, bound):
        factorization_bound = int(pow(bound**2, 1/3))
        assert(factorization_bound**3 < bound**2)
        assert((factorization_bound + 1)**3 >= bound**2)
        self.factorization = Factorization(factorization_bound)
        result = 0
        for i in range(2, factorization_bound + 1, 2):
            x = self.invert_phi_function(i)
            if x < bound:
                result += x
        return result

    def invert_phi_function(self, cube):
        x = 1
        d_factorization = self.__get_cube(cube)
        while d_factorization:
            q = self.__get_biggest_prime(d_factorization)
            b = d_factorization[q]
            if b % 2 == 0:
                return 0
            d_factorization = self.__remove_phi_factor(d_factorization, q)
            if d_factorization is None:
                return 0
            a = (b + 1) // 2
            x *= q**a
        return x

    def __get_cube(self, n):
        n_factorization = self.factorization.get(n)
        result = {}
        for p in n_factorization:
            result[p] = 3 * n_factorization[p]
        return result

    def __get_biggest_prime(self, some_factorization):
        biggest_prime_so_far = 1
        for p in some_factorization:
            if p > biggest_prime_so_far:
                biggest_prime_so_far = p
        return biggest_prime_so_far

    def __remove_phi_factor(self, some_factorization, q):
        result = dict(some_factorization)
        result.pop(q, None)
        y = self.factorization.get(q - 1)
        for p in y:
            if p not in result:
                return None
            if result[p] < y[p]:
                return None 
            elif result[p] > y[p]:
                result[p] -= y[p]
            else:
                result.pop(p, None)
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

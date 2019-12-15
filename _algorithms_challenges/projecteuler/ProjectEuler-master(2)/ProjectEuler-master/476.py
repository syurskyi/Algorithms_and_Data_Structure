import fractions
import logging
import math
import sys

class MalfattiProblem():
    def __init__(self):
        self.LOGGER = logging.getLogger()

    def solve(self, triangle):
        sorted_triangle = sorted(triangle)
        self.__debug('''Triangle: {sorted_triangle}'''.format(sorted_triangle=sorted_triangle))

        first_radius = self.__place_first_circle(sorted_triangle)
        self.__debug('''    #1 circle radius: {first_radius}'''.format(first_radius=first_radius))

        second_radius, next_triangle = self.__place_second_circle(sorted_triangle, first_radius)
        self.__debug('''    #2 circle radius: {second_radius} {next_triangle}'''.format(second_radius=second_radius, next_triangle=next_triangle))

        third_radius = self.__place_third_circle(sorted_triangle, next_triangle, second_radius, first_radius)
        self.__debug('''    #3 circle radius: {third_radius}'''.format(third_radius=third_radius))

        area = math.pi * (first_radius**2 + second_radius**2 + third_radius**2)
        return area

    def __place_first_circle(self, triangle):
        return self.__get_incircle_radius(triangle)

    def __place_second_circle(self, sorted_triangle, r):
        a, b, c = sorted_triangle
        return self.__place_circle_in_angle(sorted_triangle, a, r)

    def __place_third_circle(self, sorted_triangle, next_triangle, next_radius, r):
        a, b, c = sorted_triangle

        a_nested_radius = self.__place_circle_in_angle(next_triangle, min(next_triangle), next_radius)[0]
        self.__debug('''        #3 a_nested_radius possible: {a_nested_radius}'''.format(a_nested_radius=a_nested_radius))

        b_radius = self.__place_circle_in_angle(sorted_triangle, b, r)[0]
        self.__debug('''        #3 b_radius possible: {b_radius}'''.format(b_radius=b_radius))

        descartes_radius = self.__get_descartes_radius(next_radius, r)
        self.__debug('''        #3 descartes_radius possible: {descartes_radius}'''.format(descartes_radius=descartes_radius))

        return max(a_nested_radius, b_radius, descartes_radius)

    def __place_circle_in_angle(self, triangle, side, r):
        s = sum(triangle) / 2 
        x = math.sqrt((s - side)**2 + r**2) 
        h = x - r
        next_triangle = sorted([2 * h * r / (s - side), h * x / (s - side), h * x / (s - side)])
        return self.__get_incircle_radius(next_triangle), next_triangle

    def __get_incircle_radius(self, triangle):
        a, b, c = triangle
        return math.sqrt((a + b - c) * (b + c - a) * (c + a - b) / (a + b + c)) / 2

    def __get_descartes_radius(self, r1, r2):
        k1 = 1 / r1 
        k2 = 1 / r2
        k = k1 + k2 + 2 * math.sqrt(k1 * k2)
        return 1 / k

    def __debug(self, message):
        self.LOGGER.debug(message)

class Factorization():
    def __init__(self, sieve_range):
        self.results = [[] for _ in range(sieve_range + 1)]
        for i in range(2, sieve_range + 1):
            if len(self.results[i]) == 0:
                for j in range(i, sieve_range + 1, i):
                    self.results[j].append(i)
    
    def get_prime_factors(self, n):
        return self.results[n]

class Problem():
    def __init__(self):
        self.LOGGER = logging.getLogger()
        self.malfatti_problem = MalfattiProblem()
        self.factorization = Factorization(2000)

    def solve(self):
        self.benchmark()
        print(self.S(1803)) # 110242.87794435625

    def benchmark(self):
        self.__assert(self.R(1, 1, 1), 0.31998)
        self.__assert(self.S(2), 0.31998)
        self.__assert(self.S(5), 1.25899)

    def R(self, a, b, c):
        return self.malfatti_problem.solve([a, b, c])

    def S(self, n):
        R_sum = 0.0
        count = 0
        iter_count = 0
        for a in range(1, n + 1):
            for b in range(a, n + 1 - a):
                sub_g = fractions.gcd(a, b)
                sub_sum = a + b
                c_list = self.__get_c_list(a, b)
                for c in c_list:
                    factor = n // sub_sum
                    area_factor = factor * (factor + 1) * (2 * factor + 1) // 6
                    area = self.R(a, b, c) * area_factor
                    R_sum += area
                    count += factor
                    iter_count += 1
                    if iter_count % 10000 == 0:
                        self.LOGGER.info('''Found: {a}, {b}, {c}, {area}, {count}, {sum}'''.format(a=a, b=b, c=c, area=area, count=count, sum=R_sum))
        self.LOGGER.info('''Sum: {sum}'''.format(sum=R_sum))
        self.LOGGER.info('''Count: {count}'''.format(count=count))
        return R_sum / count

    def __get_c_list(self, a, b):
        g_factors = self.factorization.get_prime_factors(fractions.gcd(a, b))
        c_sieve = [True for _ in range(b, a + b)]
        for prime in g_factors:
            b0 = b
            q, r = divmod(b, prime)
            if r != 0:
                b0 += prime - r
            for i in range(b0, a + b, prime):
                c_sieve[i - b] = False
        return [i for i in range(b, a + b) if c_sieve[i - b]]

    def __assert(self, actual, expected, epsilon=1e-5):
        assert(abs(actual - expected) < epsilon)

def config_log(level=logging.INFO, 
                threshold=logging.WARNING,
                format="%(asctime)s %(filename)s [%(levelname)s] %(message)s",
                datefmt="%H:%M:%S"):
    root = logging.getLogger()
    root.setLevel(level)
    formatter = logging.Formatter(format, datefmt)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(level)
    stdout_handler.setFormatter(logging.Formatter(format, datefmt))
    root.addHandler(stdout_handler)

def main():
    config_log(level=logging.INFO)
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())


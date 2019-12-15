import math
import sys

class SegmentPrime():
    def get(self, begin, end):
        n = int(math.sqrt(end)) + 1 
        basic_prime_list = self.__get_basic_prime_list(n)
        visited = [False for _ in range(begin, end + 1)]
        for prime in basic_prime_list:
            i0 = 0
            r = begin % prime
            if r != 0:
                i0 = prime - r
            for i in range(i0, end - begin + 1, prime):
                visited[i] = True
        return [i + begin for i in range(end - begin + 1) if not visited[i]]

    def __get_basic_prime_list(self, n):
        sqrt_n = int(math.sqrt(n)) + 1 
        visited = [False for _ in range(n + 1)]
        visited[0] = visited[1] = True
        for i in range(2, sqrt_n + 1):
            if not visited[i]:
                for j in range(i * i, n + 1, i):
                    visited[j] = True        
        return [i for i in range(2, n + 1) if not visited[i]]

class ExtendedGCD():
    def solve(a, b):
        x, y = 0, 1
        last_x, last_y = 1, 0
        while b != 0:
            q, r = divmod(a, b)
            a, b = b, r
            x, last_x = last_x - q * x, x
            y, last_y = last_y - q * y, y
        return last_x, last_y

# Solve ax = 1 (mod m).
class ModInverse():
    def solve(a, m):
        x, y = ExtendedGCD.solve(a, m)
        return x % m

class Problem():
    def __init__(self):
        self.mod = 1000000007
        self.factorial = self.__set_factorial(10010000)
        self.inverse_factorial = self.__set_inverse_factorial(10010000)

    def solve(self):
        assert(self.get(90) == 7564511)
        prime_list = SegmentPrime().get(10000000, 10010000)
        result = 0
        for prime in prime_list:
            count = self.get(prime)
            result = (result + count) % self.mod
            print(prime, '=>', count)
        print(result)

    def get(self, n):
        result = 1
        y_max = int(math.sqrt(n))
        for y in range(1, y_max + 1):
            x = int(n - y * math.sqrt(n))
            count = self.__get_binomial(x + y, x)
            result = (result + count) % self.mod
        return result 

    def __get_binomial(self, n, m):
        return (self.factorial[n] * self.inverse_factorial[m] * self.inverse_factorial[n - m]) % self.mod

    def __set_factorial(self, n):
        d = 1
        result = [d]
        for i in range(1, n + 1):
            d = (d * i) % self.mod
            result.append(d)
        return result

    def __set_inverse_factorial(self, n):
        d = 1
        result = [d]
        for i in range(1, n + 1):
            d = (d * ModInverse.solve(i, self.mod)) % self.mod
            result.append(d)
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

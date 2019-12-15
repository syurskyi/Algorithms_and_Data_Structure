from fractions import gcd
import itertools
import math
import sys

class NumberTheory():
    def __init__(self, n):
        self.bound = n
        self.bound2 = n * n
        self.primes = self.__init_primes(n)
        self.prime_count = len(self.primes)

    def __init_primes(self, n):
        visited = [False for _ in range(n + 1)]
        visited[0] = visited[1] = True
        for i in range(2, n + 1):
            if visited[i]:
                continue
            for j in range(i*i, n + 1, i):
                visited[j] = True
        return [i for i in range(2, n + 1) if not visited[i]]

    def is_prime(self, n):
        for p in self.primes:
            if p**2 > n:
                return True
            if n % p == 0:
                return False
        assert(False)

    def factor(self, n):
        result = {}
        d = n
        for prime in self.primes:
            if prime * prime > d:
                break
            e = 0
            while d % prime == 0:
                e += 1
                d = d // prime
            if e > 0:
                result[prime] = e
        if d > 1:
            assert(d <= self.bound2)
            result[d] = 1
        return result

    def get_all_divisors(self, n):
        rep = self.factor(n)
        unpacking = [[p**a for a in range(rep[p] + 1)] for p in rep]
        return sorted([self.__product(divisor) for divisor in itertools.product(*unpacking)])

    def __product(self, sequence):
        rv = 1
        for number in sequence:
            rv *= number
        return rv

class Problem():
    def __init__(self):
        self.number_theory = None

    def solve(self):
        #self.get(10**9)
        self.get(2 * 10**11)

    def get(self, n):
        sqrt_n = int(math.sqrt(n)) + 1
        self.number_theory = NumberTheory(sqrt_n)
        print('Prime count =>', self.number_theory.prime_count)
        
        max_tuple_size = self.__get_max_tuple_size(n)
        print('max_tuple_size =>', max_tuple_size)

        result = set()
        for prime_count in range(1, max_tuple_size):
            print('prime_count =>', prime_count)
            for d, phi, last_pos in self.__generate_prime_tuple(prime_count, n):
                prime_bound = self.number_theory.primes[last_pos]
                if d > sqrt_n:
                    result |= self.__get_coresilience_set(n, d, phi, last_pos)
                else:
                    g = gcd(d, phi)
                    if g != 1:
                        continue
                    all_divisors = self.number_theory.get_all_divisors(d * phi + d - phi)
                    for divisor in all_divisors:
                        x = divisor - phi
                        y = d - phi
                        #print(x, y)
                        if x * d > n * y:
                            break
                        if x % y == 0:
                            q = x // y
                            if q > prime_bound and self.number_theory.is_prime(q):
                                coresilience = d * q
                                result.add(coresilience)
                                if prime_count > 1:
                                    print('found =>', coresilience)

        print(sum(result), len(result))
       
    def __get_coresilience_set(self, n, d, phi, last_pos):
        result = set()
        for i in range(last_pos + 1, self.number_theory.prime_count):
            q = self.number_theory.primes[i]
            next_d = d * q
            if next_d > n:
                break
            next_phi = phi * (q - 1)
            if (next_d - 1) % (next_d - next_phi) == 0:
                result.add(next_d)
        if result:
            print(d, phi, '=>', result)
        return result

    def __get_max_tuple_size(self, bound):
        d = 1
        size = 0
        prime_count = self.number_theory.prime_count
        for i in range(1, prime_count):
            d *= self.number_theory.primes[i]
            if d > bound:
                return size
            size += 1

    def __generate_prime_tuple(self, tuple_size, bound):
        prime_count = self.number_theory.prime_count
        for i in range(1, prime_count):
            prime = self.number_theory.primes[i]
            if prime**tuple_size > bound:
                break
            initial_state = (prime, prime - 1, 1, i)
            stack = [initial_state]
            while stack:
                d, phi, pos_size, last_pos = stack.pop(-1)
                if pos_size < tuple_size:
                    for j in range(last_pos + 1, prime_count):
                        next_prime = self.number_theory.primes[j]
                        next_d = d * next_prime
                        if next_d * (next_prime + 2) > bound:
                            break
                        next_phi = phi * (next_prime - 1)
                        next_pos_size = pos_size + 1
                        next_last_pos = j
                        next_state = (next_d, next_phi, next_pos_size, next_last_pos)
                        stack.append(next_state)
                else:
                    yield d, phi, last_pos

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
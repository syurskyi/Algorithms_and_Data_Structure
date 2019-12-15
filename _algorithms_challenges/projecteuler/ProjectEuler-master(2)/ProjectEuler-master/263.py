import sys

class PrimeTable():
    def get(self, sieve_range):
        primes = []
        visited = [False] * sieve_range
        visited[0] = visited[1] = True
        for i in range(2, sieve_range):
            if not visited[i]:
                primes.append(i)
                for j in range(2*i, sieve_range, i):
                    visited[j] = True
        return primes

class Factorization():
    def __init__(self, primes):
        self.primes = primes
    
    def get(self, n):
        d = n
        rv = []
        for i in range(len(self.primes)):
            p = self.primes[i]
            if d == 1 or p * p > d:
                break
            if d % p != 0:
                continue
            alpha = 0
            while d % p == 0:
                alpha += 1
                d = d // p
            rv.append((p, alpha))
        if d > 1:
            rv.append((d, 1))
        return rv        
        
class Problem():
    def __init__(self):
        self.primes = PrimeTable().get(10000000)
        self.factorization = Factorization(self.primes)
        
    def solve(self):
        paradise_count = 0
        paradise_sum = 0
        for i in range(11, 10000000000, 10):
            if (i - 11) % 1000000 == 0:
                print(i)
            if not (self.is_prime(i) and self.is_prime(i + 6) and self.is_prime(i + 12) and self.is_prime(i + 18)):
                continue
            n = i + 9
            if not self.check_practical(n):
                continue
            print('[66% engineers\' paradise]:', n)
            if not self.check_consecutive(i):
                continue
            print('{100% engineers\' paradise}:', n)
            paradise_count += 1
            paradise_sum += n
            if paradise_count == 4:
                break
        print(paradise_sum)

    def check_practical(self, n):
        return self.is_practical(n - 8) \
                and self.is_practical(n - 4) \
                and self.is_practical(n) \
                and self.is_practical(n + 4) \
                and self.is_practical(n + 8)

    def check_consecutive(self, i):
        return not (self.is_prime(i + 2) or self.is_prime(i + 8) or self.is_prime(i + 10) or self.is_prime(i + 16))

    def is_prime(self, n):
        for i in range(len(self.primes)):
            p = self.primes[i]
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

    def is_practical(self, n):
        assert(n % 2 == 0)
        factors = self.factorization.get(n)
        k = len(factors)
        for i in range(1, k):
            p_i = factors[i][0]
            right_hand_side = 1
            for j in range(i):
                p_j, alpha_j = factors[j][0], factors[j][1]
                right_hand_side *= (p_j**(alpha_j + 1) - 1) // (p_j - 1)
            right_hand_side += 1
            if p_i > right_hand_side:
                return False
        return True
    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

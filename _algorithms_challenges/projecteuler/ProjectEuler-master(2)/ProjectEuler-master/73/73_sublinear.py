import sys

class Problem():
    def __init__(self):
        self.d = None
        self.K = None
        self.M = None
        self.R_small = None
        self.R_large = None
    
    def solve(self):
        print(self.get(8))
        print(self.get(12000))

    def get(self, d):
        self.d = d
        self.K = self._int_sqrt(d // 2)
        self.M = self.d // (2 * self.K + 1)
        self.R_small = [0 for _ in range(self.M + 1)]
        self.R_large = [0 for _ in range(self.K)]
        for n in range(5, self.M + 1):
            self.R(n)
        for j in range(self.K - 1, -1, -1):
            self.R(self.d // (2 * j + 1))
        return self.R_large[0]

    def F(self, n):
        q, r = divmod(n, 6)
        rv = q * (3 * q - 2 + r)
        if r == 5:
            rv += 1
        return rv

    def R(self, n):
        max_k = self._int_sqrt(n // 2)
        count = self.F(n) - self.F(n // 2)
        m = 5
        k = (n - 5) // 10
        while k >= max_k:
            next_k = (n // (m + 1) - 1) // 2
            count -= (k - next_k) * self.R_small[m]
            k = next_k
            m += 1
        while k > 0:
            m = n // (2*k + 1)
            if m <= self.M:
                count -= self.R_small[m]
            else:
                count -= self.R_large[(self.d // m - 1) // 2]
            k -= 1
        if n <= self.M:
            self.R_small[n] = count
        else:
            self.R_large[(self.d // n - 1) // 2] = count

    def _int_sqrt(self, n):
        guess = (n >> n.bit_length() // 2) + 1
        result = (guess + n // guess) // 2
        while abs(result - guess) > 1:
            guess = result
            result = (guess + n // guess) // 2
        while result * result > n:
            result -= 1
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

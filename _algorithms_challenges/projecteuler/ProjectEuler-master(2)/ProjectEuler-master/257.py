import fractions
import math
import sys

class Problem():
    def solve(self):
        self.sanity_check()
        for n in [100000000]:
            print(n, "=>", self.T(n))

    def sanity_check(self):
        assert(self.T(10) == 3)
        assert(self.T(100) == 46)
        assert(self.T(1000) == 610)
        assert(self.T(10000) == 7677)
        assert(self.T(100000) == 92318)

    def T(self, n):
        case_4bc_count = self.get_case_4bc_count(n)
        case_3bc_count = self.get_case_3bc_count(n)
        case_2bc_count = self.get_case_2bc_count(n)
        total_count = case_4bc_count + case_3bc_count + case_2bc_count
        return total_count

    def get_case_4bc_count(self, n):
        return n // 3

    def get_case_3bc_count(self, n):
        different_parity_count = self.get_case_3bc_different_parity_count(n)
        same_parity_count = self.get_case_3bc_same_parity_count(n)
        return different_parity_count + same_parity_count

    def get_case_3bc_different_parity_count(self, n):
        p_bound = int(math.sqrt(n + 1) - 2)
        count = 0
        for p in range(1, p_bound + 1):
            if p % 3 == 0:
                continue
            q0 = p // 3 + 1
            if p % 2 == q0 % 2:
                q0 += 1
            for q in range(q0, p, 2):
                perimeter = (p + q)*(p + 3*q)
                if perimeter > n:
                    break
                if fractions.gcd(p, q) > 1:
                    continue
                count += n // perimeter
        return count

    def get_case_3bc_same_parity_count(self, n):
        m = 2*n
        p_bound = int(math.sqrt(m + 1) - 2)
        count = 0
        for p in range(1, p_bound + 1, 2):
            if p % 3 == 0:
                continue
            q0 = p // 3 + 1
            if p % 2 != q0 % 2:
                q0 += 1
            for q in range(q0, p, 2):
                perimeter = (p + q)*(p + 3*q)
                if perimeter > m:
                    break
                if fractions.gcd(p, q) > 1:
                    continue
                count += m // perimeter
        return count

    def get_case_2bc_count(self, n):
        p_bound = int((math.sqrt(4 * n + 1) - 3) / 2)
        count = 0
        for p in range(1, p_bound + 1, 2):
            for q in range(p // 2 + 1, p):
                perimeter = (p + q)*(p + 2*q) 
                if perimeter > n:
                    break
                if fractions.gcd(p, q) > 1:
                    continue
                count += n // perimeter
        return count

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

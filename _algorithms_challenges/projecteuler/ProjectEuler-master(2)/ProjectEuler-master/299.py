import fractions
import sys

class Problem():
    def solve(self):
        assert(self.get(100) == 92)
        assert(self.get(100000) == 320471)
        print(self.get(100000000))

    def get(self, bound):
        incenter_case_count = self.count_incenter_case(bound)
        parallel_case_count = self.count_parallel_case(bound)
        return incenter_case_count + parallel_case_count

    def count_incenter_case(self, bound):
        result = 0
        stack = [(0, 1, 1, 1)]
        while stack:
            a, b, c, d = stack.pop()
            n = a + c
            m = b + d
            legs_length = m**2 - n**2 + 2 * m * n
            if legs_length >= bound:
                continue
            if (m - n) % 2 != 0:
                result += ((bound - 1) // legs_length) * 2
            stack.append((a, b, n, m))
            stack.append((n, m, c, d))
        print("count_incenter_case =>", result)
        return result   

    def count_parallel_case(self, bound):
        result = 0
        stack = [(0, 1, 1, 0)]
        while stack:
            a, b, c, d = stack.pop()
            n = a + c
            m = b + d
            b_side = m**2 + 2 * m * n + 2 * n**2
            if b_side >= bound:
                continue
            if m % 2 != 0:
                result += ((bound - 1) // (b_side * 2))
            stack.append((a, b, n, m))
            stack.append((n, m, c, d))
        print("count_parallel_case =>", result)
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

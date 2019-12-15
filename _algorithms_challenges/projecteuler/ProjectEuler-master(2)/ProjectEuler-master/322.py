
import bisect
import itertools
import sys

class BaseConverter():
    def convert_decimal(self, n, base):
        reversed_rep = []
        d = n
        while d:
            d, r = divmod(d, base)
            reversed_rep.append(r)
        return reversed_rep[::-1]

    def convert_rep(self, rep, base):
        result = 0
        for digit in rep:
            result = result * base + digit
        return result

class Problem():
    def __init__(self):
        self.rep = None
        self.solution = None
        self.hashed_solution = None

    def solve(self):
        for m, n in [(10**9, 10**7 - 10), (10**18, 10**12 - 10)]:
            print(m, n, "=>", self.get(m, n))

    def get(self, m, n):
        self.rep = self.__get_rep(n)
        self.solution, self.hashed_solution = self.__get_solution(self.rep)
        count = self.__get_nondivided_count(m)
        print("count =>", count)
        return m - n - count[2] - count[5] + count[10]

    def __get_rep(self, n):
        converter = BaseConverter()
        return { 
            2 : converter.convert_decimal(n, 2),
            5 : converter.convert_decimal(n, 5),
        }

    def __get_solution(self, rep):
        converter = BaseConverter()
        solution = {}
        hashed_solution = {}
        for base in rep:
            solution[base] = []
            range_list = [range(digit, base) for digit in rep[base]]
            for x in itertools.product(*range_list):
                solution[base].append(converter.convert_rep(x, base))
            hashed_solution[base] = set(solution[base])
        print("2 (ordered) =>", solution[2][:5])
        print("5 (ordered) =>", solution[5][:5])
        print("2 (hashed) =>", len(hashed_solution[2]))
        print("5 (hashed) =>", len(hashed_solution[5]))
        return solution, hashed_solution

    def __get_nondivided_count(self, m):
        period_solution_count = {}
        period = {}
        q, r = {}, {}
        count = {}
        for base in self.rep:
            period_solution_count[base] = len(self.solution[base])
            period[base] = base**(len(self.rep[base]))
            q[base], r[base] = divmod(m, period[base])
            count[base] = q[base] * period_solution_count[base] + bisect.bisect(self.solution[base], r[base])

        count[10] = 0
        for period_pos in range(q[5] + 1):
            for x in self.solution[5]:
                y = period[5] * period_pos + x
                if y < m and (y % period[2]) in self.hashed_solution[2]:
                    count[10] += 1
                    print("found =>", y, "at period_pos =>", period_pos)
        return count

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())


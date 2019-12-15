import operator
import sys

class Problem():
    def solve(self):
        print(self.get(1000, 10))
        print(self.get(100000000, 100000))
    
    def get(self, u, k):
        divisor_count_table = {}
        for i in range(u + 1):
            divisor_count_table[i] = 1
        for i in range(2, u + 1):
            if i % 1000000 == 0:
                print("i =>", i)
            if divisor_count_table[i] != 1:
                continue
            for j in range(i, u + 1, i):
                d = j
                e = 0
                while d % i == 0:
                    d //= i
                    e += 1
                divisor_count_table[j] *= (e + 1)
        print("Completed divisor count table")

        sorted_table = sorted(divisor_count_table.items(), key=operator.itemgetter(1), reverse=True)
        print("Completed sorting divisor count table")

        fill_count = 0
        query_table = [None for _ in range(u - k + 1)]
        for n, divisor_count in sorted_table:
            for i in range(n - k, n):
                if i > u - k:
                    break
                if query_table[i] is None:
                    query_table[i] = divisor_count
                    fill_count += 1
            if fill_count == u - k + 1:
                break
            if n % 100000 == 0:
                print(n, divisor_count, fill_count)
        return sum(query_table)

    def __debug_divisor_count_table(self, divisor_count_table, u, k):
        rv = []
        for i in range(u + 1):
            rv.append(divisor_count_table[i])
        print(rv)
        result = []
        for i in range(1, u - k + 2):
            print(i, rv[i : i + k], max(rv[i : i+k]))
            result.append(max(rv[i : i+k]))
        print(result)
        print(sum(result), len(result))

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

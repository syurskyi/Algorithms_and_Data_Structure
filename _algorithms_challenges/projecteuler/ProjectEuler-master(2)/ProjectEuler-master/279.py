import sys

class Problem():
    def solve(self):
        print(self.get(10**8))

    def get(self, perimeter_bound):
        count_90 = self.count_90_triangle(perimeter_bound)
        print("count_90 =>", count_90)
        count_60 = self.count_60_triangle(perimeter_bound)
        print("count_60 =>", count_60)
        count_120 = self.count_120_triangle(perimeter_bound)
        print("count_120 =>", count_120)
        return count_90 + count_60 + count_120

    def count_90_triangle(self, perimeter_bound):
        result = 0
        stack = [(0, 1, 1, 1)]
        while stack:
            a, b, c, d = stack.pop()
            n = a + c
            m = b + d
            perimeter = 2 * m * (m + n)
            if perimeter > perimeter_bound:
                continue
            if (m - n) % 2 != 0:
                result += (perimeter_bound // perimeter)
            stack.append((a, b, n, m))
            stack.append((n, m, c, d))
        return result

    def count_60_triangle(self, perimeter_bound):
        result = perimeter_bound // 3
        stack = [(0, 1, 1, 1)]
        while stack:
            a, b, c, d = stack.pop()
            n = a + c
            m = b + d
            perimeter = (m + 2 * n) * (2 * m + n)
            if perimeter > 3 * perimeter_bound:
                continue
            g = 3 if (m - n) % 3 == 0 else 1    
            result += ((g * perimeter_bound) // perimeter)
            stack.append((a, b, n, m))
            stack.append((n, m, c, d))
        return result

    def count_120_triangle(self, perimeter_bound):
        result = 0
        stack = [(0, 1, 1, 1)]
        while stack:
            a, b, c, d = stack.pop()
            n = a + c
            m = b + d
            perimeter = (m + n) * (2 * m + n)
            if perimeter > perimeter_bound:
                continue
            if (m - n) % 3 != 0:
                result += perimeter_bound // perimeter
            stack.append((a, b, n, m))
            stack.append((n, m, c, d))
        return result        

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

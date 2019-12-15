import sys

class RoundedSquareRoot():
    def get(self, n):
        d = len(str(n))
        x_list = [2 * 10**((d - 1) // 2) if d % 2 == 1 else 7 * 10**((d - 2) // 2)]
        while True:
            x = x_list[-1]
            next_x = (x + (n + x - 1) // x) // 2
            if next_x == x:
                break
            else:
                x_list.append(next_x)
        #print(n, d, x_list)
        return len(x_list)

class Problem():
    def solve(self):
        print(self.get_naive(5))
        print(self.get(14))

    def get_naive(self, d):
        result = 0
        rounded_square_root = RoundedSquareRoot()
        for n in range(10**(d - 1), 10**d):
            result += rounded_square_root.get(n)
        return result / (9 * 10**(d - 1))

    def get(self, d):
        iteration_count = 0

        x0 = 2 * 10**((d - 1) // 2) if d % 2 == 1 else 7 * 10**((d - 2) // 2)
        n0_interval = [10**(d - 1), 10**d - 1]
        initial_state = (x0, n0_interval, 1)
        dfs_stack = [initial_state]
        while dfs_stack:
            x, n_interval, depth = dfs_stack[-1]
            dfs_stack.pop(-1)
            m_interval = self.__get_m_interval(x, n_interval)    
            for m in range(m_interval[0], m_interval[1] + 1):
                next_n_interval = self.__get_n_interval(x, m)
                next_n_interval[0] = max(next_n_interval[0], n_interval[0])
                next_n_interval[1] = min(next_n_interval[1], n_interval[1])
                next_state = (m, next_n_interval, depth + 1)
                if x == m:
                    iteration_count += depth * (next_n_interval[1] - next_n_interval[0] + 1)
                    #print("exit =>", x, next_n_interval, depth)
                    continue
                dfs_stack.append(next_state)

        return iteration_count / (9 * 10**(d - 1))

    def __get_m_interval(self, x, n_interval):
        return [(x + (n + x - 1) // x) // 2 for n in n_interval]

    def __get_n_interval(self, x, m):
        return [(2 * m - 1) * x - x**2 + 1, (2 * m + 1) * x - x**2]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

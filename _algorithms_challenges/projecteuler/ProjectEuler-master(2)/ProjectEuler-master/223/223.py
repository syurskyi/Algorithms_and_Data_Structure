import sys

class Problem():
    def solve(self, bound):
        count = 0
        dfs_stack = [(1, 2, 2), (1, 1, 1)]
        while dfs_stack:
            a, b, c = dfs_stack[-1]
            dfs_stack.pop(-1)
            count += 1
            if a < b and 7*c + 5*b - 5*a <= bound:
                dfs_stack.append((2*c + b - 2*a, 2*c + 2*b - a, 3*c + 2*b - 2*a))
            if 7*c + 5*b + 5*a <= bound:
                dfs_stack.append((2*c + b + 2*a, 2*c + 2*b + a, 3*c + 2*b + 2*a))
            if 7*c - 5*b + 5*a <= bound:
                dfs_stack.append((2*c - 2*b + a, 2*c - b + 2*a, 3*c - 2*b + 2*a))
        print(count)

def main():
    problem = Problem()
    problem.solve(25000000)
    
if __name__ == '__main__':
    sys.exit(main())

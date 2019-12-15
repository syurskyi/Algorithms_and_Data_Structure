import sys

class Problem():
    def solve(self):
        print(self.get(8))
        print(self.get(12000))

    def get(self, d):
        count = 0
        left, right = 3, 2
        dfs_stack = []
        while True:
            mediant = left + right
            if mediant > d:
                if not dfs_stack:
                    break
                left = right
                right = dfs_stack.pop()
            else:
                count += 1
                dfs_stack.append(right)
                right = mediant
        return count

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

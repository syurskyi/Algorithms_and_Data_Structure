import math
import sys

class Problem():
    def solve(self):
        print(self.find_max_n((3, 3)))

    def find_max_n(self, pos):
        corresponding_size = self.find_min_size(pos)
        n = 0
        initial_state = { 'pos': (1, 0), 'index': (0, 0) }
        dfs_stack = [initial_state]
        while dfs_stack:
            top = dfs_stack[-1]
            dfs_stack.pop(-1)
            left_state, upper_state = self.get_next_states(top)
            if top['size'] < corresponding_size:
                continue
            n += 1
            if n % 10000 == 0:
                print(n, top)
            dfs_stack.append(left_state)
            dfs_stack.append(upper_state)
        return n

    def find_min_size(self, pos):
        min_size_so_far = 1
        initial_state = { 'pos': (1, 0), 'index': (0, 0) }
        dfs_stack = [initial_state]
        while dfs_stack:
            top = dfs_stack[-1]
            dfs_stack.pop(-1)
            i, j = top['index']
            if i > pos[0] or j > pos[1]:
                continue
            left_state, upper_state = self.get_next_states(top)
            if i == pos[0] and j == pos[1]:
                min_size_so_far = min(top['size'], min_size_so_far)
                continue
            dfs_stack.append(left_state)
            dfs_stack.append(upper_state)
        return min_size_so_far

    def get_next_states(self, state):
        a, b = state['pos']
        i, j = state['index']
        x = (a - b + math.sqrt((b - a)**2 + 4)) / 2
        y = x - a + b
        state['size'] = ((a - x)**2 + (b - y)**2) / 2
        left_state = { 'pos': (x, b), 'index': (i + 1, j) }
        upper_state = { 'pos': (a, y), 'index': (i, j + 1) }
        return left_state, upper_state

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
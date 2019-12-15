import sys

class Problem():
    def solve(self):
        for n in [1000]:
            print(n, "=>", self.get(n))

    def get(self, n):
        result = 0
        winning_states = {}
        for x in range(n + 1):
            winning_states[x] = {}
            for y in range(x, n + 1):
                winning_states[x][y] = {}
                for z in range(y, n + 1):
                    winning_states[x][y][z] = False
        print('init winning_states done')
        for x in range(n + 1):
            print('x =>', x)
            for y in range(x, n + 1):
                for z in range(y, n + 1):
                    if winning_states[x][y][z]:
                        continue
                    result += (x + y + z)            
                    for i in range(1, n - x + 1):
                        sorted_x, sorted_y, sorted_z = sorted((x + i, y, z))
                        winning_states[sorted_x][sorted_y][sorted_z] = True
                    for i in range(1, n - y + 1):
                        sorted_x, sorted_y, sorted_z = sorted((x, y + i, z))
                        winning_states[sorted_x][sorted_y][sorted_z] = True
                    for i in range(1, n - z + 1):
                        sorted_x, sorted_y, sorted_z = sorted((x, y, z + i))
                        winning_states[sorted_x][sorted_y][sorted_z] = True
                    for i in range(1, n - max(x, y) + 1):
                        sorted_x, sorted_y, sorted_z = sorted((x + i, y + i, z))
                        winning_states[sorted_x][sorted_y][sorted_z] = True 
                    for i in range(1, n - max(y, z) + 1):
                        sorted_x, sorted_y, sorted_z = sorted((x, y + i, z + i))
                        winning_states[sorted_x][sorted_y][sorted_z] = True
                    for i in range(1, n - max(z, x) + 1):
                        sorted_x, sorted_y, sorted_z = sorted((x + i, y, z + i))
                        winning_states[sorted_x][sorted_y][sorted_z] = True
                    for i in range(1, n - max(x, y, z) + 1):
                        sorted_x, sorted_y, sorted_z = sorted((x + i, y + i, z + i))
                        winning_states[sorted_x][sorted_y][sorted_z] = True
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

import sys
        
class Problem():
    def solve(self):
        status = [[0] for _ in range(51)]
        status[50] = [1]
        transition_matrix = self.init_transition_matrix()
        expected_value = 0.0
        for i in range(1, 150001):
            status[0][0] = 0
            status = self.multiply(transition_matrix, status)
            expected_value += status[0][0] * i
            if i % 1000 == 0:
                print(i, expected_value)
        print(expected_value)

    def init_transition_matrix(self):
        transition_matrix = [[0 for _ in range(51)] for _ in range(51)]
        transition_matrix[0][0] = 1
        transition_matrix[0][1] = 2/9
        transition_matrix[1][1] = 1/2 + 1/36
        transition_matrix[2][1] = 2/9
        transition_matrix[3][1] = 1/36
        for i in range(2, 49):
            transition_matrix[i - 2][i] = 1/36
            transition_matrix[i - 1][i] = 2/9
            transition_matrix[i][i] = 1/2
            transition_matrix[i + 1][i] = 2/9
            transition_matrix[i + 2][i] = 1/36
        transition_matrix[47][49] = 1/36
        transition_matrix[48][49] = 2/9
        transition_matrix[49][49] = 1/2 + 1/36
        transition_matrix[50][49] = 2/9
        transition_matrix[48][50] = 1/36 + 1/36
        transition_matrix[49][50] = 2/9 + 2/9
        transition_matrix[50][50] = 1/2
        return transition_matrix

    def multiply(self, x, y):
        rv = [[0 for j in range(len(y[0]))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    rv[i][j] += x[i][k] * y[k][j]
        return rv

    def benchmark(self):
        import random
        N = 100
        total_step_count = 0
        for i in range(N):
            player_pos = [0, 50]
            step_count = 0
            while player_pos[0] != player_pos[1]:
                step_count += 1
                dice = [random.randint(1, 6), random.randint(1, 6)]
                for player_id in range(2):
                    if dice[player_id] == 1:
                        player_pos[player_id] = (player_pos[player_id] - 1) % 100
                    elif dice[player_id] == 6:
                        player_pos[player_id] = (player_pos[player_id] + 1) % 100
            total_step_count += step_count
        print(total_step_count / N)

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

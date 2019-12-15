import sys
        
class Problem():
    def solve(self):
        #self.benchmark(100)
        status = [[0.0] for _ in range(999)]
        status[0] = [1.0]
        transition_matrix = self.init_transition_matrix()
        expected_value = 0.0
        for i in range(1, 301):
            status[998] = [0.0]
            status = self.multiply(transition_matrix, status)
            expected_value += status[998][0] * i
            print(expected_value, status[998][0], i)
        print(expected_value)

    def init_transition_matrix(self):
        m = [[0.0 for _ in range(999)] for _ in range(999)]
        for k in range(499):
            m[k][k] = (k+1) / 1000
            if k < 498:
                m[k+1][k] = (1000 - 2*k - 2) / 1000
            m[499 + k][k] = 1 / 1000
            m[998][k] = k / 1000
        for k in range(499, 998):
            m[k][k] = (k - 499 + 1) / 1000
            if k < 997:
                m[k+1][k] = (1000 - 2 * (k - 499) - 2) / 1000
            m[998][k] = (k - 499 + 1) / 1000
        m[998][998] = 1.0
        return m
    
    def multiply(self, x, y):
        rv = [[0 for j in range(len(y[0]))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    rv[i][j] += x[i][k] * y[k][j]
        return rv

    def benchmark(self, N):
        import random
        total_step_count = 0
        for i in range(N):
            saw_plates = set()
            step_count = 0
            while True:
                step_count += 1
                new_plate = random.randint(0, 1000)
                if (1000 - new_plate) in saw_plates:
                    break
                else:
                    saw_plates.add(new_plate)
            total_step_count += step_count
        print(total_step_count / N)

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

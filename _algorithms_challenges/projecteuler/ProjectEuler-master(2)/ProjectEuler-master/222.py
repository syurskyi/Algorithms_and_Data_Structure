from itertools import permutations
from math import sqrt
import sys

class Problem():
    def solve(self):
        #self.benchmark()
        ball_arrangement = [49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
        print(self.get(ball_arrangement))
    
    def benchmark(self):
        best_arrangement_so_far = None
        shortest_so_far = 30000
        all_balls = [_ for _ in range(40, 51)]
        for ball_arrangement in permutations(all_balls):
            total_distance = self.get(ball_arrangement)
            if total_distance < shortest_so_far:
                shortest_so_far = total_distance
                best_arrangement_so_far = ball_arrangement
                print(best_arrangement_so_far, shortest_so_far)

        print(best_arrangement_so_far, shortest_so_far)

    def get(self, ball_arrangement):
        distance = ball_arrangement[0] + ball_arrangement[-1]
        ball_count = len(ball_arrangement)
        for i in range(0, ball_count - 1):
            distance += self.get_distance(ball_arrangement[i], ball_arrangement[i+1])
        return distance

    def get_distance(self, a, b):
        return sqrt(200 * (a + b - 50))

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())

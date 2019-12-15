import sys

class HeighwayDragon():
    def __init__(self, order):
        self.order = order

    def simulate(self, step):
        dragon = "Fa"
        rule_a = "ARBFR"
        rule_b = "LFALB"
        for i in range(self.order):
            dragon = dragon.replace("a", rule_a).replace("b", rule_b).replace("A", "a").replace("B", "b")
        curr_step = 0
        curr_pos = 0
        spot, direction = [0, 0], [0, 1]
        while curr_step < step:
            c0 = dragon[curr_pos]
            if c0 == "F":
                spot[0] += direction[0]
                spot[1] += direction[1]
                curr_step += 1
            elif c0 == "L":
                direction[0], direction[1] = -direction[1], direction[0]
            elif c0 == "R":
                direction[0], direction[1] = direction[1], -direction[0]
            curr_pos += 1
        return spot

class Problem():
    def solve(self):
        self.benchmark()
        for step in [500, 10**12]:
            print(step, '=>', self.get(step))
    
    def benchmark(self):
        heighway_dragon = HeighwayDragon(10)
        print(heighway_dragon.simulate(500))
    
    def get(self, step):
        spot = [0, 1]
        curr_step = 1
        while curr_step < step:
            spot = [spot[0] + spot[1], -spot[0] + spot[1]]
            curr_step *= 2
        if curr_step == step:
            return spot
        else:
            rest_spot = self.get(curr_step - step)
            return [spot[0] - rest_spot[1], spot[1] + rest_spot[0]]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

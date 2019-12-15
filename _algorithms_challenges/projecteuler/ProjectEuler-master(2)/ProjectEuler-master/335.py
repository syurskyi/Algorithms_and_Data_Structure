import sys

class PeterSimulator():
    def simulate(self, bowl_count):
        result = 0
        state = [1] * bowl_count
        curr_bowl = 0
        while True:
            result += 1
            beans = state[curr_bowl]
            state[curr_bowl] = 0
            for i in range(1, beans + 1):
                state[(curr_bowl + i) % bowl_count] += 1
            curr_bowl = (curr_bowl + beans) % bowl_count
            if self.__is_initial_state(state):
                break
        return result

    def __is_initial_state(self, state):
        for beans in state:
            if beans != 1:
                return False
        return True

class Problem():
    def solve(self):
        #self.benchmark()
        print(self.get(10**18, 7**9))

    def benchmark(self):    
        simulator = PeterSimulator()
        print([simulator.simulate(2**k + 1) for k in range(10)])

    def get(self, n, mod):
        a = ((pow(4, n + 1, mod) - 1) * self.__mod_inverse(4 - 1, mod)) % mod
        b = ((pow(3, n + 1, mod) - 1) * self.__mod_inverse(3 - 1, mod)) % mod
        c = (2 * (pow(2, n + 1, mod) - 1)) % mod
        return (a - b + c) % mod

    def __mod_inverse(self, a, mod):
        g, x, y = self.__extended_gcd(a, mod)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % mod

    def __extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.__extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

import sys

class Matrix():
    def multiply(self, x, y, mod):
        results = [[0 for j in range(len(y[0]))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    results[i][j] = (results[i][j] + x[i][k] * y[k][j]) % mod
        return results

    def power(self, x, power, mod):
        base = x
        rv = self.identity_matrix(len(x))
        while power > 0:
            if power & 1 == 1:
                rv = self.multiply(rv, base, mod)
            base = self.multiply(base, base, mod)
            power >>= 1
        return rv

    def identity_matrix(self, n):
        rv = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            rv[i][i] = 1
        return rv

class Problem():
    def __init__(self):
        self.q = 100000007
        self.f = self.__init_f()
        self.transition_matrix = self.__init_transition_matrix()

    def __init_f(self):
        base_sequence = [
            1,
            229,
            117805,
            64647289,
            35669566217,
            19690797527709,
            10870506600976757,
            6001202979497804657,
            3313042830624031354513,
            1829008840116358153050197,
            1009728374600381843221483965,
            557433823481589253332775648233,
            307738670509229621147710358375321,
            169891178715542584369273129260748045,
            93790658670253542024618689133882565125,
            51778366130057389441239986148841747669217,
            28584927722109981792301610403923348017948449,
            15780685138381102545287108197623881881376915397,
            8711934690116480171969789787256390490181022415693,
            4809538076408327645969201260680362259835079086427481,
            2655168723276120197512956906659822833388644760430125609,
            1465820799640802552047402979496052449322258430218930512765,
            809225642733724788155919446555896648357335949987871250500245,
        ]
        return [[i % self.q] for i in base_sequence[::-1]]

    def __init_transition_matrix(self):
        matrix = [[0 for j in range(23)] for i in range(23)]
        coefficient_sequence = [
            679,
            -76177,
            3519127,
            -85911555, 
            1235863045,
            -11123194131, 
            65256474997, 
            -257866595482,
            705239311926,
            -1363115167354,
            1888426032982,
            -1888426032982,
            1363115167354,
            -705239311926, 
            257866595482, 
            -65256474997, 
            11123194131, 
            -1235863045,
            85911555,
            -3519127,
            76177,
            -679,
            1,
        ]
        for j in range(23):
            matrix[0][j] = coefficient_sequence[j] % self.q
        for i in range(1, 23):
            matrix[i][i-1] = 1
        return matrix

    def solve(self):
        for n in [2, 4, 10, 10**3, 10**6, 10**10000]:
            print(n, '=>', self.get(n))

    def get(self, n):
        m = n // 2
        if m < 23:
            return self.f[22 - m][0]
        x = Matrix().power(self.transition_matrix, m - 22, self.q)
        y = Matrix().multiply(x, self.f, self.q)
        return y[0][0]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

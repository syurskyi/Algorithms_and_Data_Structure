from fractions import Fraction
import sys

class PlatonicDiceProblem():
    def __init__(self):
        self.expected_value = {}
        self.variance = {}    
        
    def get_variance(self):
        self._init_expected_value()
        self._init_variance()
        return self.variance[20]
    
    def _init_expected_value(self):
        dice_types = [4, 6, 8, 12, 20]
        for i in range(len(dice_types)):        
            self.expected_value[dice_types[i]] = Fraction(1)
            for j in range(i+1):
                self.expected_value[dice_types[i]] *= self.E(dice_types[j])    
    
    def _init_variance(self):
        self.variance[4] = self.Var(4)
        dice_types = [4, 6, 8, 12, 20]
        for i in range(1, len(dice_types)):
            curr_dice = dice_types[i]
            prev_dice = dice_types[i-1]
            self.variance[curr_dice] \
                    = self.Var(curr_dice) * self.expected_value[prev_dice] \
                    + self.E(curr_dice)**2 * self.variance[prev_dice]
    
    def E(self, n):
        return Fraction(n+1, 2)

    def Var(self, n):
        return Fraction(n**2 - 1, 12)
        
def main():
    problem = PlatonicDiceProblem()
    print(float(problem.get_variance()))
    
if __name__ == '__main__':
    sys.exit(main())

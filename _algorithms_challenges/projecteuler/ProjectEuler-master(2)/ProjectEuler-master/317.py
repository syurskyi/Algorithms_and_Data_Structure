import math
import sys
    
def shell_integration(h, v, g):
    x2 = v**2 / g**2 * (v**2 + 2*g*h)
    return math.pi * (x2 * (v**2/(2*g) + h) - 0.25 * x2**2 * g / v**2)
    
def main():
    print(shell_integration(h=100.0, v=20.0, g=9.81))
    
if __name__ == '__main__':
    sys.exit(main())

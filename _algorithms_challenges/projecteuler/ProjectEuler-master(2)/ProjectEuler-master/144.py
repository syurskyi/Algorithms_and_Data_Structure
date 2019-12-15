import math
import sys

def normalize(v):
    length = math.sqrt(v[0] * v[0] + v[1] * v[1])
    return (v[0] / length, v[1] / length)

def dot(u, v):    
    return u[0] * v[0] + u[1] * v[1]
    
def direction_vector(p, q):
    return (q[0] - p[0], q[1] - p[1])

def normal_vector(p):
    return normalize((4 * p[0], p[1]))

def reflect(v, n):
    return (2 * dot(v, n) * n[0] - v[0], 2 * dot(v, n) * n[1] - v[1])

def solve(v, p):
    t = (-8 * v[0] * p[0] - 2 * v[1] * p[1])/(4 * v[0] * v[0] + v[1] * v[1])
    return (v[0] * t + p[0], v[1] * t + p[1])
    
def main():
    p = (0.0, 10.1)
    q = (1.4, -9.6)
    v = direction_vector(q, p)
    for i in range(1, 1000):
        n = normal_vector(q)
        r = reflect(v, n)
        s = solve(r, q)
        v = direction_vector(s, q)
        q = s
        print(s)
        if s[0] >= -0.01 and s[0] <= 0.01 and s[1] > 0:
            print(i)
            break        
    
if __name__ == '__main__':
    sys.exit(main())

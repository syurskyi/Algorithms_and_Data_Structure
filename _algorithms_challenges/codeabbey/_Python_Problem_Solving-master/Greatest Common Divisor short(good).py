# Problem #26
def gcdlcm():
    for i in range(int(input())):
        a, b = map(int, input().split())
        g = gcd(a, b)
        print('({} {})'.format(g, a * b // g), end=' ')

def gcd(a, b):
    if(b == 0):
        return a;
    return gcd(b, a % b)
    
gcdlcm()
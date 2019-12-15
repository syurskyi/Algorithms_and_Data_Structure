import sys
from decimal import *

def f(x):
    base2 = Decimal('2')
    factor = Decimal('10') ** Decimal('-9')
    n = Decimal('30.403243784') - x * x
    return base2 ** n // 1 * factor
        
def main():
    u_list = []
    n = 0
    u = Decimal(-1)
    u_list.append(u)
    is_duplicated = False
    begin_cycle, end_cycle = -1, -1
    while not is_duplicated:
        n += 1
        u = f(Decimal(u))
        for i in range(len(u_list) - 1):
            if u == u_list[i]:
                begin_cycle, end_cycle = i, n
                is_duplicated = True
                break
        u_list.append(u)
    print(u_list, begin_cycle, end_cycle)
    print(Decimal('0.681175878') + Decimal('1.029461839'))
    
if __name__ == '__main__':
    sys.exit(main())
